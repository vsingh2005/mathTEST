/**
 * Kids STEM Studio - Modular Results Controller
 */

import { AuthManager } from '../../shared/js/auth.js';
import { StorageManager } from '../../shared/js/storage.js';
import { SoundEffectManager } from '../../shared/js/sound.js';
import '../../shared/js/components.js';

class ResultsController {
  constructor() {
    this.sound = window.soundManager || new SoundEffectManager();
    this.results = null;
    this.filter = 'all';
  }

  init() {
    AuthManager.requireAuth('../login/index.html');
    AuthManager.updateHeaderUI();

    const raw = sessionStorage.getItem('kss_last_results');
    if (raw) {
      this.results = JSON.parse(raw);
    } else {
      const attempts = StorageManager.getItem('kss_local_attempts', []);
      this.results = attempts.length > 0 ? attempts[attempts.length - 1] : null;
    }

    this.renderResults();
    this.playCelebration();
  }

  playCelebration() {
    this.sound.playFanfare();
    if (typeof confetti === 'function') {
      confetti({ particleCount: 150, spread: 90, origin: { y: 0.4 } });
      setTimeout(() => {
        confetti({ particleCount: 80, spread: 60, origin: { y: 0.6 } });
      }, 500);
    }
  }

  renderResults() {
    if (!this.results) {
      document.getElementById('results-content').innerHTML = `
        <div class="text-center py-16 space-y-4">
          <h3 class="text-2xl font-black text-navy-dark">No Recent Assessment Found</h3>
          <p class="text-slate-500 text-sm">Please take a placement test from your dashboard to view results.</p>
          <button onclick="window.location.href='../portal/index.html'" class="px-6 py-3 rounded-xl btn-blue-gradient font-bold text-sm">
            Go to Dashboard
          </button>
        </div>
      `;
      return;
    }

    const { score, recommendedGrade, timeElapsedSeconds, maxStreak, questionsServed, userAnswers } = this.results;
    const mins = Math.floor((timeElapsedSeconds || 0) / 60);
    const secs = (timeElapsedSeconds || 0) % 60;

    document.getElementById('placement-recommendation').innerText = recommendedGrade || 'Standard Level';
    document.getElementById('score-details').innerText = `You scored ${score || '10/15'} correct questions.`;
    document.getElementById('time-details').innerText = `Completed in ${mins}m ${secs}s • Highest Streak: ${maxStreak || 0} in a row`;

    this.renderBreakdown();
  }

  setFilter(filter) {
    this.filter = filter;
    ['filter-btn-all', 'filter-btn-incorrect', 'filter-btn-correct'].forEach(id => {
      const b = document.getElementById(id);
      if (b) b.className = 'px-4 py-2 text-xs font-extrabold rounded-lg text-slate-600 hover:bg-white/50 transition-colors';
    });

    const activeBtn = document.getElementById(`filter-btn-${filter}`);
    if (activeBtn) {
      activeBtn.className = 'px-4 py-2 text-xs font-extrabold rounded-lg bg-white text-navy-dark shadow-sm';
    }

    this.renderBreakdown();
  }

  renderBreakdown() {
    const container = document.getElementById('fluid-question-breakdown');
    if (!container || !this.results) return;

    const questions = this.results.questionsServed || [];
    const userAnswers = this.results.userAnswers || {};

    let html = '';
    questions.forEach((q, idx) => {
      const userAns = userAnswers[idx];
      let isCorrect = false;
      let userAnsText = 'Not answered';

      if (q.type === 'multiple-choice' && q.options) {
        if (userAns !== undefined && q.options[userAns]) {
          userAnsText = q.options[userAns].text;
          isCorrect = !!q.options[userAns].correct;
        }
      } else {
        userAnsText = userAns || 'No answer entered';
        const cleanUser = String(userAns || '').trim().replace(/,/g, '');
        const cleanCorrect = String(q.correctAnswer || '').trim().replace(/,/g, '');
        isCorrect = cleanUser === cleanCorrect || (q.acceptedAnswers && q.acceptedAnswers.includes(cleanUser));
      }

      if (this.filter === 'correct' && !isCorrect) return;
      if (this.filter === 'incorrect' && isCorrect) return;

      const borderColor = isCorrect ? 'border-emerald-200 bg-emerald-50/30' : 'border-rose-200 bg-rose-50/30';
      const badgeClass = isCorrect ? 'bg-emerald-100 text-emerald-800' : 'bg-rose-100 text-rose-800';

      html += `
        <div class="review-item p-6 rounded-2xl border ${borderColor} space-y-4">
          <div class="flex items-center justify-between">
            <span class="text-xs font-black text-slate-400 uppercase">Question ${idx + 1} • ${q.domain || 'Math Core'}</span>
            <span class="px-3 py-1 rounded-full text-xs font-black ${badgeClass}">
              ${isCorrect ? 'Correct' : 'Needs Review'}
            </span>
          </div>

          <p class="font-extrabold text-navy-dark text-base">${q.prompt || q.text}</p>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs pt-1">
            <div class="p-3 bg-white rounded-xl border border-slate-200">
              <span class="text-slate-400 font-bold block">Your Answer:</span>
              <span class="font-black ${isCorrect ? 'text-emerald-700' : 'text-rose-600'} text-sm">${userAnsText}</span>
            </div>
            <div class="p-3 bg-white rounded-xl border border-slate-200">
              <span class="text-slate-400 font-bold block">Correct Solution:</span>
              <span class="font-black text-emerald-700 text-sm">${q.correctAnswer || (q.options?.find(o => o.correct)?.text) || 'See explanation'}</span>
            </div>
          </div>

          <div class="p-3 bg-slate-50 rounded-xl border border-slate-100 text-xs text-slate-600 leading-relaxed">
            <strong class="text-navy-dark">Step-by-Step Explanation:</strong> ${q.explanation || 'Review fundamental rules for this math standard.'}
          </div>
        </div>
      `;
    });

    if (!html) {
      html = `<div class="text-center py-8 text-slate-400 font-bold text-sm">No questions in this filter.</div>`;
    }

    container.innerHTML = html;
  }
}

window.resultsController = new ResultsController();
window.addEventListener('DOMContentLoaded', () => {
  window.resultsController.init();
});
