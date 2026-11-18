# GTA 6 Mouse — mouse e teclado no app Xbox (Remote Play)

🌐 [English](README.md) · **Português**

Cria um controle de Xbox virtual no Windows (driver ViGEmBus) e transforma mouse e
teclado nesse controle. Só age com a janela do **app Xbox** em primeiro plano.

## Como usar
1. Desligue o controle de verdade.
2. Dois cliques em **INICIAR.bat** e deixe a janela preta aberta.
3. Abra o Remote Play no app Xbox e clique na janela dele: bipe, o cursor some e o mouse vira a câmera.
4. **F8** pausa (mouse normal de volta). Alt+Tab também solta.

Se o cursor do Windows sumir e não voltar (programa fechado à força), rode:
`python gta_mouse.py --mostrar-cursor` ou simplesmente abra o INICIAR.bat de novo.

## Modos
- **V**: A PÉ ↔ VEÍCULO (carro, moto, barco, bicicleta)
- **N**: A PÉ ↔ AERONAVE
- **- / =**: diminui / aumenta a sensibilidade do mouse
- **9 / 0**: diminui / aumenta a zona morta. Os dois ficam salvos em `ajustes.txt`.

## A pé (também natação, luta e paraquedas)
| Tecla | Ação no GTA 6 | Controle |
|---|---|---|
| WASD | andar | analógico esq. |
| Caps Lock | liga/desliga andar devagar (analógico a 50%) | analógico esq. |
| Mouse | câmera / mira | analógico dir. |
| Botão esquerdo | atirar · luta: agarrar | RT |
| Botão direito | mirar / interagir · luta: travar alvo | LT |
| Shift | correr · nadar mais rápido | L3 |
| Espaço | pular / escalar · bloquear/esquivar · subir à superfície · abrir paraquedas | A |
| C / Ctrl | agachar (segurar = descansar) | B |
| F | soco / chute | X |
| E / rodinha / mouse 5 | interagir, entrar no veículo · mirando: trocar arma | Y |
| Tab / mouse 4 | guardar arma (segurar = equipamento) | LB |
| Q | cobertura · mergulhar | RB |
| G | arremesso rápido (segure mirando) | RB |
| Z / botão do meio | olhar / zoom (segurar = olhar para trás) | R3 |
| T / ↑ / 1 | celular (segurar = app Waink) · mirando: aproximar | direcional ↑ |
| O / ↓ / 2 | objetivo / minimapa (segurar = navegação rápida) · mirando: afastar | direcional ↓ |
| X / ← / 3 | rádio · mirando (segurar): trocar de ombro | direcional ← |
| K / → / 4 | detonar explosivos (segurar = menu do parceiro) | direcional → |
| M | mapa | View |
| Esc / P | pausa / configurações (em todos os modos) | Menu |
| Enter | confirmar nos menus (em todos os modos) | A |
| Backspace | voltar nos menus (em todos os modos) | B |

**Paraquedas** (use o modo A PÉ): Espaço abre (A), E solta (Y), botão direito / esquerdo
freiam à esquerda / direita (LT / RT), Q atira (RB).

## Veículo (aperte V) — carros, motos, barcos e bicicletas
| Tecla | Ação | Controle |
|---|---|---|
| W / S | acelerar / frear e ré (bike: pedalar) | RT / LT |
| A / D | virar | analógico esq. |
| Espaço | freio de mão (bike: corrida) | A |
| Botão esquerdo | atirar do veículo | RB |
| E | sair do veículo / bicicleta | Y |
| F | corpo a corpo | X |
| C | farol (segurar = abaixar-se · bike: pulo) | B |
| Shift / H | buzina / nitro (bike: campainha) | L3 |
| Q / R | seta esquerda / direita (segurar = menu do veículo / parceiro) | direcional ← / → |
| T / O | celular / objetivo | direcional ↑ / ↓ |
| Z | olhar para trás | R3 |

A rodinha e o botão lateral 5 não fazem nada no veículo e na aeronave, para você não sair sem querer.

## Aeronave (aperte N)
| Tecla | Ação | Controle |
|---|---|---|
| W / S | arfagem (bico para baixo / cima) | analógico esq. |
| A / D | rolagem | analógico esq. |
| Shift / Ctrl | mais / menos motor | RT / LT |
| Q / E | guinada esquerda / direita | X / B |
| G | trem de pouso | L3 |
| F | sair | Y |
| Botão esquerdo | atirar | RB |

## Para ficar mais rápido e preciso
**No GTA 6** (Configurações > Controles):
- Sensibilidade da câmera e da mira: no máximo, ou perto disso.
- Aceleração da mira/câmera: no mínimo ou desligada (se existir).
- Zona morta do analógico direito: no mínimo.
- Se a câmera "puxar" sozinha quando você para o mouse, diminua a zona morta aqui com **9**.
- Se movimentos pequenos do mouse não mexem a câmera, aumente com **0**.

**No Windows:** Configurações > Bluetooth e dispositivos > Mouse > Configurações adicionais >
Opções de ponteiro > desmarque **Aprimorar precisão do ponteiro**. A mira fica igual
independente da velocidade da mão.

**No programa** (começo do `gta_mouse.py`): `JANELA_MS` maior = câmera mais lisa, menor = mais crua
(padrão 16 ms); `SUAVIZACAO_MS` = filtro extra; `CURVA` menor = movimentos pequenos mais fortes.
O próprio programa leva menos de 0,1 ms entre o mouse e o controle virtual; o atraso que sobra
vem do streaming (vídeo e rede). As mensagens seguem o idioma do Windows
(português ou inglês); use `IDIOMA = "pt"` para forçar português.

**Rede:** console e PC no cabo do roteador (ou Wi-Fi 5 GHz), na mesma rede, nada baixando enquanto joga.

## Aviso
No online, mouse "disfarçado" de controle pode ser visto como trapaça (igual XIM/Cronus)
e pode dar banimento. No modo história o risco é bem menor.
