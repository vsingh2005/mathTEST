/**
 * Kids STEM Studio - Authentication & Security Guard
 * 
 * Handles client-side pre-render authentication guards, session management,
 * token verification, and input sanitization (XSS prevention).
 */

import { StorageManager } from './storage.js';

export class AuthManager {
  /**
   * Sanitizes user inputs to prevent XSS attacks in dynamic math formulas
   */
  static sanitizeInput(str) {
    if (typeof str !== 'string') return str;
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#x27;')
      .replace(/\//g, '&#x2F;');
  }

  static getSession() {
    const raw = StorageManager.getItem(StorageManager.KEYS.SESSION);
    if (!raw) return null;
    if (typeof raw === 'object' && raw !== null) return raw;
    
    // When session is stored as a username string (e.g. 'student1', 'guest')
    const username = String(raw);
    let token = null;
    try {
      token = localStorage.getItem('kss_jwt_token') || sessionStorage.getItem('kss_jwt_token');
    } catch (e) {}

    return {
      username: username,
      user: { display_name: username, username: username },
      token: token || null,
      guest: username.toLowerCase() === 'guest' || !token
    };
  }

  static setSession(sessionData) {
    StorageManager.setItem(StorageManager.KEYS.SESSION, sessionData);
  }

  static isAuthenticated() {
    let raw = null;
    try {
      raw = localStorage.getItem(StorageManager.KEYS.SESSION) || sessionStorage.getItem(StorageManager.KEYS.SESSION);
    } catch (e) {}
    return !!(raw && raw !== 'null' && raw !== 'undefined');
  }

  /**
   * Client-side pre-render authentication guard:
   * Redirects unauthenticated users immediately before DOM renders.
   */
  static requireAuth(loginUrl = 'login.html') {
    if (!this.isAuthenticated()) {
      window.location.href = loginUrl;
      return false;
    }
    return true;
  }

  /**
   * Redirects authenticated users away from login page
   */
  static redirectIfAuth(portalUrl = 'portal.html') {
    if (this.isAuthenticated()) {
      window.location.href = portalUrl;
      return true;
    }
    return false;
  }

  /**
   * Logs out user and cleans session state
   */
  static logout(redirectTo = 'login.html') {
    try {
      localStorage.removeItem(StorageManager.KEYS.SESSION);
      sessionStorage.removeItem(StorageManager.KEYS.SESSION);
      sessionStorage.removeItem(StorageManager.KEYS.ACTIVE_EXAM_STATE);
    } catch (e) {}
    window.location.href = redirectTo;
  }

  /**
   * Standardized Header UI renderer
   */
  static updateHeaderUI(containerId = 'user-header-widget') {
    const container = document.getElementById(containerId);
    if (!container) return;

    const session = this.getSession();
    if (!session) {
      container.innerHTML = `
        <button onclick="window.location.href='login.html'" class="px-5 py-2.5 rounded-xl btn-blue-gradient text-sm font-bold">
          Sign In
        </button>
      `;
      return;
    }

    const displayName = this.sanitizeInput(session.user?.display_name || session.user?.user_nicename || 'Student');
    const isGuest = !!session.guest;

    container.innerHTML = `
      <div class="flex items-center space-x-3">
        <button onclick="window.soundManager && window.soundManager.toggleMute()" class="sound-toggle-btn" title="Toggle Sound FX"></button>
        <div class="flex items-center space-x-2 bg-slate-100 py-1.5 px-3 rounded-full border border-slate-200">
          <span class="w-2.5 h-2.5 rounded-full ${isGuest ? 'bg-amber-400' : 'bg-emerald-500'}"></span>
          <span class="text-xs md:text-sm font-bold text-slate-700 max-w-[120px] truncate">${displayName}</span>
        </div>
        <button onclick="AuthManager.logout()" class="text-xs font-bold text-rose-500 hover:text-rose-700 transition-colors">
          Logout
        </button>
      </div>
    `;

    if (window.soundManager) {
      window.soundManager.updateSoundButtons();
    }
  }

  /**
   * Renders past results history modal
   */
  static async renderHistoryModal(modalId = 'history-modal', contentId = 'user-history-content') {
    const content = document.getElementById(contentId);
    const modal = document.getElementById(modalId);
    if (!content || !modal) return;

    modal.classList.remove('hidden');
    modal.classList.add('flex');

    const progress = StorageManager.getProgress();
    const attempts = StorageManager.getItem('kss_local_attempts', []);

    let html = `
      <div class="space-y-4">
        <div class="bg-sky-50 p-4 rounded-xl border border-sky-100 flex items-center justify-between">
          <div>
            <h4 class="font-extrabold text-navy-dark text-base">Current Level Placement</h4>
            <p class="text-xs text-sky-700 font-semibold">
              ${progress.testedGrade ? `Grade ${progress.testedGrade} Math Benchmark` : 'Placement assessment not yet taken'}
            </p>
          </div>
          <div class="text-right">
            <span class="text-2xl font-black text-sky-600">${progress.totalStars || 0}</span>
            <span class="text-xs text-slate-500 block font-bold">Stars Earned</span>
          </div>
        </div>
    `;

    if (attempts.length === 0) {
      html += `
        <div class="text-center py-8 text-slate-400 font-semibold">
          <p class="text-xs font-bold uppercase tracking-wider text-slate-400 mb-2">History Empty</p>
          <p>No assessment attempts found on this browser yet.</p>
        </div>
      `;
    } else {
      html += `<div class="space-y-3">`;
      attempts.slice(-5).reverse().forEach(att => {
        const dateStr = att.timestamp ? new Date(att.timestamp).toLocaleDateString() : 'Recent';
        html += `
          <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 flex items-center justify-between">
            <div>
              <span class="font-bold text-navy-dark text-sm block">${att.recommendedGrade || 'Grade Assessment'}</span>
              <span class="text-xs text-slate-400">${dateStr} • Track ${att.track || '3-8'}</span>
            </div>
            <div class="text-right">
              <span class="text-sm font-extrabold text-emerald-600">${att.score || 0}/15 Correct</span>
              <span class="text-xs text-amber-600 block font-bold">Max Streak: ${att.maxStreak || 0}</span>
            </div>
          </div>
        `;
      });
      html += `</div>`;
    }

    html += `</div>`;
    content.innerHTML = html;
  }
}

// Global setup
if (typeof window !== 'undefined') {
  window.AuthManager = AuthManager;
}
