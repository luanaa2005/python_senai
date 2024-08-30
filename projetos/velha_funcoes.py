from os import system

tabuleiro = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def desenhar_tabuleiro():
    system('clear')
    for indice, i in enumerate(tabuleiro):
        if indice == 2 or indice == 5 or indice == 8:
            print(i)
        else:
            print(i, end = ' | ')

def jogar(jogada, jogador):
    tabuleiro[jogada] = jogador

def troca_jogador(jogador):
    jogador2 = jogador
    if jogador2 == 'X':
        jogador2 = 'O'
    else:
        jogador2 = 'X'
    return jogador2

def verifica_vitoria():
    if (tabuleiro[0] == tabuleiro[1] == tabuleiro[2] or
       tabuleiro[3] == tabuleiro[4] == tabuleiro[5] or
       tabuleiro[6] == tabuleiro[7] == tabuleiro[8]):
       return True
    elif (tabuleiro[0] == tabuleiro[3] == tabuleiro[6] or
         tabuleiro[1] == tabuleiro[4] == tabuleiro[7] or
         tabuleiro[2] == tabuleiro[5] == tabuleiro[8]):
       return True
    elif (tabuleiro[0] == tabuleiro[4] == tabuleiro[8] or
         tabuleiro[2] == tabuleiro[4] == tabuleiro[6]):
       return True
    else:
        return False

    