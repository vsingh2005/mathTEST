/**
 * Kids STEM Studio - Reusable Web Components & Digital Scratchpad
 * 
 * Defines custom elements: <kss-header>, <kss-footer>, and the interactive
 * digital scratchpad canvas with math stamps.
 */

export class KSSHeader extends HTMLElement {
  connectedCallback() {
    const isPagesSubdir = window.location.pathname.includes('/pages/');
    const portalUrl = isPagesSubdir ? '../portal/index.html' : 'portal.html';
    const practiceUrl = isPagesSubdir ? '../practice/index.html' : 'practice.html';

    this.innerHTML = `
      <header class="w-full bg-white border-b border-slate-100 py-4 px-6 md:px-12 flex items-center justify-between sticky top-0 z-50">
        <div class="flex items-center space-x-3 cursor-pointer" onclick="window.location.href='${portalUrl}'">
          <img src="https://kidsstemstudio.com/wp-content/uploads/2020/05/KSS_Logo.png" alt="Kids STEM Studio Logo"
            class="h-10 w-auto kss-header-logo">
          <span class="text-xl font-extrabold text-[#263238] tracking-tight">Math Placement Portal</span>
        </div>

        <nav class="hidden md:flex items-center space-x-8 text-slate-500 font-semibold">
          <a href="${portalUrl}" class="hover:text-sky-500 transition-colors">Dashboard</a>
          <a href="${practiceUrl}" class="hover:text-sky-500 transition-colors">Worksheets</a>
          <button onclick="openGlobalModal('faq-modal')" class="hover:text-sky-500 transition-colors">FAQ</button>
          <button onclick="openGlobalModal('contact-modal')" class="hover:text-sky-500 transition-colors">Contact</button>
        </nav>

        <div id="user-header-widget" class="flex items-center space-x-4">
          <!-- Populated by AuthManager.updateHeaderUI() -->
        </div>
      </header>
    `;
  }
}

export class KSSFooter extends HTMLElement {
  connectedCallback() {
    this.innerHTML = `
      <footer class="w-full bg-[#1e272e] text-white border-t border-slate-800 py-12 px-6 md:px-12">
        <div class="max-w-6xl w-full mx-auto grid grid-cols-1 md:grid-cols-4 gap-8">
          <div class="space-y-4">
            <h4 class="text-lg font-black text-[#4DA8FF]">Curriculum</h4>
            <ul class="space-y-2 text-slate-300 font-semibold text-sm">
              <li><a href="https://kidsstemstudio.com/our-approach" target="_blank" class="hover:text-sky-400">Our Approach</a></li>
              <li><a href="https://kidsstemstudio.com/robotics" target="_blank" class="hover:text-sky-400">Robotics</a></li>
              <li><a href="https://kidsstemstudio.com/coding-and-game-design" target="_blank" class="hover:text-sky-400">Coding & Game Design</a></li>
            </ul>
          </div>
          <div class="space-y-4">
            <h4 class="text-lg font-black text-[#4DA8FF]">Programs</h4>
            <ul class="space-y-2 text-slate-300 font-semibold text-sm">
              <li><a href="https://kidsstemstudio.com/weekly-classes/" target="_blank" class="hover:text-sky-400">Weekly Classes</a></li>
              <li><a href="https://kidsstemstudio.com/camps/" target="_blank" class="hover:text-sky-400">Camps</a></li>
              <li><a href="https://kidsstemstudio.com/afterschool-enrichment/" target="_blank" class="hover:text-sky-400">Afterschool Enrichment</a></li>
            </ul>
          </div>
          <div class="space-y-4">
            <h4 class="text-lg font-black text-[#4DA8FF]">Locations</h4>
            <ul class="space-y-2 text-slate-300 font-semibold text-sm">
              <li><a href="https://kidsstemstudio.com/chicago/" target="_blank" class="hover:text-sky-400">Chicago</a></li>
              <li><a href="https://kidsstemstudio.com/evanston" target="_blank" class="hover:text-sky-400">Evanston / Skokie</a></li>
              <li><a href="https://kidsstemstudio.com/" target="_blank" class="hover:text-sky-400">Naperville</a></li>
            </ul>
          </div>
          <div class="space-y-4 flex flex-col items-start">
            <img src="https://kidsstemstudio.com/wp-content/uploads/2020/05/KSS_Logo.png" alt="KSS" class="h-16 w-auto bg-white p-2 rounded-xl">
            <p class="text-slate-400 text-xs font-semibold pt-2">© 2026 Kids STEM Studio. All Rights Reserved.</p>
          </div>
        </div>
      </footer>
    `;
  }
}

