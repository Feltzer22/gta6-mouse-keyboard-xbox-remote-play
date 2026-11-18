# GTA 6 Mouse & Keyboard for Xbox Remote Play (PC)

🌐 **English** · [Português](README.pt-BR.md)

Play **GTA 6 on your Xbox** with **mouse and keyboard on your PC**, using Remote Play in the **Xbox app for Windows**.
The game keeps running on the console; this program turns your mouse and keyboard into a virtual Xbox controller.

Every action in GTA 6's default controller layout is mapped: on foot, aiming, melee,
swimming, parachute, land/water vehicles, bicycles and aircraft.

> ⚠️ **Warning:** in online modes, a mouse "disguised" as a controller may be considered cheating
> (like XIM/Cronus) and could get you banned. The risk is much lower in story mode. Use at your own risk.

## Features
- Virtual Xbox 360 controller (ViGEmBus) — the Xbox app sees a normal controller
- Only acts while the Xbox app window is focused; Alt+Tab gives you your normal mouse back
- Cursor hidden while playing, 500 Hz updates, tunable sensitivity and deadzone on the fly
- Three modes: on foot, vehicle and aircraft, following the official GTA 6 controls
- Messages in English or Portuguese (follows the Windows language)

## Requirements
- Windows 10/11 64-bit
- [Python 3](https://www.python.org/downloads/) (tick "Add Python to PATH" during setup)
- **ViGEmBus** driver (its installer ships with the `vgamepad` library)
- Xbox with **Remote features** enabled, on the same network as the PC

## Install
```powershell
pip install -r requirements.txt
```
If the ViGEmBus driver is not installed automatically, run the installer located at
`...\site-packages\vgamepad\win\vigem\install\x64\ViGEmBusSetup_x64.msi`.

## Usage
1. Turn off your real controller.
2. Double-click **`gta6-mouse-app/INICIAR.bat`** and leave the window open.
3. In the Xbox app, start Remote Play to your console and open GTA 6.
4. Click the Xbox app window: you hear a beep, the cursor hides and the mouse becomes the camera.
5. **F8** toggles on/off (gives you the normal mouse back). Alt+Tab also releases it.

## Modes and tuning
| Key | Function |
|---|---|
| **V** | ON FOOT ↔ VEHICLE (car, motorcycle, boat, bicycle) |
| **N** | ON FOOT ↔ AIRCRAFT |
| **- / =** | lower / raise mouse sensitivity |
| **9 / 0** | lower / raise deadzone |
| **F8** | on / off |

The full key list for every mode is in [`gta6-mouse-app/README.md`](gta6-mouse-app/README.md).

## Main keys (on foot)
| Key | Action | Controller |
|---|---|---|
| WASD | move (Caps Lock = walk) | L |
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

## Tips for lower latency
- **In GTA 6:** camera and aim sensitivity at max, acceleration at min, deadzone at min.
- **In Windows:** untick *Enhance pointer precision* (Mouse > Pointer Options).
- **Mouse:** set the **report/polling rate to 1000 Hz** in your mouse software (e.g. Logitech G HUB >
  Sensitivity (DPI) > Report rate). This is not the DPI; DPI only changes sensitivity.
- **Network:** PC and console wired (or 5 GHz Wi-Fi), on the same network, with Open NAT.
- **In the code** (`gta_mouse.py`): `JANELA_MS` (camera smoothing window), `CURVA` (curve), `TAXA_HZ` (update rate)
  and the key maps are at the top of the file.

The program itself adds under 0.1 ms between mouse and virtual controller (measured); the remaining
delay comes from Remote Play streaming (video encoding and network).

## Troubleshooting
| Problem | Fix |
|---|---|
| `ModuleNotFoundError: No module named 'vgamepad'` | Run `pip install -r requirements.txt` in a normal terminal (same Python that runs `INICIAR.bat`). |
| "Could not create the virtual controller" | Install the ViGEmBus driver (see Install) and restart the PC. |
| Xbox app: *"We found your console but can't connect to it"* | PC and console must be on the **same network** (same router, same IP range, e.g. both `192.168.1.x`). A mesh/second router creates a separate network. Also set the PC's network profile to **Private** (Settings > Network & internet > Ethernet). |
| Remote Play shows a black screen | On PCs with two GPUs, set the Xbox app to the dedicated GPU (Settings > System > Display > Graphics) and turn HDR off. |
| Camera feels slow | Raise sensitivity with **=**, max out camera sensitivity in GTA 6, lower deadzone in the game. |
| Camera keeps drifting after stopping the mouse | Lower the deadzone with **9**. |
| Camera feels choppy | Raise `JANELA_MS` (e.g. 24) at the top of `gta_mouse.py`; check the mouse is at 1000 Hz. |
| Nothing happens when playing | The program only acts while the window whose title starts with **XBOX** is focused. Click the Xbox app window; check the black window says ACTIVE. |
| Windows cursor disappeared | Open `INICIAR.bat` again (it restores the cursor on start) or run `python gta_mouse.py --mostrar-cursor`. |
| Real controller interferes | Turn it off or unplug it while using the program. |

## Credits
- Virtual controller: [ViGEmBus](https://github.com/nefarius/ViGEmBus) via [vgamepad](https://github.com/yannbouteiller/vgamepad)
- Keyboard and mouse hooks: [pynput](https://github.com/moses-palmer/pynput)

Independent project, not affiliated with Rockstar Games, Take-Two or Microsoft.
