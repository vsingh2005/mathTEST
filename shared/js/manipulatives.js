/**
 * Kids STEM Studio - Interactive Visual Manipulatives & Child Math Inputs
 * 
 * Provides interactive tactile tools:
 * 1. Fraction Bar & Pizza Slicer
 * 2. Number Line Hopper
 * 3. Area & Grid Unit Highlighter
 * 4. Child-friendly Touch Keypad
 * 5. Equation Tile Builder
 */

export class Manipulatives {
  /**
   * Renders an interactive fraction bar where kids can change divisions and shade parts
   */
  static renderFractionBar(containerId, initialDenominator = 4, onChange = null) {
    const container = document.getElementById(containerId);
    if (!container) return;

    let denominator = initialDenominator;
    let shaded = new Set([0]);

    const update = () => {
      let slicesHtml = '';
      for (let i = 0; i < denominator; i++) {
        const isShaded = shaded.has(i);
        slicesHtml += `
          <div onclick="window.__toggleSlice('${containerId}', ${i})"
               class="fraction-slice flex-1 h-14 border-r-2 border-white flex items-center justify-center font-bold text-xs select-none transition-all ${isShaded ? 'bg-sky-500 text-white' : 'bg-slate-200 text-slate-400'}">
            ${isShaded ? '1/' + denominator : ''}
          </div>
        `;
      }

      container.innerHTML = `
        <div class="manipulative-box space-y-3">
          <div class="flex items-center justify-between text-xs font-bold text-slate-500">
            <span>Interactive Fraction Bar:</span>
            <div class="flex items-center space-x-2">
              <span>Slices:</span>
              <button onclick="window.__changeDenom('${containerId}', -1)" class="w-6 h-6 rounded bg-slate-200 hover:bg-slate-300 font-bold">-</button>
              <span class="text-sky-600 font-black text-sm">${denominator}</span>
              <button onclick="window.__changeDenom('${containerId}', 1)" class="w-6 h-6 rounded bg-slate-200 hover:bg-slate-300 font-bold">+</button>
            </div>
          </div>

          <div class="w-full flex rounded-xl overflow-hidden border-2 border-slate-300 shadow-inner">
            ${slicesHtml}
          </div>

          <div class="flex items-center justify-between text-sm font-extrabold text-navy-dark pt-1">
            <span>Shaded Fraction: <span class="text-sky-600 text-base">${shaded.size}/${denominator}</span></span>
            <span class="text-xs text-slate-400 font-medium">(Click pieces to shade / un-shade)</span>
          </div>
        </div>
      `;

      if (onChange) {
        onChange({ numerator: shaded.size, denominator, value: shaded.size / denominator });
      }
    };

    window.__toggleSlice = (cId, idx) => {
      if (cId !== containerId) return;
      if (shaded.has(idx)) shaded.delete(idx);
      else shaded.add(idx);
      if (window.soundManager) window.soundManager.playPop();
      update();
    };

    window.__changeDenom = (cId, delta) => {
      if (cId !== containerId) return;
      const nextD = Math.min(12, Math.max(2, denominator + delta));
      if (nextD !== denominator) {
        denominator = nextD;
        shaded.clear();
        shaded.add(0);
        if (window.soundManager) window.soundManager.playPop();
        update();
      }
    };

    update();
  }

  /**
   * Renders an interactive number line with draggable hopper
   */
  static renderNumberLine(containerId, min = 0, max = 10, initialVal = 4, onChange = null) {
    const container = document.getElementById(containerId);
    if (!container) return;

    let currentVal = initialVal;

    const update = () => {
      const percent = ((currentVal - min) / (max - min)) * 100;
      container.innerHTML = `
        <div class="manipulative-box space-y-4">
          <div class="flex items-center justify-between text-xs font-bold text-slate-500">
            <span>Interactive Number Line:</span>
            <span class="text-emerald-700 font-black text-sm bg-emerald-50 px-2.5 py-0.5 rounded-full border border-emerald-200">
              Position: ${currentVal}
            </span>
          </div>

          <div class="relative py-4 px-2">
            <input type="range" min="${min}" max="${max}" value="${currentVal}" step="1"
                   oninput="window.__updateNL('${containerId}', this.value)"
                   class="w-full h-3 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-emerald-500">
            <div class="flex justify-between text-xs font-bold text-slate-400 mt-2">
              <span>${min}</span>
              <span>${Math.round((min + max) / 2)}</span>
              <span>${max}</span>
            </div>
          </div>
        </div>
      `;

      if (onChange) {
        onChange(currentVal);
      }
    };

    window.__updateNL = (cId, val) => {
      if (cId !== containerId) return;
      currentVal = parseFloat(val);
      if (window.soundManager) window.soundManager.playPop();
      update();
    };

    update();
  }

