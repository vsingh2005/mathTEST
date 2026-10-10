/**
 * Kids STEM Studio - Storage & Progress State Manager
 * 
 * Manages state persistence, crash recovery, gated curriculum unlock thresholds,
 * and offline sync queues for students.
 */

export class StorageManager {
  static KEYS = {
    SESSION: 'kss_session',
    ACTIVE_EXAM_STATE: 'kss_active_exam_state',
    STUDENT_PROGRESS: 'kss_student_progress',
    OFFLINE_SYNC_QUEUE: 'kss_offline_sync_queue',
    SELECTED_TRACK: 'selectedTrack'
  };

  /**
   * Safe getter for localStorage / sessionStorage with fallback
   */
  static getItem(key, defaultValue = null) {
    try {
      let val = null;
      try { val = localStorage.getItem(key); } catch (e) {}
      if (val === null || val === undefined) {
        try { val = sessionStorage.getItem(key); } catch (e) {}
      }
      if (val === null || val === undefined) return defaultValue;
      try {
        return JSON.parse(val);
      } catch (e) {
        // Return raw string if not JSON format
        return val;
      }
    } catch (e) {
      return defaultValue;
    }
  }

  /**
   * Safe setter for localStorage
   */
  static setItem(key, value) {
    try {
      localStorage.setItem(key, JSON.stringify(value));
      return true;
    } catch (e) {
      console.warn(`[StorageManager] Failed to write ${key}:`, e);
      return false;
    }
  }

  /* ----------------------------------------------------
     EXAM CRASH RECOVERY & IN-PROGRESS AUTO-SAVE
     ---------------------------------------------------- */
  static saveExamState(state) {
    try {
      const payload = {
        currentQuestionIndex: state.currentQuestionIndex,
        userAnswers: state.userAnswers,
        questionsServed: state.questionsServed,
        secondsElapsed: state.secondsElapsed,
        selectedTrack: state.selectedTrack,
        streak: state.streak,
        maxStreak: state.maxStreak,
        activeDifficulty: state.activeDifficulty,
        savedAt: Date.now()
      };
      sessionStorage.setItem(this.KEYS.ACTIVE_EXAM_STATE, JSON.stringify(payload));
    } catch (e) {
      console.warn('[StorageManager] Auto-save exam failed:', e);
    }
  }

  static getExamState() {
    try {
      const raw = sessionStorage.getItem(this.KEYS.ACTIVE_EXAM_STATE);
      if (!raw) return null;
      const state = JSON.parse(raw);
      // Valid if less than 3 hours old
      if (Date.now() - state.savedAt < 3 * 60 * 60 * 1000) {
        return state;
      }
      this.clearExamState();
      return null;
    } catch (e) {
      return null;
    }
  }

  static clearExamState() {
    try {
      sessionStorage.removeItem(this.KEYS.ACTIVE_EXAM_STATE);
    } catch (e) {}
  }

  /* ----------------------------------------------------
     STUDENT PROGRESS & GATED LESSON ACCESS
     ---------------------------------------------------- */
  static getProgress() {
    const defaultProgress = {
      testedGrade: null,          // e.g. 4
      testedScore: null,          // e.g. 11/15
      unlockedLessonIndex: {      // Highest unlocked lesson number per grade
        "3": 25,                  // All Grade 3 unlocked if tested Grade 4+
        "4": 1,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0
      },
      completedLessons: {},       // lessonId -> { score, stars, attempts, completedAt }
      totalStars: 0,
      highestStreak: 0,
      badges: []
    };
    const progress = this.getItem(this.KEYS.STUDENT_PROGRESS, defaultProgress);

    // If active user is student1, automatically unlock all modules/lessons across all grades
    let sessionUser = '';
    try {
      const rawSession = localStorage.getItem(this.KEYS.SESSION) || sessionStorage.getItem(this.KEYS.SESSION);
      if (rawSession) {
        if (rawSession.startsWith('{')) {
          const parsed = JSON.parse(rawSession);
          sessionUser = parsed.username || (parsed.user && (parsed.user.username || parsed.user.display_name)) || parsed.studentName || '';
        } else {
          sessionUser = rawSession;
        }
      }
    } catch (e) {}

    if (String(sessionUser).toLowerCase() === 'student1') {
      if (!progress.unlockedLessonIndex) progress.unlockedLessonIndex = {};
      for (let g = 3; g <= 8; g++) {
        progress.unlockedLessonIndex[String(g)] = 25;
      }
      if (!progress.testedGrade) progress.testedGrade = 6;
    }

    return progress;
  }

  static saveProgress(progress) {
    this.setItem(this.KEYS.STUDENT_PROGRESS, progress);
  }

