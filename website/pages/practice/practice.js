/**
 * Kids STEM Studio - Digital Worksheet Practice Engine
 * 
 * Features:
 * - Gated progressive unlocking (only up to placement test grade or consecutive completions)
 * - 3-tier progressive hint scaffolding drawer (Concept 💡 -> Formula 📐 -> Analogy 🤖)
 * - 3-star rating per lesson based on unassisted accuracy
 * - Audio cues & streak flame counter
 * - Interactive visual manipulatives (Fraction bars, Number line, Geoboard)
 * - Digital scratchpad integration
 * - WordPress REST API persistence
 */

import { StorageManager } from '../../shared/js/storage.js';
import { ApiClient } from '../../shared/js/api.js';
import { AuthManager } from '../../shared/js/auth.js';
import { SoundEffectManager } from '../../shared/js/sound.js';
import { Manipulatives } from '../../shared/js/manipulatives.js';
import '../../shared/js/components.js';

class PracticeEngine {
  constructor() {
    this.sound = window.soundManager || new SoundEffectManager();
    this.curriculum = null;
    this.gradeData = {};
    this.activeGrade = 3;
    this.activeLesson = null;
    this.activeQuestions = [];
    this.currentQuestionIdx = 0;
    this.userAnswers = {};
    this.hintsUsed = {};
    this.questionStars = {};
    this.streak = 0;
    this.maxStreak = 0;
  }

  async init() {
    AuthManager.requireAuth('../../login.html');
    AuthManager.updateHeaderUI();

    const progress = StorageManager.getProgress();
    // Default to student's placed grade if available
    if (progress.testedGrade) {
      this.activeGrade = progress.testedGrade;
    }

    await this.loadCurriculum();
    this.renderCurriculumBrowser();
  }

  async loadCurriculum() {
    try {
      const res = await fetch('../../shared/data/curriculum.json');
      this.curriculum = await res.json();
    } catch (e) {
      console.warn('Failed to load curriculum.json:', e);
    }
  }

  async loadGradeQuestions(grade) {
    if (this.gradeData[grade]) return this.gradeData[grade];
    try {
      const res = await fetch(`../../shared/data/grade_${grade}.json`);
      const data = await res.json();
      this.gradeData[grade] = data;
      return data;
    } catch (e) {
      console.warn(`Failed to load grade_${grade}.json:`, e);
      return null;
    }
  }

  setGrade(grade) {
    this.activeGrade = grade;
    this.renderCurriculumBrowser();
  }

