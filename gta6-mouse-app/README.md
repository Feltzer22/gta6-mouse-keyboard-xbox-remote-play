# GTA 6 Mouse — mouse & keyboard for the Xbox app (Remote Play)

🌐 **English** · [Português](LEIA-ME.md)

Creates a virtual Xbox controller on Windows (ViGEmBus driver) and turns your mouse and
keyboard into that controller. It only acts while the **Xbox app** window is in the foreground.

## How to use
1. Turn off your real controller.
2. Double-click **INICIAR.bat** and leave the black window open.
3. Start Remote Play in the Xbox app and click its window: beep, the cursor hides and the mouse becomes the camera.
4. **F8** pauses (normal mouse back). Alt+Tab also releases it.

If the Windows cursor disappears and doesn't come back (program killed), run
`python gta_mouse.py --mostrar-cursor` or just open INICIAR.bat again.

## Modes
- **V**: ON FOOT ↔ VEHICLE (car, motorcycle, boat, bicycle)
- **N**: ON FOOT ↔ AIRCRAFT
- **- / =**: lower / raise mouse sensitivity
- **9 / 0**: lower / raise deadzone. Both are saved in `ajustes.txt`.

## On foot (also swimming, melee and parachute)
| Key | GTA 6 action | Controller |
|---|---|---|
| WASD | move | left stick |
| Mouse | camera / aim | right stick |
| Left button | shoot · melee: grab | RT |
| Right button | aim / interact · melee: lock on | LT |
| Shift | sprint · swim faster | L3 |
| Space | jump / climb · block/dodge · surface · open parachute | A |
| C / Ctrl | crouch (hold = rest) | B |
| F | punch / kick | X |
| E / wheel / mouse 5 | interact, enter vehicle · aiming: quick weapon swap | Y |
| Tab / mouse 4 | draw/holster weapon (hold = inventory) | LB |
| Q | take cover · dive | RB |
| G | quick throw (hold while aiming) | RB |
| Z / middle button | look / zoom (hold = look behind) | R3 |
| T / ↑ / 1 | phone (hold = Waink app) · aiming: zoom in | D-pad ↑ |
| O / ↓ / 2 | objective / minimap (hold = quick navigation) · aiming: zoom out | D-pad ↓ |
| X / ← / 3 | radio · aiming (hold): switch shoulder | D-pad ← |
| K / → / 4 | detonate explosives (hold = partner menu) | D-pad → |
| M | map | View |
| Esc / P | pause / settings (all modes) | Menu |
| Enter | confirm in menus (all modes) | A |
| Backspace | back in menus (all modes) | B |

**Parachute** (use ON FOOT mode): Space opens (A), E releases (Y), right / left mouse button
brake left / right (LT / RT), Q shoots (RB).

## Vehicle (press V) — cars, motorcycles, boats and bicycles
| Key | Action | Controller |
|---|---|---|
| W / S | accelerate / brake & reverse (bike: pedal) | RT / LT |
| A / D | steer | left stick |
| Space | handbrake (bike: sprint) | A |
| Left button | shoot from vehicle | RB |
| E | exit vehicle / bicycle | Y |
| F | melee | X |
| C | headlights (hold = duck · bike: jump) | B |
| Shift / H | horn / nitro (bike: bell) | L3 |
| Q / R | left / right turn signal (hold = vehicle / partner menu) | D-pad ← / → |
| T / O | phone / objective | D-pad ↑ / ↓ |
| Z | look behind | R3 |

The wheel and side button 5 do nothing in vehicle and aircraft modes, so you don't exit by accident.

## Aircraft (press N)
| Key | Action | Controller |
|---|---|---|
| W / S | pitch (nose down / up) | left stick |
| A / D | roll | left stick |
| Shift / Ctrl | throttle up / down | RT / LT |
| Q / E | yaw left / right | X / B |
| G | landing gear | L3 |
| F | exit | Y |
| Left button | shoot | RB |

## Faster and more precise
**In GTA 6** (Settings > Controls):
- Camera and aim sensitivity: max, or close to it.
- Aim/camera acceleration: min or off (if available).
- Right stick deadzone: min.
- If the camera keeps drifting after you stop the mouse, lower the deadzone here with **9**.
- If small mouse movements don't move the camera, raise it with **0**.

**In Windows:** Settings > Bluetooth & devices > Mouse > Additional mouse settings >
Pointer Options > untick **Enhance pointer precision**. Aim stays consistent regardless of hand speed.

**In the program** (top of `gta_mouse.py`): lower `SUAVIZACAO_MS` = rawer, faster response;
lower `CURVA` = stronger small movements. Messages follow the Windows language (Portuguese or English);
set `IDIOMA = "en"` to force English.

**Network:** console and PC wired to the router (or 5 GHz Wi-Fi), same network, nothing downloading while you play.

## Warning
In online modes, a mouse "disguised" as a controller may be considered cheating (like XIM/Cronus)
and could get you banned. The risk is much lower in story mode.
