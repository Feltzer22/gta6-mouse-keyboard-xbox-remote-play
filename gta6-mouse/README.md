# GTA 6 Mouse — mouse & keyboard for Xbox Remote Play (browser)

🌐 **English** · [Português](LEIA-ME.md)

A simple Edge/Chrome extension. It makes the Remote Play page (xbox.com) believe an
Xbox controller is connected — and that controller is your mouse and keyboard.

## Install (Edge)
1. Open `edge://extensions`.
2. Turn on **Developer mode** (bottom-left corner).
3. Click **Load unpacked** and pick this `gta6-mouse` folder.
4. Open **https://www.xbox.com/remoteplay** (redirects to play.xbox.com), sign in, connect to your Xbox and open GTA 6.
5. **Disconnect your real controller** (otherwise both fight each other).
6. Click the game screen: the mouse locks and the banner at the top turns green.

## Keys
| Key | On foot | Vehicle (press V) |
|---|---|---|
| WASD | move | W accelerate, S brake/reverse, A/D steer |
| Mouse | camera / aim | camera |
| Left button | shoot (RT) | shoot (RB) |
| Right button | aim (LT) | LT |
| Shift | sprint (L3) | horn/nitro (L3) |
| Space | jump (A) | handbrake (A) |
| C / Ctrl | crouch (B) | headlights (B) |
| F | melee (X) | melee (X) |
| E | interact / enter (Y) | exit (Y) |
| Q | take cover (RB) | — |
| Tab | draw/holster weapon (LB) | LB |
| Z / middle button | look behind (R3) | look behind |
| Wheel | quick weapon swap (Y) | nothing (so you don't exit the vehicle) |
| T / arrows / 1-4 | D-pad (phone, radio...) | D-pad |
| M | map (View) | map |
| P | pause (Menu) | pause |
| Enter / Backspace | confirm / back in menus (A / B) | same |

- **V**: switches between ON FOOT and VEHICLE (the banner at the top shows the mode).
- **[ ]**: lower/raise mouse sensitivity (saved).
- **Esc**: releases the mouse (the browser reserves Esc for that). **F8**: turns everything on/off.

The Xbox app version ([`gta6-mouse-app`](../gta6-mouse-app)) is more complete: it has an aircraft mode,
Esc as pause and deadzone tuning.

## Tips
- In GTA 6, raise the camera sensitivity and lower the right stick deadzone.
- To change keys, edit `MAP_A_PE` and `MAP_VEICULO` at the top of `inject.js`
  and click **Reload** in `edge://extensions`.
- To test without the game, serve this folder from a local web server and open `teste.html`.

## Warning
In online modes, a mouse "disguised" as a controller may be considered cheating (like XIM/Cronus)
and could get you banned. The risk is much lower in story mode.
