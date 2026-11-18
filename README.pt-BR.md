# GTA 6 com mouse e teclado no Xbox Remote Play (PC)

🌐 [English](README.md) · **Português**

Jogue **GTA 6 no seu Xbox** usando **mouse e teclado no PC**, pelo Remote Play do **app Xbox para Windows**.
O jogo continua rodando no console; este programa transforma mouse e teclado em um controle de Xbox virtual.

Todas as ações do esquema padrão de controle do GTA 6 estão mapeadas: a pé, mira,
corpo a corpo, natação, paraquedas, veículos terrestres/aquáticos, bicicletas e aeronaves.

> ⚠️ **Aviso:** no online, usar mouse "disfarçado" de controle pode ser visto como trapaça
> (como XIM/Cronus) e pode dar banimento. No modo história o risco é bem menor. Use por sua conta.

## Recursos
- Controle de Xbox 360 virtual (ViGEmBus): o app Xbox enxerga um controle normal
- Só age com a janela do app Xbox em foco; Alt+Tab devolve o mouse normal
- Cursor escondido durante o jogo, 500 atualizações por segundo, sensibilidade e zona morta ajustáveis na hora
- Três modos: a pé, veículo e aeronave, seguindo os controles oficiais do GTA 6
- Mensagens em português ou inglês (segue o idioma do Windows)

## Requisitos
- Windows 10/11 64 bits
- [Python 3](https://www.python.org/downloads/) (marque "Add Python to PATH" na instalação)
- Driver **ViGEmBus** (o instalador vem junto com a biblioteca `vgamepad`)
- Xbox com **Recursos remotos** ligados e na mesma rede do PC

## Instalação
```powershell
pip install -r requirements.txt
```
Se o driver ViGEmBus não for instalado automaticamente, rode o instalador que fica em
`...\site-packages\vgamepad\win\vigem\install\x64\ViGEmBusSetup_x64.msi`.

## Uso
1. Desligue o controle de verdade.
2. Dê dois cliques em **`gta6-mouse-app/INICIAR.bat`** e deixe a janela aberta.
3. No app Xbox, abra o Remote Play do seu console e o GTA 6.
4. Clique na janela do app Xbox: toca um bipe, o cursor some e o mouse vira a câmera.
5. **F8** liga/desliga (mouse normal de volta). Alt+Tab também solta.

## Modos e ajustes
| Tecla | Função |
|---|---|
| **V** | A PÉ ↔ VEÍCULO (carro, moto, barco, bicicleta) |
| **N** | A PÉ ↔ AERONAVE |
| **- / =** | diminui / aumenta a sensibilidade do mouse |
| **9 / 0** | diminui / aumenta a zona morta |
| **F8** | liga / desliga |

A tabela completa de teclas de todos os modos está em [`gta6-mouse-app/LEIA-ME.md`](gta6-mouse-app/LEIA-ME.md).

## Teclas principais (a pé)
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

## Dicas para menos atraso
- **No GTA 6:** sensibilidade da câmera e da mira no máximo, aceleração no mínimo, zona morta no mínimo.
- **No Windows:** desmarque *Aprimorar precisão do ponteiro* (Mouse > Opções de ponteiro).
- **Rede:** PC e console no cabo (ou Wi-Fi 5 GHz), na mesma rede, NAT aberto.
- **No código** (`gta_mouse.py`): `SUAVIZACAO_MS`, `CURVA`, `TAXA_HZ` e os mapas de teclas ficam no topo.

## Créditos
- Controle virtual: [ViGEmBus](https://github.com/nefarius/ViGEmBus) via [vgamepad](https://github.com/yannbouteiller/vgamepad)
- Teclado e mouse: [pynput](https://github.com/moses-palmer/pynput)

Projeto independente, sem ligação com Rockstar Games, Take-Two ou Microsoft.