/**
 * Digital Scratchpad Modal with Math Stamps
 */
export class DigitalScratchpad {
  constructor() {
    this.modal = null;
    this.canvas = null;
    this.ctx = null;
    this.isDrawing = false;
    this.currentColor = '#1e293b';
    this.currentWidth = 3;
    this.mode = 'pen'; // 'pen', 'highlighter', 'eraser'
    this.history = [];
  }

  init() {
    if (document.getElementById('scratchpad-modal-root')) return;

    const root = document.createElement('div');
    root.id = 'scratchpad-modal-root';
    root.className = 'scratchpad-modal hidden';
    root.innerHTML = `
      <div class="scratchpad-box">
        <div class="flex items-center justify-between p-4 bg-slate-50 border-b border-slate-200">
          <div class="flex items-center space-x-2">
            <svg class="w-5 h-5 text-sky-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"/></svg>
            <h3 class="font-black text-slate-800 text-lg">Math Scratchpad & Whiteboard</h3>
          </div>
          <button onclick="window.scratchpad.close()" class="text-slate-400 hover:text-slate-600 text-2xl font-bold px-2">×</button>
        </div>

        <!-- Toolbar -->
        <div class="flex flex-wrap items-center justify-between p-3 bg-white border-b border-slate-100 gap-2">
          <!-- Drawing tools -->
          <div class="flex items-center space-x-2">
            <button onclick="window.scratchpad.setMode('pen')" id="sp-btn-pen" class="px-3 py-1.5 rounded-lg bg-sky-100 text-sky-700 font-bold text-xs">Pen</button>
            <button onclick="window.scratchpad.setMode('highlighter')" id="sp-btn-hl" class="px-3 py-1.5 rounded-lg bg-slate-100 text-slate-700 font-bold text-xs">Highlighter</button>
            <button onclick="window.scratchpad.setMode('eraser')" id="sp-btn-eraser" class="px-3 py-1.5 rounded-lg bg-slate-100 text-slate-700 font-bold text-xs">Eraser</button>
            <button onclick="window.scratchpad.clear()" class="px-3 py-1.5 rounded-lg bg-rose-50 text-rose-600 font-bold text-xs">Clear</button>
          </div>

          <!-- Color palette -->
          <div class="flex items-center space-x-1.5">
            <button onclick="window.scratchpad.setColor('#1e293b')" class="w-6 h-6 rounded-full bg-slate-800 border-2 border-white shadow-sm" title="Black"></button>
            <button onclick="window.scratchpad.setColor('#2563eb')" class="w-6 h-6 rounded-full bg-blue-600 border-2 border-white shadow-sm" title="Blue"></button>
            <button onclick="window.scratchpad.setColor('#16a34a')" class="w-6 h-6 rounded-full bg-emerald-600 border-2 border-white shadow-sm" title="Green"></button>
            <button onclick="window.scratchpad.setColor('#ea580c')" class="w-6 h-6 rounded-full bg-amber-600 border-2 border-white shadow-sm" title="Amber"></button>
            <button onclick="window.scratchpad.setColor('#dc2626')" class="w-6 h-6 rounded-full bg-rose-600 border-2 border-white shadow-sm" title="Red"></button>
          </div>

          <!-- Math Stamps -->
          <div class="flex items-center space-x-1.5 border-l border-slate-200 pl-3">
            <span class="text-xs font-bold text-slate-400">Stamps:</span>
            <button onclick="window.scratchpad.stamp('numberline')" class="px-2.5 py-1 bg-amber-50 text-amber-700 rounded-lg text-xs font-extrabold">Number Line</button>
            <button onclick="window.scratchpad.stamp('grid')" class="px-2.5 py-1 bg-teal-50 text-teal-700 rounded-lg text-xs font-extrabold">5x5 Grid</button>
            <button onclick="window.scratchpad.stamp('tenframe')" class="px-2.5 py-1 bg-purple-50 text-purple-700 rounded-lg text-xs font-extrabold">10-Frame</button>
          </div>
        </div>

        <!-- Canvas -->
        <div class="flex-1 relative overflow-hidden bg-white">
          <canvas id="scratchpad-canvas" class="scratchpad-canvas"></canvas>
        </div>
      </div>
    `;

    document.body.appendChild(root);
    this.modal = root;
    this.canvas = document.getElementById('scratchpad-canvas');
    this.ctx = this.canvas.getContext('2d');

    this.setupListeners();
  }

