"""GTA 6 Mouse para o app Xbox (Remote Play) no PC.

Cria um controle de Xbox 360 virtual (driver ViGEmBus) e transforma
mouse + teclado em botões e analógicos. Só funciona enquanto a janela
do app Xbox está em primeiro plano.

F8 = liga/desliga   V = a pé / veículo   N = aeronave
- = = sensibilidade   9 0 = zona morta
"""
import atexit
import ctypes
import ctypes.wintypes as wt
import math
import os
import sys
import threading
import time
import winsound

import vgamepad as vg
from pynput import keyboard, mouse

# ======================= CONFIGURAÇÃO =======================
SENS_PADRAO = 1.3       # sensibilidade do mouse (muda com - e =)
DEADZONE_PADRAO = 0.22  # pula a zona morta do analógico do jogo (muda com 9 e 0)
CURVA = 0.75            # < 1 deixa movimentos pequenos mais fortes
SUAVIZACAO_MS = 6       # 0 = cru (mais tremido), 15 = bem suave (mais atraso)
TAXA_HZ = 500           # atualizações do controle por segundo
ESCONDER_CURSOR = True
TITULOS_XBOX = ("xbox",)  # janela onde o programa age (título começa com isso)

# Teclas: letra/número entre aspas, ou nomes: SPACE SHIFT CTRL ALT TAB ENTER CAPS UP DOWN LEFT RIGHT
# Mouse: MOUSE_ESQ MOUSE_DIR MOUSE_MEIO MOUSE_4 MOUSE_5 RODA
# Controle: A B X Y LB RB LT RT VIEW MENU LS RS CIMA BAIXO ESQ DIR
# WASD move o analógico esquerdo (no veículo, W/S viram acelerar/frear).
MAP_A_PE = {
    "SPACE": "A",          # pular / escalar  (luta: bloquear/esquivar; natação: subir)
    "C": "B", "CTRL": "B", # agachar  (segurar = descansar)
    "F": "X",              # corpo a corpo: soco / chute
    "E": "Y",              # interagir / entrar no veículo  (mirando: trocar arma)
    "TAB": "LB",           # guardar arma  (segurar = equipamento)
    "Q": "RB",             # cobertura  (natação: mergulhar)
    "G": "RB",             # arremesso rápido (segure mirando)
    "SHIFT": "LS",         # correr  (natação: nadar mais rápido)
    "Z": "RS",             # olhar / zoom  (segurar = olhar para trás)
    "M": "VIEW",           # mapa
    "ESC": "MENU", "P": "MENU",  # pausa / configurações
    "ENTER": "A",          # confirmar nos menus
    "BACKSPACE": "B",      # voltar nos menus
    "T": "CIMA",           # celular  (segurar = app Waink; mirando: aproximar)
    "O": "BAIXO",          # objetivo / minimapa  (segurar = navegação rápida; mirando: afastar)
    "X": "ESQ",            # trocar de ombro (segurar) / rádio
    "K": "DIR",            # detonar explosivos  (segurar = menu do parceiro)
    "UP": "CIMA", "DOWN": "BAIXO", "LEFT": "ESQ", "RIGHT": "DIR",
    "1": "CIMA", "2": "BAIXO", "3": "ESQ", "4": "DIR",
    "MOUSE_ESQ": "RT",     # atirar  (luta: agarrar)
    "MOUSE_DIR": "LT",     # mirar / interagir  (luta: travar alvo)
    "MOUSE_MEIO": "RS",
    "MOUSE_4": "LB",       # botão lateral de trás: equipamento
    "MOUSE_5": "Y",        # botão lateral da frente: trocar arma
    "RODA": "Y",           # rodinha: trocar arma
}
MAP_VEICULO = {
    "W": "RT",             # acelerar  (bike: pedalar)
    "S": "LT",             # frear / ré
    "SPACE": "A",          # freio de mão  (bike: corrida)
    "E": "Y",              # sair do veículo
    "F": "X",              # corpo a corpo
    "C": "B",              # farol  (segurar = abaixar-se; bike: pulo)
    "SHIFT": "LS", "H": "LS",  # buzina / nitro  (bike: campainha)
    "TAB": "LB",           # guardar / equipamento
    "Z": "RS",             # olhar para trás
    "M": "VIEW",
    "ESC": "MENU", "P": "MENU", "ENTER": "A",
    "BACKSPACE": "B",
    "T": "CIMA",           # celular  (segurar = interagir)
    "O": "BAIXO",          # objetivo / minimapa
    "Q": "ESQ",            # seta esquerda  (segurar = menu do veículo)
    "R": "DIR",            # seta direita  (segurar = menu do parceiro)
    "X": "ESQ", "K": "DIR",
    "UP": "CIMA", "DOWN": "BAIXO", "LEFT": "ESQ", "RIGHT": "DIR",
    "1": "CIMA", "2": "BAIXO", "3": "ESQ", "4": "DIR",
    "MOUSE_ESQ": "RB",     # atirar do veículo
    "MOUSE_DIR": "LT",
    "MOUSE_MEIO": "RS",
    "MOUSE_4": "LB",
    # rodinha e mouse 5 ficam livres aqui: Y = sair do veículo
}
MAP_AERONAVE = {           # WASD: arfagem / rolagem no analógico esquerdo
    "SHIFT": "RT",         # mais motor
    "CTRL": "LT",          # menos motor
    "Q": "X",              # guinada à esquerda
    "E": "B",              # guinada à direita
    "F": "Y",              # sair
    "G": "LS",             # trem de pouso
    "Z": "RS",             # olhar para trás
    "TAB": "LB",
    "M": "VIEW",
    "ESC": "MENU", "P": "MENU", "ENTER": "A",
    "BACKSPACE": "B",
    "T": "CIMA", "O": "BAIXO", "X": "ESQ", "K": "DIR",
    "UP": "CIMA", "DOWN": "BAIXO", "LEFT": "ESQ", "RIGHT": "DIR",
    "1": "CIMA", "2": "BAIXO", "3": "ESQ", "4": "DIR",
    "MOUSE_ESQ": "RB",     # atirar
    "MOUSE_DIR": "LT",
    "MOUSE_MEIO": "RS",
    # rodinha livre aqui: Y = sair da aeronave
}
MAPAS = {"a_pe": MAP_A_PE, "veiculo": MAP_VEICULO, "aeronave": MAP_AERONAVE}
# Idioma das mensagens: português no Windows em português, inglês nos outros.
# Para forçar: IDIOMA = "pt" ou IDIOMA = "en".
IDIOMA = None
if IDIOMA is None:
    try:
        IDIOMA = "pt" if (ctypes.windll.kernel32.GetUserDefaultUILanguage() & 0x3FF) == 0x16 else "en"
    except Exception:
        IDIOMA = "en"

