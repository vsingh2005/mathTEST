/* =========================================================
   KIDS STEM STUDIO - AUTHENTICATION & SESSION MANAGER
   Shared module across all portal pages
   ========================================================= */

const DEMO_USERS = [
  {
    username: 'student1',
    email: 'student1@kidsstemstudio.com',
    passwordHash: '210327580aa4df047a16ed3f6cd59beb608e139f450b195c93700ff3c7accd85',
    salt: 'kss_salt_demo_1',
    createdAt: '2026-01-01T00:00:00.000Z',
    attempts: []
  },
  {
    username: 'parent_demo',
    email: 'parent@kidsstemstudio.com',
    passwordHash: '9cccb006ad00482db28eca01064598344c80c8472c63d8a757deefbdb27a5506',
    salt: 'kss_salt_demo_2',
    createdAt: '2026-01-01T00:00:00.000Z',
    attempts: []
  }
];

function sanitizeUsername(input) {
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
window.sanitizeUsername = sanitizeUsername;

class AuthenticationManager {
  constructor() {
    this.users = [];
    try {
      // Self-heal corrupted localStorage session if present
      const rawSess = localStorage.getItem('kss_session');
      if (rawSess && (rawSess.includes('{') || rawSess.includes('"'))) {
        const clean = sanitizeUsername(rawSess);
        if (clean && !clean.includes('{')) {
          localStorage.setItem('kss_session', JSON.stringify({ username: clean, guest: false }));
        }
      }
    } catch (e) {}

    try {
      this.users = JSON.parse(localStorage.getItem('kss_users')) || [];
      if (!Array.isArray(this.users)) this.users = [];
      this.users = this.users.map(u => {
        if (u && u.username) {
          u.username = sanitizeUsername(u.username);
        }
        return u;
      });
      const uniqueMap = new Map();
      this.users.forEach(u => {
        if (u && u.username && !uniqueMap.has(u.username.toLowerCase())) {
          uniqueMap.set(u.username.toLowerCase(), u);
        }
      });
      this.users = Array.from(uniqueMap.values());
      localStorage.setItem('kss_users', JSON.stringify(this.users));
    } catch (e) {
      this.users = [];
    }

    // Ensure baseline demo users exist synchronously
    let needsSave = false;
    DEMO_USERS.forEach(demo => {
      if (!this.users.some(u => u.username && u.username.toLowerCase() === demo.username.toLowerCase())) {
        this.users.push(Object.assign({}, demo));
        needsSave = true;
      }
    });
    if (needsSave) {
      this.saveUsersToStorage();
    }

    this.currentUser = null;
    this.allAttempts = [];
    try {
      this.allAttempts = JSON.parse(localStorage.getItem('kss_attempts')) || [];
    } catch (e) {
      this.allAttempts = [];
    }

    // Synchronously resolve current session on initialization
    this.resolveCurrentUser();

    // Async background routines
    this.initDemoUsers();
    this.loadCustomSettings();
  }

  async loadCustomSettings() {
    try {
      const res = await fetch('/wp-json/kss-math/v1/settings');
      if (res.ok) {
        const s = await res.json();
        if (s.primary_color) document.documentElement.style.setProperty('--color-primary', s.primary_color);
        if (s.secondary_color) document.documentElement.style.setProperty('--color-secondary', s.secondary_color);
        if (s.brand_teal_color) document.documentElement.style.setProperty('--color-brand', s.brand_teal_color);
        if (s.navy_dark_color) document.documentElement.style.setProperty('--color-dark', s.navy_dark_color);
      }
    } catch (e) {
      // Use standard default CSS variables
    }
  }

  async hashPassword(password, salt) {
    const encoder = new TextEncoder();
    const data = encoder.encode(password + salt);
    const hashBuffer = await crypto.subtle.digest('SHA-256', data);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
  }

  async initDemoUsers() {
    let needsSave = false;
    for (const demo of DEMO_USERS) {
      const existing = this.users.find(u => u.username && u.username.toLowerCase() === demo.username.toLowerCase());
      if (!existing) {
        this.users.push(Object.assign({}, demo));
        needsSave = true;
      } else if (!existing.passwordHash) {
        existing.passwordHash = demo.passwordHash;
        existing.salt = demo.salt;
        needsSave = true;
      }
    }

    if (needsSave) {
      this.saveUsersToStorage();
    }

    this.resolveCurrentUser();
    if (this.currentUser && this.currentUser.token) {
      this.syncAttemptsFromServer();
    }
    this.updateHeaderUI();
  }

  saveUsersToStorage() {
    try {
      localStorage.setItem('kss_users', JSON.stringify(this.users));
    } catch (e) {}
  }

  saveAttemptsToStorage() {
    try {
      localStorage.setItem('kss_attempts', JSON.stringify(this.allAttempts));
    } catch (e) {}
  }

  getSession() {
    let raw = null;
    try {
      raw = localStorage.getItem('kss_session') || sessionStorage.getItem('kss_session');
    } catch (e) {}

    if (!raw || raw === 'null' || raw === 'undefined') {
      return null;
    }

    if (typeof raw === 'string') {
      let trimmed = raw.trim();
      if (!trimmed || trimmed === 'null' || trimmed === 'undefined') return null;
      while ((trimmed.startsWith('{') && trimmed.endsWith('}')) || (trimmed.startsWith('"') && trimmed.endsWith('"'))) {
        try {
          const parsed = JSON.parse(trimmed);
          if (parsed && typeof parsed === 'object') {
            if (parsed.username) parsed.username = sanitizeUsername(parsed.username);
            return parsed;
          }
          if (typeof parsed === 'string') {
            trimmed = parsed.trim();
          } else {
            break;
          }
        } catch (e) {
          break;
        }
      }
      return sanitizeUsername(trimmed);
    }

    return raw;
  }

  resolveCurrentUser() {
    const session = this.getSession();
    if (!session) {
      this.currentUser = null;
      return null;
    }

    let uname = 'Student';
    let email = '';
    let isGuest = false;

    if (typeof session === 'object' && session !== null) {
      uname = session.username ||
              (session.user && (session.user.display_name || session.user.username)) ||
              session.studentName ||
              'Student';
      email = session.email || (session.user && session.user.email) || '';
      isGuest = !!session.guest;
    } else {
      uname = String(session).trim();
      isGuest = uname.toLowerCase().includes('guest');
    }

    uname = sanitizeUsername(uname);

    let matched = this.users.find(u => u.username && sanitizeUsername(u.username).toLowerCase() === uname.toLowerCase());
    if (matched) {
      matched.username = sanitizeUsername(matched.username);
      this.currentUser = matched;
    } else {
      this.currentUser = {
        username: uname,
        displayName: uname,
        email: email,
        isGuest: isGuest,
        attempts: []
      };
    }
    this.currentUser.username = sanitizeUsername(this.currentUser.username);
    this.currentUser.displayName = sanitizeUsername(this.currentUser.displayName || this.currentUser.username);
    this.currentUser.token = (session && session.token) || localStorage.getItem('kss_jwt_token') || sessionStorage.getItem('kss_jwt_token') || null;
    this.ensureStudentUnlocked();
    return this.currentUser;
  }

  ensureStudentUnlocked() {
    try {
      const raw = localStorage.getItem('kss_student_progress');
      if (!raw) {
        const defaultProgress = {
          testedGrade: null,
          testedScore: null,
          unlockedLessonIndex: { "3": 1, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0 },
          completedLessons: {},
          totalStars: 0,
          highestStreak: 0,
          badges: []
        };
        localStorage.setItem('kss_student_progress', JSON.stringify(defaultProgress));
      } else {
        const p = JSON.parse(raw);
        let modified = false;
        if (!p.completedLessons || typeof p.completedLessons !== 'object') {
          p.completedLessons = {};
          modified = true;
        }
        if (!p.unlockedLessonIndex || typeof p.unlockedLessonIndex !== 'object') {
          p.unlockedLessonIndex = { "3": 1, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0 };
          modified = true;
        }
        if (modified) {
          localStorage.setItem('kss_student_progress', JSON.stringify(p));
        }
      }
    } catch (e) {}
  }

  isAuthenticated() {
    if (this.currentUser) return true;
    const user = this.resolveCurrentUser();
    return !!user;
  }

  requireAuth(loginUrl = 'login.html') {
    if (!this.currentUser) {
      this.resolveCurrentUser();
    }

    if (!this.currentUser) {
      try {
        localStorage.removeItem('kss_session');
        sessionStorage.removeItem('kss_session');
        localStorage.removeItem('kss_jwt_token');
        sessionStorage.removeItem('kss_jwt_token');
      } catch (e) {}
      window.location.href = loginUrl;
      return false;
    }

    this.updateHeaderUI();
    return true;
  }

  redirectIfAuth(portalUrl = 'portal.html') {
    if (this.isAuthenticated()) {
      window.location.href = portalUrl;
      return true;
    }
    return false;
  }

  async registerUser(username, email, password) {
    username = username.trim();
    email = email.trim();
    if (!username || !email || !password) {
      throw new Error('Please fill in all registration fields.');
    }

    const existing = this.users.find(u =>
      (u.username && u.username.toLowerCase() === username.toLowerCase()) ||
      (u.email && u.email.toLowerCase() === email.toLowerCase())
    );
    if (existing) {
      throw new Error('Username or email address already registered.');
    }

    const salt = 'kss_salt_' + Math.random().toString(36).substring(2);
    const passwordHash = await this.hashPassword(password, salt);

    const newUser = {
      username: username,
      email: email,
      passwordHash: passwordHash,
      salt: salt,
      createdAt: new Date().toISOString(),
      attempts: []
    };

    this.users.push(newUser);
    this.saveUsersToStorage();
    this.currentUser = newUser;
    localStorage.setItem('kss_session', JSON.stringify({
      username: newUser.username,
      email: newUser.email,
      guest: false
    }));
    this.updateHeaderUI();
    return newUser;
  }

  async loginUser(usernameOrEmail, password, rememberMe) {
    usernameOrEmail = (usernameOrEmail || '').trim();
    if (!usernameOrEmail || !password) {
      throw new Error('Username/Email and Password are required.');
    }

    let wpError = null;
    try {
      const response = await fetch('/wp-json/jwt-auth/v1/token', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          username: usernameOrEmail,
          password: password
        })
      });

      const contentType = response.headers.get('content-type') || '';
      if (contentType.includes('application/json')) {
        const data = await response.json();
        if (response.ok && data.token) {
          let user = this.users.find(u => u.username && u.username.toLowerCase() === data.user_nicename.toLowerCase());
          if (!user) {
            user = {
              username: data.user_nicename,
              email: data.user_email,
              createdAt: new Date().toISOString(),
              attempts: []
            };
            this.users.push(user);
            this.saveUsersToStorage();
          }

          this.currentUser = user;
          const sessionPayload = {
            username: user.username,
            email: user.email,
            token: data.token,
            guest: false
          };

          if (rememberMe) {
            localStorage.setItem('kss_session', JSON.stringify(sessionPayload));
            localStorage.setItem('kss_jwt_token', data.token);
          } else {
            sessionStorage.setItem('kss_session', JSON.stringify(sessionPayload));
            sessionStorage.setItem('kss_jwt_token', data.token);
          }

          this.syncAttemptsFromServer();
          this.updateHeaderUI();
          return user;
        } else {
          wpError = data.message || 'WordPress authentication failed.';
        }
      } else {
        wpError = 'WordPress REST API is not responding with JSON.';
      }
    } catch (err) {
      wpError = err.message || 'WordPress connection failed.';
    }

    // Local fallback matching
    const fallbackUser = this.users.find(u =>
      (u.username && u.username.toLowerCase() === usernameOrEmail.toLowerCase()) ||
      (u.email && u.email.toLowerCase() === usernameOrEmail.toLowerCase())
    );

    if (fallbackUser && fallbackUser.salt) {
      const computedHash = await this.hashPassword(password, fallbackUser.salt);
      if (computedHash === fallbackUser.passwordHash) {
        this.currentUser = fallbackUser;
        const sessionPayload = {
          username: fallbackUser.username,
          email: fallbackUser.email || '',
          guest: false
        };
        if (rememberMe) {
          localStorage.setItem('kss_session', JSON.stringify(sessionPayload));
        } else {
          sessionStorage.setItem('kss_session', JSON.stringify(sessionPayload));
        }
        this.updateHeaderUI();
        return fallbackUser;
      }
    }

    // Direct fallback for default demo credentials
    if (
      (usernameOrEmail.toLowerCase() === 'student1' && password === 'password123') ||
      (usernameOrEmail.toLowerCase() === 'parent_demo' && password === 'stemstudio2026')
    ) {
      const uname = usernameOrEmail.toLowerCase() === 'student1' ? 'student1' : 'parent_demo';
      let user = this.users.find(u => u.username && u.username.toLowerCase() === uname);
      if (!user) {
        user = {
          username: uname,
          email: uname + '@kidsstemstudio.com',
          attempts: []
        };
        this.users.push(user);
        this.saveUsersToStorage();
      }
      this.currentUser = user;
      const sessionPayload = {
        username: user.username,
        email: user.email || '',
        guest: false
      };
      if (rememberMe) {
        localStorage.setItem('kss_session', JSON.stringify(sessionPayload));
      } else {
        sessionStorage.setItem('kss_session', JSON.stringify(sessionPayload));
      }
      this.updateHeaderUI();
      return user;
    }

    if (wpError && !wpError.includes('connection failed') && !wpError.includes('Failed to fetch') && !wpError.includes('not responding with JSON')) {
      throw new Error(wpError);
    }
    throw new Error('Invalid username or password.');
  }

  logoutUser(redirectUrl = 'login.html') {
    this.currentUser = null;
    try {
      localStorage.removeItem('kss_session');
      sessionStorage.removeItem('kss_session');
      localStorage.removeItem('kss_jwt_token');
      sessionStorage.removeItem('kss_jwt_token');
    } catch (e) {}
    window.location.href = redirectUrl;
  }

  saveExamAttempt(attemptData) {
    const username = this.currentUser ? this.currentUser.username : 'Guest Student';
    const attempt = {
      id: 'att_' + Date.now(),
      username: username,
      timestamp: new Date().toISOString(),
      score: attemptData.score,
      totalQuestions: 15,
      timeElapsedSeconds: attemptData.timeElapsed,
      recommendedLevel: attemptData.recommendedLevel,
      answers: attemptData.answers
    };

    this.allAttempts.push(attempt);
    this.saveAttemptsToStorage();

    if (this.currentUser) {
      const userObj = this.users.find(u => u.username === this.currentUser.username);
      if (userObj) {
        if (!userObj.attempts) userObj.attempts = [];
        userObj.attempts.push(attempt.id);
        this.saveUsersToStorage();
      }

      const token = this.currentUser.token || localStorage.getItem('kss_jwt_token') || sessionStorage.getItem('kss_jwt_token');
      if (token) {
        fetch('/wp-json/kss-math/v1/save-attempt', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
          },
          body: JSON.stringify(attempt)
        }).catch(err => {
          console.error('Error syncing attempt to WordPress:', err);
        });
      }
    }
    return attempt;
  }

  getUserAttempts(username) {
    return this.allAttempts.filter(a => a.username && a.username.toLowerCase() === String(username).toLowerCase());
  }

  async syncAttemptsFromServer() {
    const token = this.currentUser ? (this.currentUser.token || localStorage.getItem('kss_jwt_token') || sessionStorage.getItem('kss_jwt_token')) : null;
    if (!token) return;

    try {
      const response = await fetch('/wp-json/kss-math/v1/get-attempts', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + token
        }
      });
      if (response.ok) {
        const data = await response.json();
        if (data.success && Array.isArray(data.attempts)) {
          const serverAttempts = data.attempts.map((att, index) => {
            return {
              id: 'att_server_' + index + '_' + Date.now(),
              username: this.currentUser.username,
              timestamp: att.timestamp,
              score: att.score,
              totalQuestions: 15,
              timeElapsedSeconds: att.timeElapsedSeconds,
              recommendedLevel: att.recommendedLevel,
              answers: att.answers || []
            };
          });

          const otherUsersAttempts = this.allAttempts.filter(a => a.username && a.username.toLowerCase() !== this.currentUser.username.toLowerCase());
          this.allAttempts = [...otherUsersAttempts, ...serverAttempts];
          this.saveAttemptsToStorage();
        }
      }
    } catch (err) {
      console.error('Error syncing attempts from server:', err);
    }
  }

  updateHeaderUI() {
    const headerWidget = document.getElementById('user-header-widget');
    if (headerWidget) {
      if (this.currentUser) {
        const cleanName = sanitizeUsername(this.currentUser.username);
        const initial = cleanName.charAt(0).toUpperCase() || 'S';
        headerWidget.innerHTML = `
          <div class="flex items-center gap-2 bg-slate-100/90 py-1 pl-1.5 pr-2.5 rounded-full border border-slate-200 text-xs shadow-xs">
            <span class="w-6 h-6 rounded-full bg-[#287F78] text-white flex items-center justify-center font-black text-xs">
              ${initial}
            </span>
            <span class="font-extrabold text-[#253238]">${cleanName}</span>
            <div class="h-3 w-px bg-slate-300 mx-0.5"></div>
            <button onclick="AuthManager.renderHistoryModal()" class="text-[11px] font-bold text-sky-600 hover:underline">History</button>
            <button onclick="AuthManager.logoutUser()" class="text-[11px] font-bold text-rose-500 hover:underline">Logout</button>
          </div>
        `;
      } else {
        headerWidget.innerHTML = `
          <a href="login.html" class="px-3 py-1.5 text-xs font-bold text-white bg-sky-500 hover:bg-sky-600 rounded-lg transition-colors">Log In</a>
        `;
      }
    }

    // Sync stars display if present in header
    const headerStars = document.getElementById('header-stars-display');
    if (headerStars) {
      try {
        const rawP = localStorage.getItem('kss_student_progress');
        if (rawP) {
          const p = JSON.parse(rawP);
          headerStars.textContent = `${p.totalStars || 0} Stars`;
        }
      } catch (e) {}
    }

    // Sync nav placement button if present in header
    const navLabel = document.getElementById('nav-placement-label');
    if (navLabel) {
      try {
        const rawP = localStorage.getItem('kss_student_progress');
        const p = rawP ? JSON.parse(rawP) : {};
        const placed = p.testedGrade;
        if (!placed) {
          navLabel.textContent = 'Placement Exam';
        } else if (placed < 8) {
          navLabel.textContent = `Test into Grade ${placed + 1}`;
        } else {
          navLabel.textContent = 'Curriculum Mastered';
        }
      } catch (e) {}
    }
  }

  renderHistoryModal() {
    const historyModal = document.getElementById('history-modal');
    const container = document.getElementById('user-history-content');
    if (!historyModal || !container) return;

    if (!this.currentUser) {
      container.innerHTML = `
        <div class="text-center py-8 text-slate-500 font-semibold">
          Please log in to view your saved math placement exam history.
        </div>
      `;
    } else {
      const attempts = this.getUserAttempts(this.currentUser.username);
      if (attempts.length === 0) {
        container.innerHTML = `
          <div class="text-center py-8 space-y-2">
            <p class="text-slate-600 font-bold text-sm">No exam attempts found yet.</p>
            <p class="text-slate-400 text-xs">Complete a math assessment to view your solution breakdown here.</p>
          </div>
        `;
      } else {
        attempts.sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));
        let html = '';
        attempts.forEach(att => {
          const dateStr = new Date(att.timestamp).toLocaleString();
          const mins = Math.floor((att.timeElapsedSeconds || 0) / 60);
          const secs = (att.timeElapsedSeconds || 0) % 60;

          html += `
            <div class="bg-slate-50 p-4 rounded-xl border border-slate-200 space-y-2 text-xs">
              <div class="flex justify-between items-center font-bold">
                <span class="text-[#263238] text-sm">${att.recommendedLevel}</span>
                <span class="text-emerald-600 bg-emerald-100 px-2.5 py-0.5 rounded-full">Score: ${att.score}/${att.totalQuestions}</span>
              </div>
              <div class="flex justify-between text-slate-500 font-medium">
                <span>Completed: ${dateStr}</span>
                <span>Time: ${mins}m ${secs}s</span>
              </div>
            </div>
          `;
        });
        container.innerHTML = html;
      }
    }

    if (window.openModal) {
      window.openModal('history-modal');
    } else if (historyModal) {
      historyModal.classList.remove('hidden');
      historyModal.classList.add('flex');
    }
  }
}

const AuthManager = new AuthenticationManager();
window.AuthManager = AuthManager;

function handlePlacementAction() {
  try {
    const rawP = localStorage.getItem('kss_student_progress');
    const p = rawP ? JSON.parse(rawP) : {};
    const placed = p.testedGrade;
    if (!placed) {
      sessionStorage.removeItem('targetLevelUpGrade');
      window.location.href = 'portal.html';
    } else if (placed < 8) {
      const targetGrade = placed + 1;
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
}
window.handlePlacementAction = handlePlacementAction;