  /**
   * Mounts the scratchpad directly into an embedded side-by-side workspace container
   */
  mountEmbedded(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    let savedData = null;
    if (this.canvas) {
      try {
        savedData = this.canvas.toDataURL();
      } catch (e) {}
    }

    container.innerHTML = `
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm flex flex-col overflow-hidden h-[640px]">
        <div class="flex items-center justify-between px-4 py-3 bg-slate-50 border-b border-slate-200">
          <div class="flex items-center space-x-2">
            <svg class="w-4 h-4 text-sky-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"/></svg>
            <span class="text-xs font-bold uppercase tracking-wider text-slate-700">Scratchpad Workspace</span>
          </div>
          <div class="flex items-center space-x-2">
            <button type="button" onclick="window.scratchpad.clear()" class="px-2.5 py-1 rounded-lg bg-rose-50 text-rose-600 hover:bg-rose-100 font-bold text-xs transition-colors">
              Clear Canvas
            </button>
          </div>
        </div>

        <!-- Toolbar -->
        <div class="p-2.5 bg-white border-b border-slate-100 flex flex-wrap items-center justify-between gap-2 text-xs">
          <div class="flex items-center space-x-1">
            <button type="button" onclick="window.scratchpad.setMode('pen')" id="sp-btn-pen" class="px-2.5 py-1 rounded-lg bg-sky-100 text-sky-700 font-bold">Pen</button>
            <button type="button" onclick="window.scratchpad.setMode('highlighter')" id="sp-btn-hl" class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 font-bold">Highlighter</button>
            <button type="button" onclick="window.scratchpad.setMode('eraser')" id="sp-btn-eraser" class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 font-bold">Eraser</button>
          </div>

          <!-- Color palette -->
          <div class="flex items-center space-x-1.5">
            <button type="button" onclick="window.scratchpad.setColor('#0f172a')" class="w-5 h-5 rounded-full bg-slate-900 border-2 border-white shadow-sm" title="Black"></button>
            <button type="button" onclick="window.scratchpad.setColor('#2563eb')" class="w-5 h-5 rounded-full bg-blue-600 border-2 border-white shadow-sm" title="Blue"></button>
            <button type="button" onclick="window.scratchpad.setColor('#059669')" class="w-5 h-5 rounded-full bg-emerald-600 border-2 border-white shadow-sm" title="Green"></button>
            <button type="button" onclick="window.scratchpad.setColor('#d97706')" class="w-5 h-5 rounded-full bg-amber-600 border-2 border-white shadow-sm" title="Amber"></button>
            <button type="button" onclick="window.scratchpad.setColor('#dc2626')" class="w-5 h-5 rounded-full bg-rose-600 border-2 border-white shadow-sm" title="Red"></button>
          </div>

          <!-- Math Stamps -->
          <div class="flex items-center space-x-1 border-t sm:border-t-0 sm:border-l border-slate-200 pt-1 sm:pt-0 sm:pl-2 w-full sm:w-auto">
            <span class="text-[11px] font-bold text-slate-400 mr-1">Stamps:</span>
            <button type="button" onclick="window.scratchpad.stamp('numberline')" class="px-2 py-0.5 bg-amber-50 text-amber-700 hover:bg-amber-100 rounded text-xs font-bold">Number Line</button>
            <button type="button" onclick="window.scratchpad.stamp('grid')" class="px-2 py-0.5 bg-teal-50 text-teal-700 hover:bg-teal-100 rounded text-xs font-bold">5x5 Grid</button>
            <button type="button" onclick="window.scratchpad.stamp('tenframe')" class="px-2 py-0.5 bg-purple-50 text-purple-700 hover:bg-purple-100 rounded text-xs font-bold">10-Frame</button>
          </div>
        </div>

        <!-- Canvas -->
        <div class="flex-1 relative bg-white overflow-hidden cursor-crosshair">
          <canvas id="scratchpad-canvas" class="w-full h-full block"></canvas>
        </div>
      </div>
    `;

    this.canvas = document.getElementById('scratchpad-canvas');
    this.ctx = this.canvas.getContext('2d');

    const parent = this.canvas.parentElement;
    const rect = parent.getBoundingClientRect();
    this.canvas.width = rect.width || 420;
    this.canvas.height = rect.height || 500;

    if (savedData) {
      const img = new Image();
      img.onload = () => {
        this.ctx.drawImage(img, 0, 0);
      };
      img.src = savedData;
    }

    this.setupListeners();
    this.setMode('pen');
  }

