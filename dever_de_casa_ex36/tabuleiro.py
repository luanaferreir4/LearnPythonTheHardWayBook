from util import die
from sys import exit

tabuleiro = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]


def comecar(x, y, peca):
    if x >= 3 or y >= 3:
        die("Posição inválida! (> 2)")
    elif x < 0 or y < 0:
        die("Posição inválida! (< 0)")
    elif type(x) != int or type(y) != int:
        die("Valor não reconhecido! (needs integer)")
    elif tabuleiro[x][y] != ' ':
        die("Local já ocupado, escolha outro lugar desocupado ou reinicie o jogo!")
        exit(1)
    elif peca.upper() != 'X' and peca.upper() != 'O':
        die("Peça não reconhecida! Escolha 'X' ou 'O'")
    else:
        tabuleiro[x][y] = peca.upper()
        return tabuleiro


def print_tabuleiro():
    print(tabuleiro[0])
    print(tabuleiro[1])
    print(tabuleiro[2])


# def jogador_venceu(peca):
#     if peca.upper() != 'X' and peca.upper() != 'O':
#         die("Peça não reconhecida! Escolha 'X' ou 'O'")


comecar(0, 0, 'X')
comecar(1, 1, 'X')
comecar(1, 2, 'O')

print_tabuleiro()
