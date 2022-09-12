from die import *
from paraiso import *
from sala_dourada import *


def comecar():
    print('Você acorda diante de um recinto desconhecido onde a sua frente há 2 portas e mais nenhum lugar para ir.'
          'Qual das portas você entraria?', end=' ')

    porta = input()

    if porta == "1":
        sala_dourada()
    elif porta == "2":
        paraiso()
    else:
        die("Você cai no mundo dos fantasmas para sempre e agora a sua mente é perturbada!")