  /**
   * Renders curriculum browser with strict prerequisite gating
   */
  renderCurriculumBrowser() {
    const container = document.getElementById('practice-main-view');
    if (!container) return;

    const progress = StorageManager.getProgress();
    const gradeLessons = this.curriculum?.lessons?.filter(l => l.grade === this.activeGrade) || [];

    let tabsHtml = '';
    [3, 4, 5, 6, 7, 8].forEach(g => {
      const isActive = g === this.activeGrade;
      tabsHtml += `
        <button onclick="window.practiceEngine.setGrade(${g})"
                class="px-5 py-2.5 rounded-xl font-extrabold text-sm transition-all ${isActive ? 'bg-sky-500 text-white shadow-md' : 'bg-white text-slate-600 hover:bg-slate-100 border border-slate-200'}">
          Grade ${g}
        </button>
      `;
    });

    let cardsHtml = '';
    gradeLessons.forEach((lesson, idx) => {
      const isUnlocked = StorageManager.isLessonUnlocked(this.activeGrade, lesson.lessonNumber);
      const completion = progress.completedLessons[lesson.lessonId];
      const starsEarned = completion ? completion.stars : 0;

      let starIcons = '';
      for (let s = 1; s <= 3; s++) {
        starIcons += s <= starsEarned ? '⭐' : '☆';
      }

      if (isUnlocked) {
        cardsHtml += `
          <div class="bg-white p-6 rounded-card card-shadow border border-slate-100 hover-lift lesson-card-unlocked flex flex-col justify-between space-y-4">
            <div class="space-y-2">
              <div class="flex items-center justify-between">
                <span class="px-3 py-1 bg-sky-50 text-sky-700 rounded-full font-extrabold text-xs">Lesson ${lesson.lessonNumber}</span>
                <span class="text-sm font-bold text-amber-500">${starIcons}</span>
              </div>
              <h4 class="font-extrabold text-navy-dark text-lg">${lesson.title}</h4>
              <p class="text-slate-500 text-xs leading-relaxed line-clamp-2">${lesson.description}</p>
              <span class="inline-block text-[11px] font-bold text-slate-400 bg-slate-50 px-2 py-0.5 rounded">${lesson.standard}</span>
            </div>
            <button onclick="window.practiceEngine.startLesson('${lesson.lessonId}', ${lesson.lessonNumber})"
                    class="w-full py-3 rounded-xl btn-blue-gradient text-sm font-bold text-center">
              ${completion ? 'Practice Again ↻' : 'Start Lesson 🚀'}
            </button>
          </div>
        `;
      } else {
        cardsHtml += `
          <div class="bg-slate-50 p-6 rounded-card border border-slate-200 lesson-card-locked flex flex-col justify-between space-y-4 opacity-70">
            <div class="space-y-2">
              <div class="flex items-center justify-between">
                <span class="px-3 py-1 bg-slate-200 text-slate-500 rounded-full font-bold text-xs">Lesson ${lesson.lessonNumber}</span>
                <span class="text-base">🔒</span>
              </div>
              <h4 class="font-bold text-slate-500 text-lg">${lesson.title}</h4>
              <p class="text-slate-400 text-xs leading-relaxed line-clamp-2">${lesson.description}</p>
            </div>
            <div class="p-2.5 bg-amber-50 border border-amber-200 rounded-xl text-center">
              <span class="text-xs font-bold text-amber-800">
                🔒 Prerequisite: Complete Lesson ${lesson.lessonNumber - 1} with ≥80%
              </span>
            </div>
          </div>
        `;
      }
    });

    container.innerHTML = `
      <div class="space-y-8">
        <!-- Header Banner -->
        <div class="practice-hero space-y-3">
          <div class="flex items-center space-x-2">
            <span class="px-3 py-1 bg-emerald-100 text-emerald-800 rounded-full font-bold text-xs uppercase">Interactive Worksheets</span>
            <span class="text-xs text-slate-500 font-semibold">• Consecutive Mastery Mode</span>
          </div>
          <h2 class="text-3xl font-black text-navy-dark">Digital Math Practice & Mastery</h2>
          <p class="text-slate-600 text-sm max-w-2xl font-medium">
            Solve standards-aligned math problems step-by-step. Earn up to 3 stars per lesson and build continuous streaks to unlock the next levels!
          </p>
        </div>

        <!-- Grade Selector Tabs -->
        <div class="flex flex-wrap items-center gap-3">
          ${tabsHtml}
        </div>

        <!-- Lessons Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          ${cardsHtml}
        </div>
      </div>
    `;
  }

  /**
   * Starts a practice session for a specific lesson
   */
  async startLesson(lessonId, lessonNumber) {
    const data = await this.loadGradeQuestions(this.activeGrade);
    if (!data) return;

    this.activeLesson = data.lessons.find(l => l.lessonId === lessonId);
    this.activeQuestions = data.questions.filter(q => q.lessonId === lessonId);

    if (this.activeQuestions.length === 0) {
      alert('Questions for this lesson are being compiled. Please try another lesson!');
      return;
    }

    this.currentQuestionIdx = 0;
    this.userAnswers = {};
    this.hintsUsed = {};
    this.questionStars = {};
    this.streak = 0;

    this.renderQuestionView();
  }