  /**
   * Renders an interactive 2D grid unit highlighter for Area & Perimeter
   */
  static renderAreaGrid(containerId, rows = 5, cols = 6, onChange = null) {
    const container = document.getElementById(containerId);
    if (!container) return;

    let selectedRows = 3;
    let selectedCols = 4;

    const update = () => {
      let gridHtml = '';
      for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
          const isHighlighted = r < selectedRows && c < selectedCols;
          gridHtml += `
            <div onclick="window.__selectGridCell('${containerId}', ${r + 1}, ${c + 1})"
                 class="w-8 h-8 md:w-10 md:h-10 border border-slate-200 rounded-sm cursor-pointer transition-all ${isHighlighted ? 'bg-amber-400 border-amber-500' : 'bg-slate-50 hover:bg-slate-100'}">
            </div>
          `;
        }
      }

      const area = selectedRows * selectedCols;
      const perimeter = 2 * (selectedRows + selectedCols);

      container.innerHTML = `
        <div class="manipulative-box space-y-3">
          <div class="flex items-center justify-between text-xs font-bold text-slate-500">
            <span>Area & Perimeter Geoboard:</span>
            <span class="text-xs text-slate-400">(Click any square to adjust rectangle)</span>
          </div>

          <div class="flex justify-center p-2">
            <div class="grid gap-1" style="grid-template-columns: repeat(${cols}, minmax(0, 1fr));">
              ${gridHtml}
            </div>
          </div>

          <div class="grid grid-cols-2 gap-3 text-center pt-2 border-t border-slate-100">
            <div class="bg-amber-50 p-2 rounded-xl border border-amber-200">
              <span class="text-xs text-amber-800 font-bold block">Area (Units²)</span>
              <span class="text-lg font-black text-amber-600">${selectedRows} × ${selectedCols} = ${area}</span>
            </div>
            <div class="bg-teal-50 p-2 rounded-xl border border-teal-200">
              <span class="text-xs text-teal-800 font-bold block">Perimeter (Border)</span>
              <span class="text-lg font-black text-teal-600">2(${selectedRows}+${selectedCols}) = ${perimeter}</span>
            </div>
          </div>
        </div>
      `;

      if (onChange) {
        onChange({ rows: selectedRows, cols: selectedCols, area, perimeter });
      }
    };

    window.__selectGridCell = (cId, r, c) => {
      if (cId !== containerId) return;
      selectedRows = r;
      selectedCols = c;
      if (window.soundManager) window.soundManager.playPop();
      update();
    };

    update();
  }

  /**
   * Renders an on-screen child-friendly touch keypad for math inputs
   */
  static renderTouchKeypad(targetInputId, containerId = 'math-keypad-container') {
    const container = document.getElementById(containerId);
    const targetInput = document.getElementById(targetInputId);
    if (!container || !targetInput) return;

    const keys = [
      '1', '2', '3', '+', '×',
      '4', '5', '6', '-', '÷',
      '7', '8', '9', '/', '=',
      '0', '.', '⌫', '(', ')'
    ];

    let buttonsHtml = '';
    keys.forEach(k => {
      buttonsHtml += `
        <button type="button" onclick="window.__pressKeypad('${targetInputId}', '${k}')" class="keypad-btn">
          ${k}
        </button>
      `;
    });

    container.innerHTML = `
      <div class="math-touch-keypad">
        ${buttonsHtml}
      </div>
    `;

    window.__pressKeypad = (inputId, key) => {
      const input = document.getElementById(inputId);
      if (!input) return;
      if (window.soundManager) window.soundManager.playPop();

      if (key === '⌫') {
        input.value = input.value.slice(0, -1);
      } else {
        input.value += key;
      }
      input.dispatchEvent(new Event('input', { bubbles: true }));
    };
  }
}

// Global attach
if (typeof window !== 'undefined') {
  window.Manipulatives = Manipulatives;
}