TEXTOS = {
    "pt": {
        "modos": {"a_pe": "A PÉ", "veiculo": "VEÍCULO", "aeronave": "AERONAVE"},
        "titulo": "GTA 6 Mouse para o app Xbox  -  feche esta janela para sair\n",
        "desligado": "DESLIGADO  (F8 liga)",
        "esperando": "Esperando: clique na janela do app Xbox  (F8 desliga)",
        "ativo": "ATIVO: {modo}  (V veículo, N aeronave)  sens {sens:.2f} (- =)  zona morta {dz:.2f} (9 0)",
        "sem_driver": "Não consegui criar o controle virtual. O driver ViGEmBus está instalado?",
        "sair": "Enter para sair",
        "cursor": "Cursor do Windows restaurado.",
    },
    "en": {
        "modos": {"a_pe": "ON FOOT", "veiculo": "VEHICLE", "aeronave": "AIRCRAFT"},
        "titulo": "GTA 6 Mouse for the Xbox app  -  close this window to quit\n",
        "desligado": "OFF  (F8 turns on)",
        "esperando": "Waiting: click the Xbox app window  (F8 turns off)",
        "ativo": "ACTIVE: {modo}  (V vehicle, N aircraft)  sens {sens:.2f} (- =)  deadzone {dz:.2f} (9 0)",
        "sem_driver": "Could not create the virtual controller. Is the ViGEmBus driver installed?",
        "sair": "Press Enter to quit",
        "cursor": "Windows cursor restored.",
    },
}
T = TEXTOS[IDIOMA]
NOMES_MODO = T["modos"]
# ============================================================