  setupListeners() {
    const resizeCanvas = () => {
      if (!this.canvas) return;
      const rect = this.canvas.parentElement.getBoundingClientRect();
      if (rect.width && rect.height) {
        let prev = null;
        try { prev = this.canvas.toDataURL(); } catch (e) {}
        this.canvas.width = rect.width;
        this.canvas.height = rect.height;
        if (prev) {
          const img = new Image();
          img.onload = () => { this.ctx.drawImage(img, 0, 0); };
          img.src = prev;
        }
      }
    };

    window.addEventListener('resize', resizeCanvas);

    const start = (e) => {
      this.isDrawing = true;
      const pos = this.getPos(e);
      this.ctx.beginPath();
      this.ctx.moveTo(pos.x, pos.y);
    };

    const move = (e) => {
      if (!this.isDrawing) return;
      const pos = this.getPos(e);
      this.ctx.lineTo(pos.x, pos.y);
      this.ctx.stroke();
    };

    const stop = () => {
      if (this.isDrawing) {
        this.ctx.closePath();
        this.isDrawing = false;
      }
    };

    this.canvas.addEventListener('mousedown', start);
    this.canvas.addEventListener('mousemove', move);
    window.addEventListener('mouseup', stop);

    this.canvas.addEventListener('touchstart', (e) => {
      e.preventDefault();
      start(e.touches[0]);
    }, { passive: false });

    this.canvas.addEventListener('touchmove', (e) => {
      e.preventDefault();
      move(e.touches[0]);
    }, { passive: false });

    this.canvas.addEventListener('touchend', stop);
  }

  getPos(e) {
    const rect = this.canvas.getBoundingClientRect();
    return {
      x: e.clientX - rect.left,
      y: e.clientY - rect.top
    };
  }

  open() {
    this.init();
    this.modal.classList.remove('hidden');
    this.modal.classList.add('flex');
    const rect = this.canvas.parentElement.getBoundingClientRect();
    this.canvas.width = rect.width;
    this.canvas.height = rect.height;
    this.setMode('pen');
  }

  close() {
    if (this.modal) {
      this.modal.classList.add('hidden');
      this.modal.classList.remove('flex');
    }
  }

  setMode(mode) {
    this.mode = mode;
    ['sp-btn-pen', 'sp-btn-hl', 'sp-btn-eraser'].forEach(id => {
      const b = document.getElementById(id);
      if (b) {
        b.className = 'px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 font-bold text-xs';
      }
    });

    if (mode === 'pen') {
      const pen = document.getElementById('sp-btn-pen');
      if (pen) {
        pen.className = 'px-2.5 py-1 rounded-lg bg-sky-100 text-sky-700 font-bold text-xs';
      }
      this.ctx.globalAlpha = 1.0;
      this.ctx.strokeStyle = this.currentColor;
      this.ctx.lineWidth = 3;
      this.ctx.lineCap = 'round';
    } else if (mode === 'highlighter') {
      const hl = document.getElementById('sp-btn-hl');
      if (hl) {
        hl.className = 'px-2.5 py-1 rounded-lg bg-amber-100 text-amber-700 font-bold text-xs';
      }
      this.ctx.globalAlpha = 0.35;
      this.ctx.strokeStyle = '#facc15';
      this.ctx.lineWidth = 18;
      this.ctx.lineCap = 'square';
    } else if (mode === 'eraser') {
      const er = document.getElementById('sp-btn-eraser');
      if (er) {
        er.className = 'px-2.5 py-1 rounded-lg bg-slate-300 text-slate-800 font-bold text-xs';
      }
      this.ctx.globalAlpha = 1.0;
      this.ctx.strokeStyle = '#ffffff';
      this.ctx.lineWidth = 24;
      this.ctx.lineCap = 'round';
    }
  }

