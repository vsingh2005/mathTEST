/**
 * Kids STEM Studio - REST API Client & Offline Sync Service
 * 
 * Synchronizes student assessment attempts, completed worksheets,
 * lesson index progress, and stars with WordPress backend.
 */

import { StorageManager } from './storage.js';

export class ApiClient {
  static BASE_URL = '/wp-json/kss-math/v1';

  /**
   * Helper for authenticated/nonce REST requests
   */
  static async request(endpoint, options = {}) {
    const session = StorageManager.getItem(StorageManager.KEYS.SESSION);
    const token = session ? session.token : null;

    const headers = {
      'Content-Type': 'application/json',
      ...(options.headers || {})
    };

    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }

    try {
      const response = await fetch(`${this.BASE_URL}${endpoint}`, {
        ...options,
        headers
      });

      if (!response.ok) {
        throw new Error(`HTTP Error ${response.status}: ${response.statusText}`);
      }

      return await response.json();
    } catch (error) {
      console.warn(`[ApiClient] Request failed for ${endpoint}:`, error);
      throw error;
    }
  }

  /**
   * Fetch portal settings
   */
  static async getSettings() {
    try {
      return await this.request('/settings');
    } catch (e) {
      return null;
    }
  }

  /**
   * Fetch question bank from WordPress backend
   */
  static async getQuestions() {
    try {
      return await this.request('/questions');
    } catch (e) {
      return null;
    }
  }

  /**
   * Save assessment attempt (persists score, grade, answers, and streak)
   */
  static async saveAttempt(attemptData) {
    const session = StorageManager.getItem(StorageManager.KEYS.SESSION);
    const payload = {
      ...attemptData,
      user_id: session?.user?.id || 0,
      user_name: session?.user?.display_name || 'Guest Student',
      timestamp: new Date().toISOString()
    };

    try {
      const res = await this.request('/save-attempt', {
        method: 'POST',
        body: JSON.stringify(payload)
      });
      return res;
    } catch (error) {
      // Offline fallback: Queue for subsequent sync
      StorageManager.queueOfflineSync('save-attempt', payload);
      return { success: false, queued: true };
    }
  }

  /**
   * Persist student lesson index progress to REST API
   * (Direct requirement: Saves unlockedLessonIndex, stars, and completedLessons)
   */
  static async saveStudentProgress(progressData) {
    const session = StorageManager.getItem(StorageManager.KEYS.SESSION);
    const payload = {
      user_id: session?.user?.id || 0,
      user_name: session?.user?.display_name || 'Guest Student',
      progress: progressData,
      updated_at: new Date().toISOString()
    };

    try {
      const res = await this.request('/student-progress', {
        method: 'POST',
        body: JSON.stringify(payload)
      });
      return res;
    } catch (error) {
      // Offline fallback: Queue sync
      StorageManager.queueOfflineSync('student-progress', payload);
      return { success: false, queued: true };
    }
  }

  /**
   * Fetch persisted student progress across devices
   */
  static async getStudentProgress(userId = null) {
    const session = StorageManager.getItem(StorageManager.KEYS.SESSION);
    const id = userId || session?.user?.id;
    if (!id) return null;

    try {
      return await this.request(`/student-progress?user_id=${id}`);
    } catch (e) {
      return null;
    }
  }

  /**
   * Process offline queue when network is restored
   */
  static async processOfflineQueue() {
    if (!navigator.onLine) return;
    const pending = StorageManager.getPendingSyncs();
    if (!pending || pending.length === 0) return;

    console.log(`[ApiClient] Draining offline sync queue (${pending.length} items)...`);

    for (const item of pending) {
      try {
        if (item.action === 'save-attempt') {
          await this.request('/save-attempt', {
            method: 'POST',
            body: JSON.stringify(item.payload)
          });
        } else if (item.action === 'student-progress') {
          await this.request('/student-progress', {
            method: 'POST',
            body: JSON.stringify(item.payload)
          });
        }
        StorageManager.removePendingSync(item.id);
      } catch (err) {
        console.warn(`[ApiClient] Failed syncing queue item ${item.id}, will retry later.`);
        break; // Stop draining if network failed again
      }
    }
  }
}

// Global setup and offline listener
if (typeof window !== 'undefined') {
  window.ApiClient = ApiClient;
  window.addEventListener('online', () => {
    ApiClient.processOfflineQueue();
  });
  // Drain on page load if online
  setTimeout(() => ApiClient.processOfflineQueue(), 2000);
}
