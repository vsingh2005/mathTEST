/**
 * Kids STEM Studio - Modular Exam Controller
 * 
 * Diagnostic Placement Assessment Engine:
 * - Strictly NO HINTS during official placement exam
 * - In-progress test crash recovery & auto-save via StorageManager
 * - Sound feedback & streak flame counter
 * - Initializes student unlocked lesson threshold upon completion
 * - REST API sync
 */

import { StorageManager } from '../../shared/js/storage.js';
import { ApiClient } from '../../shared/js/api.js';
import { AuthManager } from '../../shared/js/auth.js';
import { SoundEffectManager } from '../../shared/js/sound.js';
import '../../shared/js/components.js';

class ExamEngine {
  constructor() {
    this.sound = window.soundManager || new SoundEffectManager();
    this.questions = [];
    this.state = {
      selectedTrack: '7-8',
      activeDifficulty: 7,
      currentQuestionIndex: 0,
      userAnswers: {},
      questionsServed: [],
      secondsElapsed: 0,
      streak: 0,
      maxStreak: 0,
      timerInterval: null
    };
  }

  async init() {
    AuthManager.requireAuth('../login/index.html');
    AuthManager.updateHeaderUI();

    const track = sessionStorage.getItem('selectedTrack') || '7-8';
    this.state.selectedTrack = track;

    await this.loadQuestionBank();

    // Check for crash recovery / auto-saved state
    const saved = StorageManager.getExamState();
    if (saved && saved.questionsServed && saved.questionsServed.length > 0 && saved.selectedTrack === track) {
      if (confirm('An in-progress assessment was found. Would you like to resume where you left off?')) {
        this.state = {
          ...this.state,
          ...saved
        };
        this.startTimer();
        this.renderQuestion();
        return;
      } else {
        StorageManager.clearExamState();
      }
    }

    this.startExam();
  }

  async loadQuestionBank() {
    try {
      // Load questions from shared grade files
      const [g3, g4, g5, g6, g7, g8] = await Promise.all([
        fetch('../../shared/data/grade_3.json').then(r => r.json()),
        fetch('../../shared/data/grade_4.json').then(r => r.json()),
        fetch('../../shared/data/grade_5.json').then(r => r.json()),
        fetch('../../shared/data/grade_6.json').then(r => r.json()),
        fetch('../../shared/data/grade_7.json').then(r => r.json()),
        fetch('../../shared/data/grade_8.json').then(r => r.json())
      ]);
      this.questions = [
        ...g3.questions, ...g4.questions, ...g5.questions,
        ...g6.questions, ...g7.questions, ...g8.questions
      ];
    } catch (e) {
      console.warn('Falling back to local questions pool:', e);
      if (window.__fallbackQuestions) {
        this.questions = window.__fallbackQuestions;
      }
    }
  }

  startExam() {
    if (this.state.selectedTrack === '3-4') this.state.activeDifficulty = 3;
    else if (this.state.selectedTrack === '5-6') this.state.activeDifficulty = 5;
    else this.state.activeDifficulty = 7;

    this.state.currentQuestionIndex = 0;
    this.state.userAnswers = {};
    this.state.questionsServed = [];
    this.state.secondsElapsed = 0;
    this.state.streak = 0;
    this.state.maxStreak = 0;

    this.fetchNextQuestion();
    this.startTimer();
    this.renderQuestion();
  }

  startTimer() {
    if (this.state.timerInterval) clearInterval(this.state.timerInterval);
    this.state.timerInterval = setInterval(() => {
      this.state.secondsElapsed++;
      this.updateTimerDisplay();
      if (this.state.secondsElapsed % 5 === 0) {
        StorageManager.saveExamState(this.state);
      }
    }, 1000);
  }

  updateTimerDisplay() {
    const el = document.getElementById('timer-display');
    if (!el) return;
    const mins = String(Math.floor(this.state.secondsElapsed / 60)).padStart(2, '0');
    const secs = String(this.state.secondsElapsed % 60).padStart(2, '0');
    el.innerText = `Time: ${mins}:${secs}`;
  }

  fetchNextQuestion() {
    const servedIds = this.state.questionsServed.map(q => q.id);
    const pool = this.questions.filter(q => q.grade === this.state.activeDifficulty && !servedIds.includes(q.id));

    if (pool.length > 0) {
      const selected = pool[Math.floor(Math.random() * pool.length)];
      this.state.questionsServed.push(selected);
    } else {
      const fallback = this.questions.filter(q => !servedIds.includes(q.id));
      if (fallback.length > 0) {
        this.state.questionsServed.push(fallback[Math.floor(Math.random() * fallback.length)]);
      }
    }
  }