  renderQuestionView() {
    const container = document.getElementById('practice-main-view');
    if (!container) return;

    const q = this.activeQuestions[this.currentQuestionIdx];
    const totalQ = this.activeQuestions.length;
    const progressPercent = ((this.currentQuestionIdx + 1) / totalQ) * 100;
    const currentHintsRevealed = this.hintsUsed[this.currentQuestionIdx] || 0;

    // Determine star preview for this question
    let starPreview = '⭐⭐⭐';
    if (currentHintsRevealed === 1) starPreview = '⭐⭐☆ (1 Hint)';
    else if (currentHintsRevealed >= 2) starPreview = '⭐☆☆ (Assisted)';

    container.innerHTML = `
      <div class="max-w-4xl mx-auto space-y-6">
        <!-- Navigation bar -->
        <div class="flex items-center justify-between bg-white p-4 rounded-2xl border border-slate-100 shadow-sm">
          <button onclick="window.practiceEngine.renderCurriculumBrowser()" class="text-slate-500 hover:text-navy-dark font-extrabold text-sm flex items-center gap-1">
            ← Back to Lessons
          </button>
          <div class="flex items-center space-x-3">
            <span id="practice-streak-badge" class="streak-badge">
              <span>🔥</span>
              <span>Streak: ${this.streak}</span>
            </span>
            <button onclick="window.scratchpad.open()" class="px-3.5 py-1.5 rounded-full bg-teal-50 text-teal-700 border border-teal-200 text-xs font-extrabold hover:bg-teal-100 transition-colors">
              📝 Scratchpad
            </button>
          </div>
        </div>

        <!-- Question Card -->
        <div class="bg-white p-8 md:p-10 rounded-card card-shadow border border-slate-100 space-y-6">
          <!-- Progress header -->
          <div class="space-y-2">
            <div class="flex items-center justify-between text-xs font-bold text-slate-400">
              <span>Question ${this.currentQuestionIdx + 1} of ${totalQ}</span>
              <span class="text-amber-500 font-extrabold">Star Potential: ${starPreview}</span>
            </div>
            <div class="w-full bg-slate-100 h-2.5 rounded-full overflow-hidden">
              <div class="bg-sky-500 h-full transition-all duration-300" style="width: ${progressPercent}%"></div>
            </div>
          </div>

          <!-- Prompt -->
          <div class="space-y-3">
            <div class="flex items-center space-x-2">
              <span class="px-3 py-1 bg-sky-50 text-sky-700 rounded-full font-bold text-xs">${this.activeLesson.domain}</span>
              <span class="text-xs font-bold text-slate-400">${this.activeLesson.standard}</span>
            </div>
            <h3 class="text-2xl font-black text-navy-dark leading-relaxed">${q.prompt}</h3>
          </div>

          <!-- Interactive Manipulatives Widget -->
          <div id="interactive-manipulative-slot"></div>

          <!-- Inputs -->
          <div id="practice-inputs-slot" class="pt-2"></div>

          <!-- 3-Step Tiered Hint Drawer -->
          <div class="pt-4 border-t border-slate-100 space-y-3">
            <div class="flex items-center justify-between">
              <button onclick="window.practiceEngine.revealHint()" class="px-4 py-2 rounded-xl bg-amber-50 text-amber-800 border border-amber-200 hover:bg-amber-100 text-xs font-extrabold flex items-center gap-1.5 transition-all">
                💡 Need a Hint? (${currentHintsRevealed}/3 Steps)
              </button>
              <span class="text-xs text-slate-400">Using hints provides guidance while preserving practice!</span>
            </div>

            <div id="hint-drawer-content" class="space-y-2"></div>
          </div>

          <!-- Bottom Action Buttons -->
          <div class="pt-6 border-t border-slate-100 flex items-center justify-between">
            <button onclick="window.practiceEngine.prevQuestion()" ${this.currentQuestionIdx === 0 ? 'disabled class="opacity-40 cursor-not-allowed px-5 py-2.5 rounded-xl border border-slate-200 font-bold text-slate-400"' : 'class="px-5 py-2.5 rounded-xl border border-slate-200 font-bold text-slate-600 hover:bg-slate-50"'}>
              Previous
            </button>
            <button onclick="window.practiceEngine.checkAnswer()" class="px-8 py-3 rounded-xl btn-blue-gradient text-base font-bold shadow-md">
              Check Answer ✓
            </button>
          </div>
        </div>
      </div>
    `;

    this.renderInputs(q);
    this.renderHints(q, currentHintsRevealed);
    this.renderManipulativeIfApplicable(q);
  }