VK_NOMES = {0x20: "SPACE", 0xA0: "SHIFT", 0xA1: "SHIFT", 0x10: "SHIFT",
            0xA2: "CTRL", 0xA3: "CTRL", 0x11: "CTRL", 0xA4: "ALT", 0x12: "ALT",
            0x09: "TAB", 0x0D: "ENTER", 0x14: "CAPS", 0x1B: "ESC", 0x08: "BACKSPACE",
            0x25: "LEFT", 0x26: "UP", 0x27: "RIGHT", 0x28: "DOWN"}
VK_F8, VK_V, VK_N = 0x77, 0x56, 0x4E
VK_SENS_MENOS, VK_SENS_MAIS = 0xBD, 0xBB        # - =  (mesmo lugar no ABNT2 e no americano)
VK_DZ_MENOS, VK_DZ_MAIS = 0x39, 0x30            # 9 0

B = vg.XUSB_BUTTON
BOTOES = {
    "A": B.XUSB_GAMEPAD_A, "B": B.XUSB_GAMEPAD_B, "X": B.XUSB_GAMEPAD_X, "Y": B.XUSB_GAMEPAD_Y,
    "LB": B.XUSB_GAMEPAD_LEFT_SHOULDER, "RB": B.XUSB_GAMEPAD_RIGHT_SHOULDER,
    "VIEW": B.XUSB_GAMEPAD_BACK, "MENU": B.XUSB_GAMEPAD_START,
    "LS": B.XUSB_GAMEPAD_LEFT_THUMB, "RS": B.XUSB_GAMEPAD_RIGHT_THUMB,
    "CIMA": B.XUSB_GAMEPAD_DPAD_UP, "BAIXO": B.XUSB_GAMEPAD_DPAD_DOWN,
    "ESQ": B.XUSB_GAMEPAD_DPAD_LEFT, "DIR": B.XUSB_GAMEPAD_DPAD_RIGHT,
}

WM_MOUSEMOVE, WM_LDOWN, WM_LUP, WM_RDOWN, WM_RUP, WM_MDOWN, WM_MUP, WM_WHEEL, WM_XDOWN, WM_XUP = (
    0x0200, 0x0201, 0x0202, 0x0204, 0x0205, 0x0207, 0x0208, 0x020A, 0x020B, 0x020C)
WM_KEYDOWN, WM_KEYUP, WM_SYSKEYDOWN, WM_SYSKEYUP = 0x0100, 0x0101, 0x0104, 0x0105
LLMHF_INJECTED = 0x01

user32 = ctypes.windll.user32
winmm = ctypes.windll.winmm
kernel32 = ctypes.windll.kernel32
user32.CreateCursor.restype = ctypes.c_void_p
user32.CreateCursor.argtypes = [wt.HINSTANCE, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
                                ctypes.c_void_p, ctypes.c_void_p]
user32.SetSystemCursor.argtypes = [ctypes.c_void_p, wt.DWORD]
user32.SystemParametersInfoW.argtypes = [wt.UINT, wt.UINT, ctypes.c_void_p, wt.UINT]

PASTA = os.path.dirname(os.path.abspath(__file__))
CONFIG = os.path.join(PASTA, "ajustes.txt")


# ---------------- cursor invisível ----------------
CURSORES = (32512, 32513, 32514, 32515, 32516, 32640, 32641, 32642, 32643,
            32644, 32645, 32646, 32648, 32649, 32650, 32651)
_cursor_escondido = False