  renderQuestion() {
    const container = document.getElementById('question-container');
    if (!container) return;

    const currentQ = this.state.questionsServed[this.state.currentQuestionIndex];
    if (!currentQ) return;

    const idx = this.state.currentQuestionIndex;
    const total = 15;

    document.getElementById('question-number-display').innerText = `Question ${idx + 1} of ${total}`;
    document.getElementById('progress-bar-fill').style.width = `${((idx + 1) / total) * 100}%`;

    // Update streak badge
    const streakBadge = document.getElementById('exam-streak-badge');
    const streakCount = document.getElementById('exam-streak-count');
    if (streakCount) streakCount.innerText = this.state.streak;
    if (streakBadge) {
      streakBadge.classList.remove('flame-active');
      void streakBadge.offsetWidth; // Trigger reflow
      streakBadge.classList.add('flame-active');
    }

    let html = `
      <div class="mb-6 space-y-2">
        <div class="flex items-center space-x-2">
          <span class="px-3 py-1 text-xs font-bold text-sky-600 bg-sky-50 rounded-full">${currentQ.domain || 'Core Mathematics'}</span>
          <span class="text-xs font-bold text-slate-400">Diagnostic Question</span>
        </div>
        <h2 class="text-xl md:text-2xl font-black text-slate-800 leading-relaxed pt-2">${currentQ.prompt || currentQ.text}</h2>
      </div>
    `;

    if (currentQ.type === 'multiple-choice' && currentQ.options) {
      html += '<div class="space-y-3">';
      currentQ.options.forEach((opt, optIdx) => {
        const isSelected = this.state.userAnswers[idx] === optIdx;
        html += `
          <button onclick="window.examEngine.selectOption(${optIdx})"
                  class="w-full text-left p-4 rounded-xl border-2 transition-all flex items-center justify-between ${isSelected ? 'border-sky-500 bg-sky-50' : 'border-slate-100 hover:bg-slate-50'}">
            <span class="font-bold text-slate-700">${opt.text}</span>
            <span class="w-5 h-5 rounded-full border-2 flex items-center justify-center ${isSelected ? 'border-sky-500 bg-sky-500 text-white' : 'border-slate-300'}">
              ${isSelected ? '<svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"/></svg>' : ''}
            </span>
          </button>
        `;
      });
      html += '</div>';
    } else {
      const currentVal = this.state.userAnswers[idx] || '';
      html += `
        <div class="space-y-4">
          <input type="text" id="exam-numeric-input"
                 value="${currentVal}"
                 oninput="window.examEngine.saveNumeric(this.value)"
                 placeholder="Type your answer..."
                 class="w-full p-4 rounded-xl border-2 border-slate-200 focus:border-sky-500 focus:outline-none text-xl font-black text-navy-dark">
        </div>
      `;
    }

    container.innerHTML = html;
    this.renderSidebar();
    StorageManager.saveExamState(this.state);
  }

  selectOption(optIdx) {
    this.state.userAnswers[this.state.currentQuestionIndex] = optIdx;
    this.sound.playPop();
    this.renderQuestion();
  }

  saveNumeric(val) {
    this.state.userAnswers[this.state.currentQuestionIndex] = val;
  }

  renderSidebar() {
    const container = document.getElementById('sidebar-questions');
    if (!container) return;

    let html = '';
    for (let i = 0; i < 15; i++) {
      const isCurrent = i === this.state.currentQuestionIndex;
      const isAnswered = this.state.userAnswers[i] !== undefined && String(this.state.userAnswers[i]).trim() !== '';
      const isServed = i < this.state.questionsServed.length;

      let bubbleClass = 'bg-slate-100 text-slate-400';
      if (isCurrent) bubbleClass = 'bg-sky-500 text-white shadow-md ring-2 ring-sky-300';
      else if (isAnswered) bubbleClass = 'bg-emerald-500 text-white';
      else if (isServed) bubbleClass = 'bg-slate-200 text-slate-700 cursor-pointer';

      html += `
        <button onclick="${isServed ? `window.examEngine.jumpToQuestion(${i})` : ''}"
                ${!isServed ? 'disabled' : ''}
                class="sidebar-bubble ${bubbleClass}">
          ${i + 1}
        </button>
      `;
    }
    container.innerHTML = html;
  }

  jumpToQuestion(i) {
    this.state.currentQuestionIndex = i;
    this.renderQuestion();
  }