  renderInputs(q) {
    const slot = document.getElementById('practice-inputs-slot');
    if (!slot) return;

    if (q.type === 'multiple-choice' && q.options) {
      let optionsHtml = '<div class="space-y-3">';
      q.options.forEach((opt, idx) => {
        const isSelected = this.userAnswers[this.currentQuestionIdx] === idx;
        optionsHtml += `
          <button onclick="window.practiceEngine.selectOption(${idx})"
                  class="w-full text-left p-4 rounded-xl border-2 transition-all flex items-center justify-between ${isSelected ? 'border-sky-500 bg-sky-50' : 'border-slate-100 hover:bg-slate-50'}">
            <span class="font-bold text-slate-700">${opt.text}</span>
            <span class="w-5 h-5 rounded-full border-2 flex items-center justify-center ${isSelected ? 'border-sky-500 bg-sky-500 text-white' : 'border-slate-300'}">
              ${isSelected ? '✓' : ''}
            </span>
          </button>
        `;
      });
      optionsHtml += '</div>';
      slot.innerHTML = optionsHtml;
    } else {
      const currentVal = this.userAnswers[this.currentQuestionIdx] || '';
      slot.innerHTML = `
        <div class="space-y-3">
          <input type="text" id="practice-numeric-input"
                 value="${currentVal}"
                 oninput="window.practiceEngine.saveNumeric(this.value)"
                 placeholder="Enter your math answer..."
                 class="w-full p-4 rounded-xl border-2 border-slate-200 focus:border-sky-500 focus:outline-none text-xl font-black text-navy-dark">
          <div id="math-keypad-container"></div>
        </div>
      `;
      Manipulatives.renderTouchKeypad('practice-numeric-input', 'math-keypad-container');
    }
  }

  renderManipulativeIfApplicable(q) {
    const slot = document.getElementById('interactive-manipulative-slot');
    if (!slot) return;

    const domainLower = (q.domain || '').toLowerCase();
    const promptLower = (q.prompt || '').toLowerCase();

    if (domainLower.includes('fraction') || promptLower.includes('fraction')) {
      slot.innerHTML = '<div id="fraction-manipulative-container"></div>';
      Manipulatives.renderFractionBar('fraction-manipulative-container', 4);
    } else if (domainLower.includes('area') || promptLower.includes('area') || promptLower.includes('perimeter')) {
      slot.innerHTML = '<div id="area-manipulative-container"></div>';
      Manipulatives.renderAreaGrid('area-manipulative-container', 5, 6);
    } else if (promptLower.includes('number line') || promptLower.includes('jumps')) {
      slot.innerHTML = '<div id="nl-manipulative-container"></div>';
      Manipulatives.renderNumberLine('nl-manipulative-container', 0, 12, 3);
    }
  }

  renderHints(q, revealedCount) {
    const container = document.getElementById('hint-drawer-content');
    if (!container || !q.hints) return;

    let html = '';
    for (let i = 0; i < revealedCount && i < q.hints.length; i++) {
      const colors = ['border-sky-500 bg-sky-50', 'border-amber-500 bg-amber-50', 'border-purple-500 bg-purple-50'];
      html += `
        <div class="hint-step-card p-3 rounded-xl border-l-4 ${colors[i]} shadow-sm text-xs font-bold text-slate-700">
          ${q.hints[i]}
        </div>
      `;
    }
    container.innerHTML = html;
  }

  revealHint() {
    const cur = this.hintsUsed[this.currentQuestionIdx] || 0;
    if (cur < 3) {
      this.hintsUsed[this.currentQuestionIdx] = cur + 1;
      this.sound.playHint();
      this.renderQuestionView();
    }
  }

  selectOption(idx) {
    this.userAnswers[this.currentQuestionIdx] = idx;
    this.sound.playPop();
    this.renderInputs(this.activeQuestions[this.currentQuestionIdx]);
  }

  saveNumeric(val) {
    this.userAnswers[this.currentQuestionIdx] = val;
  }

  prevQuestion() {
    if (this.currentQuestionIdx > 0) {
      this.currentQuestionIdx--;
      this.renderQuestionView();
    }
  }