def esconder_cursor():
    global _cursor_escondido
    if _cursor_escondido or not ESCONDER_CURSOR:
        return
    e_mask = (ctypes.c_ubyte * 128)(*([0xFF] * 128))
    x_mask = (ctypes.c_ubyte * 128)()
    for cid in CURSORES:
        h = user32.CreateCursor(None, 0, 0, 32, 32, e_mask, x_mask)
        if h:
            user32.SetSystemCursor(h, cid)
    _cursor_escondido = True


def mostrar_cursor(forcar=False):
    global _cursor_escondido
    if _cursor_escondido or forcar:
        user32.SystemParametersInfoW(0x0057, 0, None, 0)  # SPI_SETCURSORS: volta os cursores do Windows
        _cursor_escondido = False


# ---------------- utilidades ----------------
def vk_para_nome(vk):
    if vk in VK_NOMES:
        return VK_NOMES[vk]
    if 0x30 <= vk <= 0x39 or 0x41 <= vk <= 0x5A:
        return chr(vk)
    return None


def janela_xbox_em_foco():
    hwnd = user32.GetForegroundWindow()
    if not hwnd:
        return None
    buf = ctypes.create_unicode_buffer(256)
    user32.GetWindowTextW(hwnd, buf, 256)
    if not buf.value.strip().lower().startswith(TITULOS_XBOX):
        return None
    r = wt.RECT()
    user32.GetWindowRect(hwnd, ctypes.byref(r))
    return ((r.left + r.right) // 2, (r.top + r.bottom) // 2)


class Estado:
    def __init__(self):
        self.lock = threading.Lock()
        self.ligado = True
        self.ativo = False
        self.modo = "a_pe"
        self.pressionadas = set()
        self.pulsos = {}
        self.acc_x = 0.0
        self.acc_y = 0.0
        self.centro = None
        self.avisos = []
        self.sens = SENS_PADRAO
        self.deadzone = DEADZONE_PADRAO
        try:
            with open(CONFIG) as f:
                s, d = f.read().split()
                self.sens, self.deadzone = float(s), float(d)
        except (OSError, ValueError):
            pass

    def salvar(self):
        try:
            with open(CONFIG, "w") as f:
                f.write(f"{self.sens:.3f} {self.deadzone:.3f}")
        except OSError:
            pass


E = Estado()


def stick_da_velocidade(v, sens, deadzone):
    """v em pixels/ms -> valor do analógico (-1..1)."""
    if v == 0:
        return 0.0
    forca = min(1.0, (abs(v) * sens) ** CURVA)
    return math.copysign(min(1.0, deadzone + forca * (1 - deadzone)), v)


def calcular_controle(pressionadas, pulsos_ativos, modo):
    """Devolve (botões, lt, rt, lx, ly) a partir das entradas."""
    mapa = MAPAS[modo]
    alvos = {mapa[e] for e in pressionadas | pulsos_ativos if e in mapa}
    botoes = {BOTOES[a] for a in alvos if a in BOTOES}
    lt = 1.0 if "LT" in alvos else 0.0
    rt = 1.0 if "RT" in alvos else 0.0
    lx = (1 if "D" in pressionadas else 0) - (1 if "A" in pressionadas else 0)
    ly = 0 if modo == "veiculo" else (1 if "W" in pressionadas else 0) - (1 if "S" in pressionadas else 0)
    n = math.hypot(lx, ly)
    if n > 1:
        lx, ly = lx / n, ly / n
    return botoes, lt, rt, float(lx), float(ly)


def tecla_e_nossa(nome):
    if nome is None:
        return False
    return nome in ("W", "A", "S", "D") or any(nome in m for m in MAPAS.values())


# ---------------- ganchos de teclado e mouse ----------------
def filtro_teclado(msg, data):
    vk = data.vkCode
    desce = msg in (WM_KEYDOWN, WM_SYSKEYDOWN)
    with E.lock:
        if vk == VK_F8:
            if desce and "F8" not in E.pressionadas:
                E.ligado = not E.ligado
                E.avisos.append("ligou" if E.ligado else "desligou")
            (E.pressionadas.add if desce else E.pressionadas.discard)("F8")
            teclado_listener.suppress_event()
            return
        if not E.ativo:
            return
        if vk in (VK_V, VK_N):
            chave = "V" if vk == VK_V else "N"
            if desce and chave not in E.pressionadas:
                if vk == VK_V:
                    E.modo = "a_pe" if E.modo == "veiculo" else "veiculo"
                else:
                    E.modo = "a_pe" if E.modo == "aeronave" else "aeronave"
                E.avisos.append(E.modo)
            (E.pressionadas.add if desce else E.pressionadas.discard)(chave)
            teclado_listener.suppress_event()
            return
        if vk in (VK_SENS_MENOS, VK_SENS_MAIS):
            if desce:
                E.sens = max(0.1, min(8.0, E.sens * (1.1 if vk == VK_SENS_MAIS else 1 / 1.1)))
                E.salvar()
                E.avisos.append("ajuste")
            teclado_listener.suppress_event()
            return
        if vk in (VK_DZ_MENOS, VK_DZ_MAIS):
            if desce:
                passo = 0.02 if vk == VK_DZ_MAIS else -0.02
                E.deadzone = max(0.0, min(0.5, E.deadzone + passo))
                E.salvar()
                E.avisos.append("ajuste")
            teclado_listener.suppress_event()
            return
        nome = vk_para_nome(vk)
        if not tecla_e_nossa(nome):
            return
        if desce:
            E.pressionadas.add(nome)
        else:
            E.pressionadas.discard(nome)
    teclado_listener.suppress_event()


def filtro_mouse(msg, data):
    with E.lock:
        if not E.ativo:
            return
        if msg == WM_MOUSEMOVE:
            if data.flags & LLMHF_INJECTED or E.centro is None:
                return
            E.acc_x += data.pt.x - E.centro[0]
            E.acc_y += data.pt.y - E.centro[1]
        elif msg in (WM_LDOWN, WM_LUP):
            (E.pressionadas.add if msg == WM_LDOWN else E.pressionadas.discard)("MOUSE_ESQ")
        elif msg in (WM_RDOWN, WM_RUP):
            (E.pressionadas.add if msg == WM_RDOWN else E.pressionadas.discard)("MOUSE_DIR")
        elif msg in (WM_MDOWN, WM_MUP):
            (E.pressionadas.add if msg == WM_MDOWN else E.pressionadas.discard)("MOUSE_MEIO")
        elif msg in (WM_XDOWN, WM_XUP):
            nome = "MOUSE_4" if (data.mouseData >> 16) == 1 else "MOUSE_5"
            (E.pressionadas.add if msg == WM_XDOWN else E.pressionadas.discard)(nome)
        elif msg == WM_WHEEL:
            E.pulsos["RODA"] = time.perf_counter() + 0.09
        else:
            return
    mouse_listener.suppress_event()


teclado_listener = keyboard.Listener(win32_event_filter=filtro_teclado)
mouse_listener = mouse.Listener(win32_event_filter=filtro_mouse)


def mostrar_estado():
    if not E.ligado:
        texto = T["desligado"]
    elif not E.ativo:
        texto = T["esperando"]
    else:
        texto = T["ativo"].format(modo=NOMES_MODO[E.modo], sens=E.sens, dz=E.deadzone)
    print(f"\r{texto:<96}", end="", flush=True)


def _ao_fechar_console(_tipo):
    mostrar_cursor(forcar=True)
    return False


_handler = ctypes.WINFUNCTYPE(wt.BOOL, wt.DWORD)(_ao_fechar_console)


def main():
    print(T["titulo"])
    mostrar_cursor(forcar=True)  # garante cursor normal se uma execução anterior caiu
    atexit.register(mostrar_cursor, True)
    kernel32.SetConsoleCtrlHandler(_handler, True)
    try:
        pad = vg.VX360Gamepad()
    except Exception as e:  # driver ausente
        print(T["sem_driver"])
        print(e)
        input(T["sair"])
        return
    winmm.timeBeginPeriod(1)  # timer do Windows em 1 ms (menos atraso)
    teclado_listener.start()
    mouse_listener.start()
    rx = ry = 0.0
    periodo = 1.0 / TAXA_HZ
    ultimo = time.perf_counter()
    ultimo_estado = None
    try:
        while True:
            time.sleep(periodo)
            agora = time.perf_counter()
            dt_ms = max(0.5, (agora - ultimo) * 1000)
            ultimo = agora
            centro = janela_xbox_em_foco() if E.ligado else None
            with E.lock:
                era_ativo = E.ativo
                E.ativo = centro is not None
                if E.ativo and (not era_ativo or centro != E.centro):
                    E.centro = centro
                    user32.SetCursorPos(*centro)
                    E.acc_x = E.acc_y = 0.0
                if not E.ativo and era_ativo:
                    E.pressionadas = {p for p in E.pressionadas if p == "F8"}
                    E.pulsos.clear()
                vx, vy = E.acc_x / dt_ms, E.acc_y / dt_ms
                E.acc_x = E.acc_y = 0.0
                pulsos = {k for k, t in E.pulsos.items() if t > agora}
                E.pulsos = {k: t for k, t in E.pulsos.items() if t > agora}
                press = set(E.pressionadas)
                modo, sens, dz, ativo = E.modo, E.sens, E.deadzone, E.ativo
                avisos, E.avisos = E.avisos, []

            if ativo and not era_ativo:
                esconder_cursor()
            elif era_ativo and not ativo:
                mostrar_cursor()

            alvo_x = stick_da_velocidade(vx, sens, dz) if ativo else 0.0
            alvo_y = stick_da_velocidade(vy, sens, dz) if ativo else 0.0
            k = math.exp(-dt_ms / SUAVIZACAO_MS) if SUAVIZACAO_MS > 0 else 0.0
            rx = rx * k + alvo_x * (1 - k)
            ry = ry * k + alvo_y * (1 - k)
            if abs(rx) < dz * 0.5 and alvo_x == 0:
                rx = 0.0
            if abs(ry) < dz * 0.5 and alvo_y == 0:
                ry = 0.0

            pad.reset()
            if ativo:
                botoes, lt, rt, lx, ly = calcular_controle(press, pulsos, modo)
                for b in botoes:
                    pad.press_button(button=b)
                pad.left_trigger_float(value_float=lt)
                pad.right_trigger_float(value_float=rt)
                pad.left_joystick_float(x_value_float=lx, y_value_float=ly)
                pad.right_joystick_float(x_value_float=max(-1.0, min(1.0, rx)),
                                         y_value_float=max(-1.0, min(1.0, -ry)))
            pad.update()

            if avisos:
                threading.Thread(target=_bipes, args=(avisos,), daemon=True).start()
            estado = (E.ligado, ativo, modo, round(sens, 2), round(dz, 2))
            if estado != ultimo_estado:
                mostrar_estado()
                ultimo_estado = estado
    except KeyboardInterrupt:
        pass
    finally:
        mostrar_cursor(forcar=True)
        winmm.timeEndPeriod(1)
        pad.reset()
        pad.update()


def _bipes(avisos):
    for a in avisos:
        winsound.Beep({"ligou": 880, "desligou": 440, "veiculo": 660, "aeronave": 770,
                       "a_pe": 550, "ajuste": 990}.get(a, 700), 50)


if __name__ == "__main__":
    if "--teste" in sys.argv:
        p = vg.VX360Gamepad()
        time.sleep(1)
        p.press_button(button=B.XUSB_GAMEPAD_A)
        p.right_joystick_float(x_value_float=0.5, y_value_float=0.0)
        p.update()
        time.sleep(float(sys.argv[2]) if len(sys.argv) > 2 else 3)
        p.reset()
        p.update()
    elif "--mostrar-cursor" in sys.argv:
        mostrar_cursor(forcar=True)
        print(T["cursor"])
    else:
        main()
