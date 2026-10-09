/**
 * Kids STEM Studio Math Assessment & Practice
 * SoundEffectManager: Zero-asset Web Audio Synthesizer
 * 
 * Generates pleasant educational UI sounds using native browser Web Audio API.
 * No external audio files or downloads required.
 */
class SoundEffectManager {
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
    buttons.forEach(btn => {
      if (this.muted) {
        btn.innerHTML = '🔇 <span class="hidden sm:inline text-xs font-bold text-slate-400">Muted</span>';
        btn.setAttribute('title', 'Sound Muted (Click to Unmute)');
        btn.classList.add('opacity-75');
      } else {
        btn.innerHTML = '🔊 <span class="hidden sm:inline text-xs font-bold text-sky-600">Sound ON</span>';
        btn.setAttribute('title', 'Sound Enabled (Click to Mute)');
        btn.classList.remove('opacity-75');
      }
    });
  }

  /**
   * Helper to play synthesized tone with envelope
   */
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
    } catch (e) {
      // Audio context policy or unsupported
    }
  }

  /**
   * Subtle button / click pop
   */
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

  /**
   * Joyful two-tone chime on correct answer (E5 -> A5)
   */
  playCorrect() {
    if (this.muted) return;
    const ctx = this.ensureContext();
    if (!ctx) return;

    const now = ctx.currentTime;
    this.playTone(659.25, now, 0.15, 'sine', 0.12);        // E5
    this.playTone(880.00, now + 0.11, 0.35, 'sine', 0.15); // A5
  }

  /**
   * Encouraging, gentle soft tone on incorrect / retry (not harsh)
   */
  playTryAgain() {
    if (this.muted) return;
    const ctx = this.ensureContext();
    if (!ctx) return;

    const now = ctx.currentTime;
    this.playTone(392.00, now, 0.14, 'triangle', 0.08);        // G4
    this.playTone(349.23, now + 0.10, 0.22, 'triangle', 0.08); // F4
  }

  /**
   * Sparkly ascending chime when revealing a hint
   */
  playHint() {
    if (this.muted) return;
    const ctx = this.ensureContext();
    if (!ctx) return;

    const now = ctx.currentTime;
    this.playTone(523.25, now, 0.1, 'sine', 0.08);        // C5
    this.playTone(659.25, now + 0.08, 0.1, 'sine', 0.09); // E5
    this.playTone(783.99, now + 0.16, 0.2, 'sine', 0.10); // G5
  }

  /**
   * Energetic ascending arpeggio on streak milestones (3, 5, 10 in a row)
   */
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

  /**
   * Triumphant fanfare upon exam or practice completion
   */
  playFanfare() {
    if (this.muted) return;
    const ctx = this.ensureContext();
    if (!ctx) return;

    const now = ctx.currentTime;
    // Chords / notes sequence: C5 -> E5 -> G5 -> C6 held
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

// Global singleton instance
window.soundManager = new SoundEffectManager();

document.addEventListener('DOMContentLoaded', () => {
  window.soundManager.updateSoundButtons();
});
