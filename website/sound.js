/**
 * Kids STEM Studio Math Assessment & Practice
 * SoundEffectManager: Zero-asset Web Audio Synthesizer
 * 
 * Generates pleasant educational UI sounds using native browser Web Audio API.
 * No external audio files or downloads required.
 */
export class SoundEffectManager {
  constructor() {
    this.storageKey = 'kss_sound_muted';
    this.muted = localStorage.getItem(this.storageKey) === 'true';
    this.ctx = null;
    this.isUnlocked = false;

    // Attach unlock listener on first user gesture
    const unlockAudio = () => {
      this.ensureContext();
      if (this.ctx && this.ctx.state === 'running') {
        this.isUnlocked = true;
        window.removeEventListener('click', unlockAudio);
        window.removeEventListener('touchstart', unlockAudio);
      }
    };
    window.addEventListener('click', unlockAudio, { passive: true });
    window.addEventListener('touchstart', unlockAudio, { passive: true });
  }

  ensureContext() {
    if (!this.ctx) {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (AudioCtx) {
        this.ctx = new AudioCtx();
      }
    }
    if (this.ctx && this.ctx.state === 'suspended') {
      this.ctx.resume().catch(() => {});
    }
    return this.ctx;
  }

  isMuted() {
    return this.muted;
  }

  toggleMute() {
    this.muted = !this.muted;
    localStorage.setItem(this.storageKey, this.muted ? 'true' : 'false');
    this.updateSoundButtons();
    if (!this.muted) {
      this.playPop();
    }
    return this.muted;
  }

  updateSoundButtons() {
    const buttons = document.querySelectorAll('.sound-toggle-btn');
    const speakerSvg = `<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072M17.95 6.05a8 8 0 010 11.9M6 10H3a1 1 0 00-1 1v2a1 1 0 001 1h3l5 4V6l-5 4z"/></svg>`;
    const muteSvg = `<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5.586 15H3a1 1 0 01-1-1v-2a1 1 0 011-1h2.586l4.707-4.707A1 1 0 0112 7v10a1 1 0 01-1.707.707L5.586 15zM17 14l4-4m0 4l-4-4"/></svg>`;

    buttons.forEach(btn => {
      if (this.muted) {
        btn.innerHTML = `${muteSvg} <span class="text-xs font-bold text-slate-500">Muted</span>`;
        btn.setAttribute('title', 'Sound Muted (Click to Unmute)');
        btn.classList.add('is-muted');
        btn.classList.remove('is-active', 'opacity-75');
      } else {
        btn.innerHTML = `${speakerSvg} <span class="text-xs font-bold text-sky-700">Sound ON</span>`;
        btn.setAttribute('title', 'Sound Enabled (Click to Mute)');
        btn.classList.add('is-active');
        btn.classList.remove('is-muted', 'opacity-75');
      }
    });
  }

  playTone(freq, startTime, duration, type = 'sine', maxGain = 0.15) {
    if (this.muted) return;
    const ctx = this.ensureContext();
    if (!ctx) return;

    try {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();

      osc.type = type;
      osc.frequency.setValueAtTime(freq, startTime);

      gain.gain.setValueAtTime(0.001, startTime);
      gain.gain.exponentialRampToValueAtTime(maxGain, startTime + 0.02);
      gain.gain.exponentialRampToValueAtTime(0.0001, startTime + duration);

      osc.connect(gain);
      gain.connect(ctx.destination);

      osc.start(startTime);
      osc.stop(startTime + duration);
    } catch (e) {}
  }

  playPop() {
    if (this.muted) return;
    const ctx = this.ensureContext();
    if (!ctx) return;

    try {
      const now = ctx.currentTime;
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();

      osc.type = 'sine';
      osc.frequency.setValueAtTime(500, now);
      osc.frequency.exponentialRampToValueAtTime(750, now + 0.04);

      gain.gain.setValueAtTime(0.08, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.05);

      osc.connect(gain);
      gain.connect(ctx.destination);

      osc.start(now);
      osc.stop(now + 0.05);
    } catch (e) {}
  }

  playCorrect() {
    if (this.muted) return;
    const ctx = this.ensureContext();
    if (!ctx) return;

    const now = ctx.currentTime;
    this.playTone(659.25, now, 0.15, 'sine', 0.12);        // E5
    this.playTone(880.00, now + 0.11, 0.35, 'sine', 0.15); // A5
  }

  playTryAgain() {
    if (this.muted) return;
    const ctx = this.ensureContext();
    if (!ctx) return;

    const now = ctx.currentTime;
    this.playTone(392.00, now, 0.14, 'triangle', 0.08);        // G4
    this.playTone(349.23, now + 0.10, 0.22, 'triangle', 0.08); // F4
  }

  playHint() {
    if (this.muted) return;
    const ctx = this.ensureContext();
    if (!ctx) return;

    const now = ctx.currentTime;
    this.playTone(523.25, now, 0.1, 'sine', 0.08);        // C5
    this.playTone(659.25, now + 0.08, 0.1, 'sine', 0.09); // E5
    this.playTone(783.99, now + 0.16, 0.2, 'sine', 0.10); // G5
  }

  playStreak() {
    if (this.muted) return;
    const ctx = this.ensureContext();
    if (!ctx) return;

    const now = ctx.currentTime;
    const notes = [523.25, 659.25, 783.99, 1046.50]; // C5, E5, G5, C6
    notes.forEach((freq, idx) => {
      this.playTone(freq, now + idx * 0.07, 0.22, 'sine', 0.12);
    });
  }

  playFanfare() {
    if (this.muted) return;
    const ctx = this.ensureContext();
    if (!ctx) return;

    const now = ctx.currentTime;
    const notes = [
      { f: 523.25, t: 0.00, d: 0.18 },
      { f: 659.25, t: 0.15, d: 0.18 },
      { f: 783.99, t: 0.30, d: 0.22 },
      { f: 1046.50, t: 0.48, d: 0.60 }
    ];
    notes.forEach(n => {
      this.playTone(n.f, now + n.t, n.d, 'triangle', 0.14);
    });
  }
}

// Attach globally and export for ES Module or script tag usage
if (typeof window !== 'undefined') {
  if (!window.soundManager) {
    window.soundManager = new SoundEffectManager();
  }
  document.addEventListener('DOMContentLoaded', () => {
    window.soundManager.updateSoundButtons();
  });
}
