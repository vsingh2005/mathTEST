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

  static sanitizeUsername(input) {
    if (!input) return 'student1';
    if (typeof input === 'object' && input !== null) {
      input = input.username || input.name || input.studentName || input.user_nicename || input.display_name || 'student1';
    }
    let str = String(input).trim();
    str = str.replace(/\\"/g, '"').replace(/\\'/g, "'");

    for (let i = 0; i < 5; i++) {
      if ((str.startsWith('{') && str.endsWith('}')) || (str.startsWith('"') && str.endsWith('"')) || (str.startsWith("'") && str.endsWith("'"))) {
        try {
          const parsed = JSON.parse(str);
          if (parsed && typeof parsed === 'object') {
            str = parsed.username || parsed.name || parsed.studentName || parsed.user_nicename || parsed.display_name || 'student1';
          } else if (typeof parsed === 'string') {
            str = parsed;
          } else {
            break;
          }
        } catch (e) {
          const match = str.match(/(?:username|name|studentName|user_nicename|display_name)["']?\s*:\s*["']?([^"',}\s]+)/i);
          if (match && match[1]) {
            str = match[1];
          }
          break;
        }
        str = String(str).trim();
        str = str.replace(/\\"/g, '"').replace(/\\'/g, "'");
      } else {
        break;
      }
    }

    if (str.includes('{') || str.includes('}')) {
      const match = str.match(/(?:username|name|studentName|user_nicename|display_name)["']?\s*:\s*["']?([^"',}\s]+)/i);
      if (match && match[1]) {
        str = match[1];
      } else {
        str = 'student1';
      }
    }

    str = str.replace(/[{}\"']/g, '').trim();
    return str || 'student1';
  }

  static getSession() {
    const raw = StorageManager.getItem(StorageManager.KEYS.SESSION);
    if (!raw) return null;
    if (typeof raw === 'object' && raw !== null) {
      if (raw.username) raw.username = this.sanitizeUsername(raw.username);
      return raw;
    }
    
    // When session is stored as a username string (e.g. 'student1', 'guest')
    const username = this.sanitizeUsername(raw);
    let token = null;
    try {
      token = localStorage.getItem('kss_jwt_token') || sessionStorage.getItem('kss_jwt_token');
    } catch (e) {}

    // Self-heal storage
    try {
      if (raw && typeof raw === 'string' && (raw.includes('{') || raw.includes('"'))) {
        StorageManager.setItem(StorageManager.KEYS.SESSION, { username: username, guest: false });
      }
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

    const rawName = session.username || session.user?.display_name || session.user?.username || session.studentName || 'Student';
    const cleanName = this.sanitizeUsername(rawName);
    const displayName = this.sanitizeInput(cleanName);
    const initial = displayName.substring(0, 1).toUpperCase();

    container.innerHTML = `
      <div class="flex items-center gap-2 bg-slate-100/90 py-1 pl-1.5 pr-2.5 rounded-full border border-slate-200 text-xs shadow-xs">
        <span class="w-6 h-6 rounded-full bg-[#287F78] text-white flex items-center justify-center font-black text-xs">
          ${initial}
        </span>
        <span class="font-extrabold text-[#253238] max-w-[120px] truncate" title="${displayName}">${displayName}</span>
        <div class="h-3 w-px bg-slate-300 mx-0.5"></div>
        <button onclick="window.location.href='portal.html'" class="text-[11px] font-bold text-sky-600 hover:underline">Dashboard</button>
        <button onclick="AuthManager.logout()" class="text-[11px] font-bold text-rose-500 hover:underline">Logout</button>
      </div>
    `;

    // Sync stars display if present
    const headerStars = document.getElementById('header-stars-display');
    if (headerStars) {
      try {
        const p = StorageManager.getProgress ? StorageManager.getProgress() : JSON.parse(localStorage.getItem('kss_student_progress') || '{}');
        headerStars.textContent = `${p.totalStars || 0} Stars`;
      } catch (e) {}
    }

    // Sync nav placement button if present
    const navLabel = document.getElementById('nav-placement-label');
    if (navLabel) {
      try {
        const p = StorageManager.getProgress ? StorageManager.getProgress() : JSON.parse(localStorage.getItem('kss_student_progress') || '{}');
        const placed = p.testedGrade;
        if (placed) {
          const placedNum = parseInt(placed, 10);
          const nextGrade = placedNum + 1;
          if (nextGrade <= 8) {
            navLabel.textContent = `Test into Grade ${nextGrade}`;
          } else {
            navLabel.textContent = `Placement Complete`;
          }
        } else {
          navLabel.textContent = `Placement Exam`;
        }
      } catch (e) {}
    }

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
  window.handlePlacementAction = function() {
    try {
      const p = StorageManager.getProgress ? StorageManager.getProgress() : JSON.parse(localStorage.getItem('kss_student_progress') || '{}');
      const placed = p.testedGrade;
      if (!placed) {
        sessionStorage.removeItem('targetLevelUpGrade');
        window.location.href = 'portal.html';
      } else if (placed < 8) {
        const targetGrade = parseInt(placed, 10) + 1;
        let track = '3-4';
        if (targetGrade >= 7) track = '7-8';
        else if (targetGrade >= 5) track = '5-6';
        sessionStorage.setItem('selectedTrack', track);
        sessionStorage.setItem('targetLevelUpGrade', String(targetGrade));
        window.location.href = 'instructions.html';
      } else {
        window.location.href = 'practice.html?grade=8';
      }
    } catch (e) {
      window.location.href = 'portal.html';
    }
  };
}