  /**
   * Determines if a student is permitted to access a specific lesson.
   * STRICT GATING: Can only access lessons up to tested placement level,
   * OR unlocked consecutively by completing previous lesson with >= 80%.
   */
  static isLessonUnlocked(grade, lessonNumber) {
    let sessionUser = '';
    try {
      const rawSession = localStorage.getItem(this.KEYS.SESSION) || sessionStorage.getItem(this.KEYS.SESSION);
      if (rawSession) {
        if (rawSession.startsWith('{')) {
          const parsed = JSON.parse(rawSession);
          sessionUser = parsed.username || (parsed.user && (parsed.user.username || parsed.user.display_name)) || parsed.studentName || '';
        } else {
          sessionUser = rawSession;
        }
      }
    } catch (e) {}

    if (String(sessionUser).toLowerCase() === 'student1') {
      return true; // All modules are unlocked for student1
    }

    const progress = this.getProgress();
    const gradeStr = String(grade);
    const maxUnlocked = progress.unlockedLessonIndex[gradeStr] || 0;
    
    // First lesson of a tested grade is always unlocked once placed
    if (lessonNumber <= maxUnlocked) {
      return true;
    }
    return false;
  }

  /**
   * Records completed worksheet and unlocks next lesson consecutively if score >= 80% (or >= 2 stars)
   */
  static recordLessonCompletion(grade, lessonNumber, scorePercent, starsEarned) {
    const progress = this.getProgress();
    const gradeStr = String(grade);
    const lessonId = `G${grade}_L${String(lessonNumber).padStart(2, '0')}`;

    const prev = progress.completedLessons[lessonId] || { attempts: 0, stars: 0, score: 0 };
    const bestStars = Math.max(prev.stars, starsEarned);
    const bestScore = Math.max(prev.score, scorePercent);

    progress.completedLessons[lessonId] = {
      grade,
      lessonNumber,
      score: bestScore,
      stars: bestStars,
      attempts: prev.attempts + 1,
      completedAt: new Date().toISOString()
    };

    // Calculate total stars
    let totalStars = 0;
    Object.values(progress.completedLessons).forEach(l => {
      totalStars += (l.stars || 0);
    });
    progress.totalStars = totalStars;

    // Consecutively unlock next lesson if mastered (>= 80% or >= 2 stars)
    const currentMax = progress.unlockedLessonIndex[gradeStr] || 1;
    if ((scorePercent >= 80 || starsEarned >= 2) && lessonNumber >= currentMax) {
      progress.unlockedLessonIndex[gradeStr] = lessonNumber + 1;
    }

    this.saveProgress(progress);
    return progress;
  }

  /**
   * Sets initial unlocked threshold upon placement test completion
   */
  static initializePlacementThreshold(placedGrade) {
    const progress = this.getProgress();
    progress.testedGrade = placedGrade;

    // Unlock all lessons for grades prior to placed grade
    for (let g = 3; g < placedGrade; g++) {
      progress.unlockedLessonIndex[String(g)] = 25;
    }
    // Set tested grade to start at lesson 1 if not already higher
    if (!progress.unlockedLessonIndex[String(placedGrade)] || progress.unlockedLessonIndex[String(placedGrade)] < 1) {
      progress.unlockedLessonIndex[String(placedGrade)] = 1;
    }

    this.saveProgress(progress);
    return progress;
  }

  /* ----------------------------------------------------
     OFFLINE QUEUE FOR REST API SYNC RESILIENCE
     ---------------------------------------------------- */
  static queueOfflineSync(action, payload) {
    const queue = this.getItem(this.KEYS.OFFLINE_SYNC_QUEUE, []);
    queue.push({
      id: 'sync_' + Date.now() + '_' + Math.random().toString(36).substr(2, 6),
      action,
      payload,
      timestamp: Date.now()
    });
    this.setItem(this.KEYS.OFFLINE_SYNC_QUEUE, queue);
  }

  static getPendingSyncs() {
    return this.getItem(this.KEYS.OFFLINE_SYNC_QUEUE, []);
  }

  static removePendingSync(syncId) {
    let queue = this.getItem(this.KEYS.OFFLINE_SYNC_QUEUE, []);
    queue = queue.filter(item => item.id !== syncId);
    this.setItem(this.KEYS.OFFLINE_SYNC_QUEUE, queue);
  }

  /* ----------------------------------------------------
     GLOBAL CLIENT-SIDE ERROR HANDLING
     ---------------------------------------------------- */
  static setupGlobalErrorHandler() {
    window.onerror = function(message, source, lineno, colno, error) {
      console.warn('[KSS Error Monitor]', { message, source, lineno, colno, error });
      return false;
    };

    window.addEventListener('unhandledrejection', function(event) {
      console.warn('[KSS Unhandled Promise Rejection]', event.reason);
    });
  }
}

// Attach globally
if (typeof window !== 'undefined') {
  window.StorageManager = StorageManager;
  StorageManager.setupGlobalErrorHandler();
}
