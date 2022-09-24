# Se eu fosse criar uma classe como o módulo minha_coisa, faria algo assim:


class MinhaCoisa(object):

    def __init__(self):
        self.tangerina = "Aqui temos uma fruta madurinha!"

    def maca(self):
        print('Eu sou uma maçã')


coisa = MinhaCoisa()
coisa.maca()
print(coisa.tangerina)
