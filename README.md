# GTA 6 — all keys for mouse & keyboard (Xbox Remote Play)

🌐 **English** · [Português](README.pt-BR.md)

Play **GTA 6 on your Xbox** with **mouse and keyboard on your PC**, through Remote Play.
The game keeps running on the console; the PC turns your mouse and keyboard into an Xbox controller.

Every action in GTA 6's default controller layout is mapped: on foot, aiming, melee,
swimming, parachute, land/water vehicles, bicycles and aircraft.

> ⚠️ **Warning:** in online modes, a mouse "disguised" as a controller may be considered cheating
> (like XIM/Cronus) and could get you banned. The risk is much lower in story mode. Use at your own risk.

## Two versions

| Folder | Works with | How it works |
|---|---|---|
| [`gta6-mouse-app/`](gta6-mouse-app) | **Xbox app** on Windows | Python program that creates a virtual Xbox 360 controller (ViGEmBus driver) |
| [`gta6-mouse/`](gta6-mouse) | Remote Play **in the browser** (xbox.com/remoteplay) | Edge/Chrome extension that pretends to be a controller on the page |

---

## Xbox app version (recommended)

### Requirements
- Windows 10/11 64-bit
- [Python 3](https://www.python.org/downloads/) (tick "Add Python to PATH" during setup)
- **ViGEmBus** driver (its installer ships with the `vgamepad` library)
- Xbox with **Remote features** enabled, on the same network as the PC

### Install
```powershell
pip install -r requirements.txt
```
If the ViGEmBus driver is not installed automatically, run the installer located at
`...\site-packages\vgamepad\win\vigem\install\x64\ViGEmBusSetup_x64.msi`.

### Usage
1. Turn off your real controller.
2. Double-click **`gta6-mouse-app/INICIAR.bat`** and leave the window open.
3. In the Xbox app, start Remote Play to your console and open GTA 6.
4. Click the Xbox app window: you hear a beep, the cursor hides and the mouse becomes the camera.
5. **F8** toggles on/off (gives you the normal mouse back). Alt+Tab also releases it.

The program shows its messages in Portuguese on a Portuguese Windows and in English otherwise.

### Modes and tuning
| Key | Function |
|---|---|
| **V** | ON FOOT ↔ VEHICLE (car, motorcycle, boat, bicycle) |
| **N** | ON FOOT ↔ AIRCRAFT |
| **- / =** | lower / raise mouse sensitivity |
| **9 / 0** | lower / raise deadzone |
| **F8** | on / off |

The full key list is in [`gta6-mouse-app/README.md`](gta6-mouse-app/README.md).

### Main keys (on foot)
| Key | Action | Controller |
|---|---|---|
| WASD | move | L |
| Mouse | look / aim | R |
| Left / right button | shoot / aim | RT / LT |
| Shift | sprint | L3 |
| Space | jump / climb | A |
| C | crouch (hold = rest) | B |
| F | melee | X |
| E | interact / enter vehicle | Y |
| Q | take cover | RB |
| Tab | draw/holster weapon (hold = inventory) | LB |
| Z | look behind | R3 |
| T / O / X / K | phone / objective / radio / detonate | D-pad |
| M | map | View |
| Esc | pause | Menu |
| Enter / Backspace | confirm / back in menus | A / B |

### Tips for lower latency
- **In GTA 6:** camera and aim sensitivity at max, acceleration at min, deadzone at min.
- **In Windows:** untick *Enhance pointer precision* (Mouse > Pointer Options).
- **Network:** PC and console wired (or 5 GHz Wi-Fi), on the same network, with Open NAT.
- **In the code** (`gta_mouse.py`): `SUAVIZACAO_MS` (smoothing), `CURVA` (curve), `TAXA_HZ` (update rate)
  and the key maps are at the top of the file.

---

## Browser version

1. Open `edge://extensions`, turn on **Developer mode** and click **Load unpacked**.
2. Pick the [`gta6-mouse/`](gta6-mouse) folder.
3. Open **https://www.xbox.com/remoteplay**, connect to your console and click the game screen.

Details in [`gta6-mouse/README.md`](gta6-mouse/README.md).

---

## Credits
- Virtual controller: [ViGEmBus](https://github.com/nefarius/ViGEmBus) via [vgamepad](https://github.com/yannbouteiller/vgamepad)
- Keyboard and mouse hooks: [pynput](https://github.com/moses-palmer/pynput)
- Browser version idea inspired by [Better xCloud](https://github.com/redphx/better-xcloud)

Independent project, not affiliated with Rockstar Games, Take-Two or Microsoft.
