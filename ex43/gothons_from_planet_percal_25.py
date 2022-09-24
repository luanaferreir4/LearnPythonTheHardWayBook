from sys import exit
from random import randint
from textwrap import dedent


class Cena(object):

    def enter(self):
        pass


class Mecanismo(object):

    def __init__(self, mapa_cenografico):
        pass

    def jogar(self):
        pass


class Morte(Cena):

    def enter(self):
        pass


class CorredorCentral(Cena):

    def enter(self):
        pass


class ArsenalDeArmasLaser(Cena):

    def enter(self):
        pass


class APonte(Cena):

    def enter(self):
        pass


class CapsulaDeEscape(Cena):

    def enter(self):
        pass


class Mapa(object):

    def __init__(self, cena_inicial):
        pass

    def proxima_cena(self, nome_da_cena):
        pass

    def cena_de_abertura(self):
        pass


um_mapa = Mapa('corredor_central')
um_jogo = Mecanismo(um_mapa)
um_jogo.jogar()