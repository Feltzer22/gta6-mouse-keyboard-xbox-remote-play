# GTA 6 — todas as teclas para mouse e teclado (Xbox Remote Play)

🌐 [English](README.md) · **Português**

Jogue **GTA 6 no seu Xbox** usando **mouse e teclado no PC**, pelo Remote Play.
O jogo continua rodando no console; o PC transforma mouse e teclado em um controle de Xbox.

Todas as ações do esquema padrão de controle do GTA 6 estão mapeadas: a pé, mira,
corpo a corpo, natação, paraquedas, veículos, bicicletas e aeronaves.

> ⚠️ **Aviso:** no online, usar mouse "disfarçado" de controle pode ser visto como trapaça
> (como XIM/Cronus) e pode dar banimento. No modo história o risco é bem menor. Use por sua conta.

## Duas versões

| Pasta | Funciona em | Como funciona |
|---|---|---|
| [`gta6-mouse-app/`](gta6-mouse-app) | **App Xbox** no Windows | Programa em Python que cria um controle de Xbox 360 virtual (driver ViGEmBus) |
| [`gta6-mouse/`](gta6-mouse) | Remote Play **no navegador** (xbox.com/remoteplay) | Extensão do Edge/Chrome que finge ser um controle na página |

---

## Versão para o app Xbox (recomendada)

### Requisitos
- Windows 10/11 64 bits
- [Python 3](https://www.python.org/downloads/) (marque "Add Python to PATH" na instalação)
- Driver **ViGEmBus** (o instalador vem junto com a biblioteca `vgamepad`)
- Xbox com **Recursos remotos** ligados e na mesma rede do PC

### Instalação
```powershell
pip install -r requirements.txt
```
Se o driver ViGEmBus não for instalado automaticamente, rode o instalador que fica em
`...\site-packages\vgamepad\win\vigem\install\x64\ViGEmBusSetup_x64.msi`.

### Uso
1. Desligue o controle de verdade.
2. Dê dois cliques em **`gta6-mouse-app/INICIAR.bat`** e deixe a janela aberta.
3. No app Xbox, abra o Remote Play do seu console e o GTA 6.
4. Clique na janela do app Xbox: toca um bipe, o cursor some e o mouse vira a câmera.
5. **F8** liga/desliga (mouse normal de volta). Alt+Tab também solta.

### Modos e ajustes
| Tecla | Função |
|---|---|
| **V** | A PÉ ↔ VEÍCULO (carro, moto, barco, bicicleta) |
| **N** | A PÉ ↔ AERONAVE |
| **- / =** | diminui / aumenta a sensibilidade do mouse |
| **9 / 0** | diminui / aumenta a zona morta |
| **F8** | liga / desliga |

A tabela completa de teclas está em [`gta6-mouse-app/LEIA-ME.md`](gta6-mouse-app/LEIA-ME.md).
O programa mostra as mensagens em português quando o Windows está em português, e em inglês nos outros idiomas.

### Teclas principais (a pé)
| Tecla | Ação | Controle |
|---|---|---|
| WASD | mover-se | L |
| Mouse | olhar / mirar | R |
| Botão esquerdo / direito | atirar / mirar | RT / LT |
| Shift | correr | L3 |
| Espaço | pular / escalar | A |
| C | agachar (segurar = descansar) | B |
| F | corpo a corpo | X |
| E | interagir / entrar no veículo | Y |
| Q | proteger-se | RB |
| Tab | sacar/guardar arma (segurar = inventário) | LB |
| Z | olhar para trás | R3 |
| T / O / X / K | celular / objetivo / rádio / detonar | direcional |
| M | mapa | View |
| Esc | pausar | Menu |
| Enter / Backspace | confirmar / voltar nos menus | A / B |

### Dicas para menos atraso
- **No GTA 6:** sensibilidade da câmera e da mira no máximo, aceleração no mínimo, zona morta no mínimo.
- **No Windows:** desmarque *Aprimorar precisão do ponteiro* (Mouse > Opções de ponteiro).
- **Rede:** PC e console no cabo (ou Wi-Fi 5 GHz), na mesma rede, NAT aberto.
- **No código** (`gta_mouse.py`): `SUAVIZACAO_MS`, `CURVA`, `TAXA_HZ` e os mapas de teclas ficam no topo.

---

## Versão para o navegador

1. Abra `edge://extensions`, ligue **Modo de desenvolvedor** e clique em **Carregar sem pacote**.
2. Escolha a pasta [`gta6-mouse/`](gta6-mouse).
3. Abra **https://www.xbox.com/remoteplay**, conecte no console e clique na tela do jogo.

Detalhes em [`gta6-mouse/LEIA-ME.md`](gta6-mouse/LEIA-ME.md).

---

## Créditos
- Controle virtual: [ViGEmBus](https://github.com/nefarius/ViGEmBus) via [vgamepad](https://github.com/yannbouteiller/vgamepad)
- Teclado e mouse: [pynput](https://github.com/moses-palmer/pynput)
- Ideia da versão de navegador inspirada no [Better xCloud](https://github.com/redphx/better-xcloud)

Projeto independente, sem ligação com Rockstar Games, Take-Two ou Microsoft.
