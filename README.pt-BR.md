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
| WASD | mover-se (Caps Lock = andar devagar) | L |
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
- **Mouse:** coloque a **taxa de relatório (polling rate) em 1000 Hz** no software do mouse (ex.: Logitech G HUB >
  Sensibilidade (DPI) > Taxa de relatório). Não é o DPI; o DPI só muda a sensibilidade.
- **Rede:** PC e console no cabo (ou Wi-Fi 5 GHz), na mesma rede, NAT aberto.
- **No código** (`gta_mouse.py`): `JANELA_MS` (suavidade da câmera), `CURVA`, `TAXA_HZ` e os mapas de teclas ficam no topo.

O próprio programa adiciona menos de 0,1 ms entre o mouse e o controle virtual (medido); o atraso
que sobra vem do streaming do Remote Play (codificação do vídeo e rede).

## Problemas comuns
| Problema | Solução |
|---|---|
| `ModuleNotFoundError: No module named 'vgamepad'` | Rode `pip install -r requirements.txt` num terminal normal (o mesmo Python que abre o `INICIAR.bat`). |
| "Não consegui criar o controle virtual" | Instale o driver ViGEmBus (veja Instalação) e reinicie o PC. |
| App Xbox: *"Encontramos seu console, mas não é possível conectá-lo"* | PC e console precisam estar na **mesma rede** (mesmo roteador, mesma faixa de IP, ex.: os dois em `192.168.1.x`). Um mesh/segundo roteador cria outra rede. Coloque também o perfil de rede do PC como **Privada** (Configurações > Rede e Internet > Ethernet). |
| Remote Play com tela preta | Em PCs com duas placas de vídeo, coloque o app Xbox na placa dedicada (Configurações > Sistema > Tela > Elementos gráficos) e desligue o HDR. |
| Câmera lenta | Aumente a sensibilidade com **=**, coloque a sensibilidade da câmera no máximo no GTA 6 e diminua a zona morta do jogo. |
| Câmera continua andando depois de parar o mouse | Diminua a zona morta com **9**. |
| Câmera travada / engasgando | Aumente `JANELA_MS` (ex.: 24) no começo do `gta_mouse.py`; confira se o mouse está em 1000 Hz. |
| Nada acontece no jogo | O programa só age com a janela cujo título começa com **XBOX** em foco. Clique na janela do app Xbox; a janela preta deve mostrar ATIVO. |
| O cursor do Windows sumiu | Abra o `INICIAR.bat` de novo (ele restaura o cursor ao iniciar) ou rode `python gta_mouse.py --mostrar-cursor`. |
| Controle de verdade atrapalhando | Desligue ou desconecte o controle enquanto usa o programa. |

## Créditos
- Controle virtual: [ViGEmBus](https://github.com/nefarius/ViGEmBus) via [vgamepad](https://github.com/yannbouteiller/vgamepad)
- Teclado e mouse: [pynput](https://github.com/moses-palmer/pynput)

Projeto independente, sem ligação com Rockstar Games, Take-Two ou Microsoft.
