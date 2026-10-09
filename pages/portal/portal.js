/**
 * Kids STEM Studio - Modular Portal Controller
 */

import { AuthManager } from '../../shared/js/auth.js';
import { StorageManager } from '../../shared/js/storage.js';
import '../../shared/js/components.js';

class PortalController {
  static init() {
    AuthManager.requireAuth('../login/index.html');
    AuthManager.updateHeaderUI();
    this.renderRecommendedPracticeWidget();
  }

  static showTrackSelection() {
    document.getElementById('landing-main-content')?.classList.add('hidden');
    document.getElementById('track-selection-panel')?.classList.remove('hidden');
  }

  static showLandingMain() {
    document.getElementById('track-selection-panel')?.classList.add('hidden');
    document.getElementById('landing-main-content')?.classList.remove('hidden');
  }

  static selectTrack(track) {
    sessionStorage.setItem('selectedTrack', track);
    window.location.href = '../exam/index.html';
  }

  /**
   * Renders real-time student placement status & recommended practice jump-in
   */
  static renderRecommendedPracticeWidget() {
    const container = document.getElementById('recommended-practice-container');
    if (!container) return;

    const progress = StorageManager.getProgress();
    const placedGrade = progress.testedGrade;
    const totalStars = progress.totalStars || 0;
    const completedCount = Object.keys(progress.completedLessons || {}).length;

    if (!placedGrade) {
      container.innerHTML = `
        <div class="recommended-practice-banner flex flex-col md:flex-row items-center justify-between gap-6">
          <div class="space-y-2">
            <span class="px-3 py-1 bg-amber-100 text-amber-800 rounded-full font-extrabold text-xs uppercase">Step 1: Calibrate Level</span>
            <h3 class="text-2xl font-black text-navy-dark">Take Placement Assessment First</h3>
            <p class="text-slate-600 text-sm max-w-xl font-medium">
              Start your adaptive diagnostic placement test below to identify your math level and unlock your personalized worksheet quests!
            </p>
          </div>
          <button onclick="PortalController.showTrackSelection()" class="px-6 py-3.5 rounded-xl btn-blue-gradient text-sm font-extrabold whitespace-nowrap shadow-md">
            Begin Assessment 🚀
          </button>
        </div>
      `;
    } else {
      const highestUnlocked = progress.unlockedLessonIndex[String(placedGrade)] || 1;
      container.innerHTML = `
        <div class="recommended-practice-banner flex flex-col md:flex-row items-center justify-between gap-6">
          <div class="space-y-3">
            <div class="flex items-center space-x-2">
              <span class="px-3 py-1 bg-emerald-100 text-emerald-800 rounded-full font-extrabold text-xs uppercase">🎯 Recommended Practice</span>
              <span class="text-xs text-slate-500 font-bold">• Placed in Grade ${placedGrade}</span>
            </div>
            <h3 class="text-2xl font-black text-navy-dark">Grade ${placedGrade} Worksheet Path: Lesson ${highestUnlocked}</h3>
            <p class="text-slate-600 text-sm max-w-xl font-medium">
              You have completed <strong>${completedCount}</strong> worksheets and earned <strong>${totalStars}</strong> stars! Continue your consecutive practice quest to unlock subsequent standards.
            </p>
            <div class="w-full bg-slate-200 h-2.5 rounded-full overflow-hidden max-w-md">
              <div class="bg-emerald-500 h-full" style="width: ${Math.min(100, (highestUnlocked / 25) * 100)}%"></div>
            </div>
          </div>
          <div class="flex flex-col sm:flex-row items-center gap-3">
            <button onclick="window.location.href='../practice/index.html'" class="px-8 py-4 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-extrabold text-sm whitespace-nowrap shadow-md transition-all">
              Jump into Worksheets 🚀
            </button>
            <button onclick="PortalController.showTrackSelection()" class="px-5 py-4 rounded-xl border border-slate-300 text-slate-700 hover:bg-slate-100 font-extrabold text-sm whitespace-nowrap transition-colors">
              Retake Placement
            </button>
          </div>
        </div>
      `;
    }
  }
}

window.PortalController = PortalController;
window.addEventListener('DOMContentLoaded', () => {
  PortalController.init();
});
