from die import *
from win import *


def sala_dourada():
    print("Você está numa sala cheia de ouro. \n Quanto $$$ você pegaria dessa sala cheia de ouro?", end=' ')

    quanto = int(input())

    if quanto > 1000:
        die("Seu bastardo ganancioso, ficou sem dinheiro e sem vida!")
    else:
        win("Alcançou o paraíso por sua humildade!")