  setColor(hex) {
    this.currentColor = hex;
    if (this.mode === 'pen') {
      this.ctx.strokeStyle = hex;
    }
  }

  clear() {
    if (!this.ctx || !this.canvas) return;
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
  }

  stamp(type) {
    if (!this.ctx || !this.canvas) return;
    const cx = this.canvas.width / 2;
    const cy = this.canvas.height / 2;
    this.ctx.save();
    this.ctx.globalAlpha = 0.85;
    this.ctx.strokeStyle = '#3b82f6';
    this.ctx.fillStyle = '#1e293b';
    this.ctx.lineWidth = 2;
    this.ctx.font = 'bold 12px Nunito, sans-serif';

    if (type === 'numberline') {
      const startX = Math.max(30, cx - 180);
      const endX = Math.min(this.canvas.width - 30, cx + 180);
      this.ctx.beginPath();
      this.ctx.moveTo(startX, cy);
      this.ctx.lineTo(endX, cy);
      this.ctx.stroke();

      const ticks = 10;
      const step = (endX - startX) / ticks;
      for (let i = 0; i <= ticks; i++) {
        const x = startX + i * step;
        this.ctx.beginPath();
        this.ctx.moveTo(x, cy - 8);
        this.ctx.lineTo(x, cy + 8);
        this.ctx.stroke();
        this.ctx.fillText(String(i), x - 4, cy + 24);
      }
    } else if (type === 'grid') {
      const size = 180;
      const x0 = cx - size / 2;
      const y0 = cy - size / 2;
      for (let i = 0; i <= 5; i++) {
        const x = x0 + (i * size) / 5;
        const y = y0 + (i * size) / 5;
        this.ctx.beginPath();
        this.ctx.moveTo(x, y0);
        this.ctx.lineTo(x, y0 + size);
        this.ctx.moveTo(x0, y);
        this.ctx.lineTo(x0 + size, y);
        this.ctx.stroke();
      }
    } else if (type === 'tenframe') {
      const w = 220;
      const h = 90;
      const x0 = cx - w / 2;
      const y0 = cy - h / 2;
      this.ctx.strokeRect(x0, y0, w, h);
      this.ctx.beginPath();
      this.ctx.moveTo(x0, y0 + h / 2);
      this.ctx.lineTo(x0 + w, y0 + h / 2);
      for (let i = 1; i < 5; i++) {
        const x = x0 + (i * w) / 5;
        this.ctx.moveTo(x, y0);
        this.ctx.lineTo(x, y0 + h);
      }
      this.ctx.stroke();
    }

    this.ctx.restore();
    this.setMode(this.mode);
  }
}

// Global modal helper
window.openGlobalModal = function(id) {
  const el = document.getElementById(id);
  if (el) {
    el.classList.remove('hidden');
    el.classList.add('flex');
  }
};

window.closeGlobalModal = function(id) {
  const el = document.getElementById(id);
  if (el) {
    el.classList.add('hidden');
    el.classList.remove('flex');
  }
};

// Initialize elements
if (typeof customElements !== 'undefined') {
  if (!customElements.get('kss-header')) customElements.define('kss-header', KSSHeader);
  if (!customElements.get('kss-footer')) customElements.define('kss-footer', KSSFooter);
}

// Initialize scratchpad on window
if (typeof window !== 'undefined') {
  window.scratchpad = new DigitalScratchpad();
}