  prevQuestion() {
    if (this.state.currentQuestionIndex > 0) {
      this.state.currentQuestionIndex--;
      this.renderQuestion();
    }
  }

  nextQuestion() {
    const curIdx = this.state.currentQuestionIndex;
    const currentQ = this.state.questionsServed[curIdx];
    const userAns = this.state.userAnswers[curIdx];

    // Check correct to adapt difficulty and streak
    let isCorrect = false;
    if (currentQ.type === 'multiple-choice' && currentQ.options) {
      if (userAns !== undefined && currentQ.options[userAns]?.correct) isCorrect = true;
    } else {
      const cleanUser = String(userAns || '').trim().replace(/,/g, '');
      const cleanCorrect = String(currentQ.correctAnswer || '').trim().replace(/,/g, '');
      if (cleanUser === cleanCorrect || (currentQ.acceptedAnswers && currentQ.acceptedAnswers.includes(cleanUser))) {
        isCorrect = true;
      }
    }

    if (isCorrect) {
      this.sound.playCorrect();
      this.state.streak++;
      if (this.state.streak > this.state.maxStreak) this.state.maxStreak = this.state.streak;
    } else {
      this.sound.playTryAgain();
      this.state.streak = 0;
    }

    // Adaptive difficulty update constrained by track
    const track = this.state.selectedTrack;
    if (isCorrect) {
      if (track === '3-4') this.state.activeDifficulty = 4;
      else if (track === '5-6') this.state.activeDifficulty = 6;
      else if (track === '7-8') this.state.activeDifficulty = 8;
    } else {
      if (track === '3-4') this.state.activeDifficulty = 3;
      else if (track === '5-6') this.state.activeDifficulty = 5;
      else if (track === '7-8') this.state.activeDifficulty = 7;
    }

    if (curIdx + 1 < 15) {
      this.state.currentQuestionIndex++;
      if (this.state.currentQuestionIndex >= this.state.questionsServed.length) {
        this.fetchNextQuestion();
      }
      this.renderQuestion();
    } else {
      this.finishExam();
    }
  }

  async finishExam() {
    if (this.state.timerInterval) clearInterval(this.state.timerInterval);

    // Score calculation
    let correctCount = 0;
    this.state.questionsServed.forEach((q, idx) => {
      const ans = this.state.userAnswers[idx];
      if (q.type === 'multiple-choice' && q.options) {
        if (ans !== undefined && q.options[ans]?.correct) correctCount++;
      } else {
        const cleanUser = String(ans || '').trim().replace(/,/g, '');
        const cleanCorrect = String(q.correctAnswer || '').trim().replace(/,/g, '');
        if (cleanUser === cleanCorrect || (q.acceptedAnswers && q.acceptedAnswers.includes(cleanUser))) {
          correctCount++;
        }
      }
    });

    // Determine recommended placement grade
    const track = this.state.selectedTrack;
    let placedGrade = 3;
    if (track === '3-4') {
      placedGrade = correctCount >= 10 ? 4 : 3;
    } else if (track === '5-6') {
      placedGrade = correctCount >= 10 ? 6 : 5;
    } else {
      placedGrade = correctCount >= 10 ? 8 : 7;
    }

    // Initialize unlocked threshold in storage
    const updatedProgress = StorageManager.initializePlacementThreshold(placedGrade);
    updatedProgress.testedScore = `${correctCount}/15`;
    updatedProgress.highestStreak = Math.max(updatedProgress.highestStreak || 0, this.state.maxStreak);
    StorageManager.saveProgress(updatedProgress);

    // Save attempt payload
    const attemptPayload = {
      score: `${correctCount}/15`,
      recommendedGrade: `Grade ${placedGrade} Math Benchmark`,
      placedGrade,
      track,
      timeElapsedSeconds: this.state.secondsElapsed,
      maxStreak: this.state.maxStreak,
      questionsServed: this.state.questionsServed,
      userAnswers: this.state.userAnswers
    };

    // Store in local attempts
    const attempts = StorageManager.getItem('kss_local_attempts', []);
    attempts.push(attemptPayload);
    StorageManager.setItem('kss_local_attempts', attempts);
    sessionStorage.setItem('kss_last_results', JSON.stringify(attemptPayload));

    // Clear active exam auto-save
    StorageManager.clearExamState();

    // Persist to REST API asynchronously
    ApiClient.saveAttempt(attemptPayload);
    ApiClient.saveStudentProgress(updatedProgress);

    window.location.href = '../results/index.html';
  }
}

window.examEngine = new ExamEngine();
window.addEventListener('DOMContentLoaded', () => {
  window.examEngine.init();
});