  checkAnswer() {
    const q = this.activeQuestions[this.currentQuestionIdx];
    const userAns = this.userAnswers[this.currentQuestionIdx];
    const hintsCount = this.hintsUsed[this.currentQuestionIdx] || 0;

    let isCorrect = false;
    if (q.type === 'multiple-choice') {
      if (userAns !== undefined && q.options && q.options[userAns]?.correct) {
        isCorrect = true;
      }
    } else {
      const cleanUser = String(userAns || '').trim().replace(/,/g, '');
      const cleanCorrect = String(q.correctAnswer || '').trim().replace(/,/g, '');
      isCorrect = cleanUser === cleanCorrect || (q.acceptedAnswers && q.acceptedAnswers.includes(cleanUser));
    }

    if (isCorrect) {
      this.sound.playCorrect();
      this.streak++;
      if (this.streak > this.maxStreak) this.maxStreak = this.streak;

      // Calculate stars for this question
      let stars = 3;
      if (hintsCount === 1) stars = 2;
      else if (hintsCount >= 2) stars = 1;
      this.questionStars[this.currentQuestionIdx] = stars;

      // Celebrate streak milestones
      if (this.streak >= 3) {
        this.sound.playStreak();
        if (typeof confetti === 'function') {
          confetti({ particleCount: 40, spread: 50, origin: { y: 0.6 } });
        }
      }

      // Move to next question or complete lesson
      if (this.currentQuestionIdx + 1 < this.activeQuestions.length) {
        this.currentQuestionIdx++;
        this.renderQuestionView();
      } else {
        this.finishLesson();
      }
    } else {
      this.sound.playTryAgain();
      this.streak = 0;
      alert(`Not quite! Review your work or click "Need a Hint?" 💡 to guide you through.`);
      this.renderQuestionView();
    }
  }

  finishLesson() {
    this.sound.playFanfare();
    if (typeof confetti === 'function') {
      confetti({ particleCount: 120, spread: 80, origin: { y: 0.5 } });
    }

    const totalQ = this.activeQuestions.length;
    let totalStars = 0;
    Object.values(this.questionStars).forEach(s => totalStars += s);
    const scorePercent = 100; // All solved correctly to finish
    const earnedStars = Math.max(1, Math.round(totalStars / totalQ));

    // Save progress to local state
    const updatedProgress = StorageManager.recordLessonCompletion(
      this.activeGrade,
      this.activeLesson.lessonNumber,
      scorePercent,
      earnedStars
    );

    // Persist to WordPress REST API!
    ApiClient.saveStudentProgress(updatedProgress);

    const container = document.getElementById('practice-main-view');
    container.innerHTML = `
      <div class="max-w-xl mx-auto bg-white p-10 rounded-card card-shadow border border-slate-100 text-center space-y-6">
        <span class="text-6xl block">🎉</span>
        <h3 class="text-3xl font-black text-navy-dark">Lesson Mastered!</h3>
        <p class="text-slate-500 font-semibold">You've successfully completed ${this.activeLesson.title}.</p>

        <div class="p-6 bg-amber-50 rounded-2xl border border-amber-200 space-y-2">
          <span class="text-xs uppercase tracking-widest font-black text-amber-700">Stars Earned</span>
          <div class="text-4xl">
            ${'⭐'.repeat(earnedStars)}${'☆'.repeat(3 - earnedStars)}
          </div>
          <span class="text-xs text-amber-600 font-bold block">🔥 Best Streak: ${this.maxStreak} in a row</span>
        </div>

        <div class="p-4 bg-emerald-50 rounded-xl border border-emerald-200 text-emerald-800 text-sm font-bold">
          🔓 Next consecutive lesson has been unlocked!
        </div>

        <button onclick="window.practiceEngine.renderCurriculumBrowser()" class="w-full py-4 rounded-xl btn-blue-gradient text-base font-extrabold shadow-md">
          Continue to Next Quest →
        </button>
      </div>
    `;
  }
}

// Global initialization
if (typeof window !== 'undefined') {
  window.practiceEngine = new PracticeEngine();
  window.addEventListener('DOMContentLoaded', () => {
    window.practiceEngine.init();
  });
}
