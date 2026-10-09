/**
 * Kids STEM Studio - Modular Login Controller
 */

import { AuthManager } from '../../shared/js/auth.js';
import { StorageManager } from '../../shared/js/storage.js';

class LoginController {
  static init() {
    AuthManager.redirectIfAuth('../portal/index.html');
  }

  static async handleSubmit(e) {
    e.preventDefault();
    const alertEl = document.getElementById('auth-alert');
    const submitBtn = document.getElementById('wp-submit');
    const username = document.getElementById('user_login').value.trim();
    const password = document.getElementById('user_pass').value;

    if (!username || !password) {
      this.showAlert('Please enter both username and password.', 'error');
      return;
    }

    submitBtn.disabled = true;
    submitBtn.innerText = 'Signing In...';

    try {
      const response = await fetch('/wp-json/jwt-auth/v1/token', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
      });

      if (response.ok) {
        const data = await response.json();
        AuthManager.setSession({
          token: data.token,
          user: {
            id: data.user_id || 1,
            display_name: data.user_display_name || username,
            email: data.user_email
          }
        });
        window.location.href = '../portal/index.html';
        return;
      }
    } catch (err) {
      console.warn('Network or REST auth unreachable, falling back to guest verification:', err);
    }

    // Local / Offline Student Session Fallback
    AuthManager.setSession({
      guest: true,
      user: {
        id: 0,
        display_name: username
      }
    });

    submitBtn.innerText = 'Entering Portal...';
    setTimeout(() => {
      window.location.href = '../portal/index.html';
    }, 600);
  }

  static startGuestSession() {
    const studentName = prompt("Enter Student's First Name:", "Guest Student") || "Guest Student";
    AuthManager.setSession({
      guest: true,
      user: {
        id: 0,
        display_name: studentName.trim()
      }
    });
    window.location.href = '../portal/index.html';
  }

  static showAlert(msg, type = 'error') {
    const el = document.getElementById('auth-alert');
    if (!el) return;
    el.innerText = msg;
    el.className = `mb-4 p-3 rounded-lg text-xs font-bold text-center ${type === 'error' ? 'bg-rose-50 text-rose-600 border border-rose-200' : 'bg-emerald-50 text-emerald-600 border border-emerald-200'}`;
    el.classList.remove('hidden');
  }

  static togglePassword() {
    const pwd = document.getElementById('user_pass');
    if (pwd) {
      pwd.type = pwd.type === 'password' ? 'text' : 'password';
    }
  }
}

window.LoginController = LoginController;
window.addEventListener('DOMContentLoaded', () => {
  LoginController.init();
});
