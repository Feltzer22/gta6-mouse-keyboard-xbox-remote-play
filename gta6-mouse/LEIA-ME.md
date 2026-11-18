# GTA 6 Mouse — mouse e teclado no Xbox Remote Play (navegador)

Extensão simples para o Edge/Chrome. Ela faz a página do Remote Play (xbox.com)
achar que tem um controle de Xbox conectado, e esse controle é o seu mouse e teclado.

## Instalar (Edge)
1. Abra `edge://extensions`.
2. Ligue **Modo de desenvolvedor** (canto inferior esquerdo).
3. Clique em **Carregar sem pacote** e escolha esta pasta `gta6-mouse`.
4. Abra **https://www.xbox.com/remoteplay** (vai para play.xbox.com), entre na conta, conecte no seu Xbox e abra o GTA 6.
5. **Desconecte o controle de verdade** (senão os dois brigam).
6. Clique na tela do jogo: o mouse trava e o aviso no topo fica verde.

## Teclas
| Tecla | A pé | Veículo (aperte V) |
|---|---|---|
| WASD | andar | W acelera, S freia/ré, A/D vira |
| Mouse | câmera / mira | câmera |
| Botão esquerdo | atirar (RT) | atirar (RB) |
| Botão direito | mirar (LT) | — (LT) |
| Shift | correr (L3) | buzina/nitro (L3) |
| Espaço | pular (A) | freio de mão (A) |
| C / Ctrl | agachar (B) | faróis (B) |
| F | corpo a corpo (X) | sair (Y) |
| E | interagir / entrar (Y) | sair (Y) |
| Q | cobertura (RB) | — |
| Tab | guardar / equipamento (LB) | LB |
| Z / botão do meio | olhar para trás (R3) | olhar para trás |
| Rodinha | trocar arma (Y) | — |
| T / setas / 1-4 | direcional (celular, rádio...) | direcional |
| M | mapa (View) | mapa |
| Enter / P | pausa (Menu) | pausa |

- **V**: troca entre A PÉ e VEÍCULO (o aviso no topo mostra o modo).
- **[ ]**: diminui/aumenta a sensibilidade do mouse (fica salva).
- **Esc**: solta o mouse. **F8**: liga/desliga tudo.

## Dicas
- No GTA 6, aumente a sensibilidade da câmera e diminua a zona morta do analógico direito.
- Para mudar teclas, edite `MAP_A_PE` e `MAP_VEICULO` no começo do `inject.js`
  e clique em **Recarregar** em `edge://extensions`.
- Para testar sem o jogo: com o servidor de teste ligado, abra `teste.html`.

## Aviso
No online, usar mouse "disfarçado" de controle pode ser visto como trapaça (igual XIM/Cronus)
e pode dar banimento. No modo história o risco é bem menor.
