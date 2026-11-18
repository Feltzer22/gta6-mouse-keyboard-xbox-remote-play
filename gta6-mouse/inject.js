// GTA 6 Mouse - transforma mouse e teclado num controle de Xbox virtual
// dentro da página do Remote Play (xbox.com). Roda direto na página.
//
// F8  = liga/desliga      Clique na tela = trava o mouse e começa
// Esc = solta o mouse     V = alterna A PÉ / VEÍCULO
// [ ] = sensibilidade do mouse (-/+)
(() => {
  'use strict';
  if (window.__gtaMouseLoaded) return;
  window.__gtaMouseLoaded = true;

  // Botões do controle (padrão "standard gamepad"):
  const A = 0, B = 1, X = 2, Y = 3, LB = 4, RB = 5, LT = 6, RT = 7,
        VIEW = 8, MENU = 9, LS = 10, RS = 11, UP = 12, DOWN = 13, LEFT = 14, RIGHT = 15;

  // ======================= CONFIGURAÇÃO =======================
  // Teclas usam o "code" do teclado (KeyW, Space, ShiftLeft...).
  // Mouse: Mouse0 = esquerdo, Mouse1 = meio, Mouse2 = direito.
  const MAP_A_PE = {
    Space: A,          // pular / escalar
    KeyC: B,           // agachar (segurar = descansar)
    ControlLeft: B,
    KeyF: X,           // corpo a corpo
    KeyE: Y,           // interagir / entrar no veículo / trocar arma mirando
    Tab: LB,           // guardar arma (segurar = equipamento)
    KeyQ: RB,          // cobertura
    ShiftLeft: LS,     // correr
    KeyZ: RS,          // olhar para trás / zoom
    KeyM: VIEW,        // mapa
    Enter: MENU,       // pausa
    KeyP: MENU,
    KeyT: UP,          // celular
    ArrowUp: UP, ArrowDown: DOWN, ArrowLeft: LEFT, ArrowRight: RIGHT,
    Digit1: UP, Digit2: DOWN, Digit3: LEFT, Digit4: RIGHT,
    Mouse0: RT,        // atirar
    Mouse2: LT,        // mirar
    Mouse1: RS,
  };

  const MAP_VEICULO = {
    KeyW: RT,          // acelerar
    KeyS: LT,          // frear / ré
    Space: A,          // freio de mão
    KeyE: Y,           // sair do veículo
    KeyF: Y,
    KeyC: B,           // faróis (segurar = abaixar a cabeça)
    ShiftLeft: LS,     // buzina / nitro
    KeyH: LS,
    Tab: LB,
    KeyZ: RS,          // olhar para trás
    KeyM: VIEW,
    Enter: MENU,
    KeyP: MENU,
    KeyT: UP,
    ArrowUp: UP, ArrowDown: DOWN, ArrowLeft: LEFT, ArrowRight: RIGHT,
    Digit1: UP, Digit2: DOWN, Digit3: LEFT, Digit4: RIGHT,
    Mouse0: RB,        // atirar do veículo
    Mouse2: LT,
    Mouse1: RS,
  };

  const RODA_DO_MOUSE = Y;     // rodinha = trocar arma (Y) por um instante
  const SENS_PADRAO = 0.55;    // sensibilidade inicial do mouse
  const DEADZONE = 0.18;       // compensa a zona morta do analógico no jogo
  const SUAVIZACAO = 0.5;      // 0 = cru, 0.9 = bem suave
  const TECLA_LIGAR = 'F8';
  const TECLA_MODO = 'KeyV';
  // ============================================================

  const NUM_BOTOES = 17;
  const pressed = new Set();       // teclas/botões do mouse seguros agora
  const pulses = new Map();        // botão -> fim do toque rápido (ms)
  let enabled = true;              // F8
  let locked = false;              // mouse travado na página
  let vehicle = false;             // modo veículo
  let sens = SENS_PADRAO;
  try { const s = parseFloat(localStorage.getItem('gtaMouseSens')); if (s > 0) sens = s; } catch (_) {}

  let accX = 0, accY = 0, lastTick = performance.now();
  let rx = 0, ry = 0;

  const active = () => enabled && locked;
  const currentMap = () => (vehicle ? MAP_VEICULO : MAP_A_PE);

  // ---------- leitura do mouse -> analógico direito ----------
  function stickFromVelocity(v) {
    if (v === 0) return 0;
    const mag = Math.min(1, DEADZONE + Math.abs(v) * sens * (1 - DEADZONE));
    return Math.sign(v) * mag;
  }

  setInterval(() => {
    const now = performance.now();
    const dt = Math.max(1, now - lastTick);
    lastTick = now;
    const tx = active() ? stickFromVelocity(accX / dt) : 0;
    const ty = active() ? stickFromVelocity(accY / dt) : 0;
    accX = 0; accY = 0;
    rx = rx * SUAVIZACAO + tx * (1 - SUAVIZACAO);
    ry = ry * SUAVIZACAO + ty * (1 - SUAVIZACAO);
    if (Math.abs(rx) < 0.02) rx = 0;
    if (Math.abs(ry) < 0.02) ry = 0;
  }, 8);

  // ---------- estado do controle virtual ----------
  function snapshot() {
    const map = currentMap();
    const values = new Array(NUM_BOTOES).fill(0);
    for (const input of pressed) {
      const b = map[input];
      if (b !== undefined) values[b] = 1;
    }
    const now = performance.now();
    for (const [b, until] of pulses) {
      if (until > now) values[b] = 1; else pulses.delete(b);
    }

    // analógico esquerdo: WASD (no veículo só A/D)
    let lx = (pressed.has('KeyD') ? 1 : 0) - (pressed.has('KeyA') ? 1 : 0);
    let ly = vehicle ? 0 : (pressed.has('KeyS') ? 1 : 0) - (pressed.has('KeyW') ? 1 : 0);
    const len = Math.hypot(lx, ly);
    if (len > 1) { lx /= len; ly /= len; }

    return {
      id: 'Xbox 360 Controller (XInput STANDARD GAMEPAD)',
      index: 0,
      connected: true,
      mapping: 'standard',
      timestamp: now,
      axes: [lx, ly, rx, ry],
      buttons: values.map((v) => ({ pressed: v > 0, touched: v > 0, value: v })),
      vibrationActuator: null,
    };
  }

  // ---------- substitui o controle que a página enxerga ----------
  const realGetGamepads = navigator.getGamepads ? navigator.getGamepads.bind(navigator) : () => [];
  navigator.getGamepads = function () {
    if (!active()) return realGetGamepads();
    return [snapshot(), null, null, null];
  };

  function fireGamepadEvent(type) {
    const ev = new Event(type);
    Object.defineProperty(ev, 'gamepad', { value: snapshot() });
    window.dispatchEvent(ev);
  }

  function setLocked(v) {
    if (locked === v) return;
    locked = v;
    pressed.clear();
    pulses.clear();
    accX = accY = rx = ry = 0;
    fireGamepadEvent(v ? 'gamepadconnected' : 'gamepaddisconnected');
    updateHud();
  }

  // ---------- teclado ----------
  const isOurKey = (code) => code in MAP_A_PE || code in MAP_VEICULO ||
    ['KeyW', 'KeyA', 'KeyS', 'KeyD', TECLA_MODO, 'BracketLeft', 'BracketRight'].includes(code);

  window.addEventListener('keydown', (e) => {
    if (e.code === TECLA_LIGAR) {
      e.preventDefault(); e.stopImmediatePropagation();
      if (e.repeat) return;
      enabled = !enabled;
      if (!enabled && document.pointerLockElement) document.exitPointerLock();
      updateHud();
      return;
    }
    if (!active() || !isOurKey(e.code)) return;
    e.preventDefault(); e.stopImmediatePropagation();
    if (e.repeat) return;
    if (e.code === TECLA_MODO) { vehicle = !vehicle; pressed.clear(); updateHud(); return; }
    if (e.code === 'BracketLeft' || e.code === 'BracketRight') {
      sens = Math.max(0.05, Math.min(3, sens * (e.code === 'BracketRight' ? 1.1 : 1 / 1.1)));
      try { localStorage.setItem('gtaMouseSens', String(sens)); } catch (_) {}
      updateHud();
      return;
    }
    pressed.add(e.code);
  }, true);

  window.addEventListener('keyup', (e) => {
    if (!active() && !pressed.has(e.code)) return;
    pressed.delete(e.code);
    if (isOurKey(e.code)) { e.preventDefault(); e.stopImmediatePropagation(); }
  }, true);

  window.addEventListener('blur', () => { pressed.clear(); pulses.clear(); });

  // ---------- mouse ----------
  window.addEventListener('mousemove', (e) => {
    if (!active()) return;
    accX += e.movementX || 0;
    accY += e.movementY || 0;
    e.stopImmediatePropagation();
  }, true);

  window.addEventListener('mousedown', (e) => {
    if (!enabled) return;
    if (!locked) {
      // primeiro clique: trava o mouse na página
      const target = document.querySelector('video') || document.body || document.documentElement;
      try { const p = target.requestPointerLock(); if (p && p.catch) p.catch(() => {}); } catch (_) {}
      return;
    }
    e.preventDefault(); e.stopImmediatePropagation();
    pressed.add('Mouse' + e.button);
  }, true);

  window.addEventListener('mouseup', (e) => {
    if (!locked) return;
    e.preventDefault(); e.stopImmediatePropagation();
    pressed.delete('Mouse' + e.button);
  }, true);

  window.addEventListener('contextmenu', (e) => { if (locked) e.preventDefault(); }, true);

  window.addEventListener('wheel', (e) => {
    if (!active()) return;
    e.preventDefault(); e.stopImmediatePropagation();
    pulses.set(RODA_DO_MOUSE, performance.now() + 90);
  }, { capture: true, passive: false });

  document.addEventListener('pointerlockchange', () => {
    setLocked(!!document.pointerLockElement);
  });

  // ---------- aviso na tela ----------
  let hud = null;
  function updateHud() {
    if (!hud) return;
    if (!enabled) {
      hud.textContent = 'GTA Mouse: DESLIGADO (F8 liga)';
      hud.style.background = 'rgba(60,60,60,.75)';
    } else if (!locked) {
      hud.textContent = 'GTA Mouse: clique na tela para jogar (F8 desliga)';
      hud.style.background = 'rgba(160,110,0,.85)';
    } else {
      hud.textContent = `GTA Mouse: ${vehicle ? 'VEÍCULO' : 'A PÉ'} (V troca) · sens ${sens.toFixed(2)} ([ ]) · Esc solta`;
      hud.style.background = 'rgba(0,120,60,.85)';
    }
  }
  function mountHud() {
    if (hud || !document.body) return;
    hud = document.createElement('div');
    hud.style.cssText = 'position:fixed;top:8px;left:50%;transform:translateX(-50%);z-index:2147483647;' +
      'font:600 13px system-ui,sans-serif;color:#fff;padding:5px 12px;border-radius:6px;pointer-events:none;';
    document.body.appendChild(hud);
    updateHud();
  }
  if (document.body) mountHud();
  else document.addEventListener('DOMContentLoaded', mountHud);

  // usado só pela página de teste
  window.__gtaMouseAPI = { snapshot, setLocked, isActive: active };
})();
