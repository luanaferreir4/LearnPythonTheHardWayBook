class Musica(object):

    def __init__(self, letras):
        self.letras = letras

    def cante_uma_musica(self):
        for linha in self.letras:
            print(linha)


parabens = Musica(["Parabens pra voce", "Nesta data querida", "Muitas felicidades e muitos anos de vida"])

bulls_on_parade = Musica(["They rally around tha family", "With pockets"])

old_town_road = Musica(["I'm gonna take my horse", "Living like a rockstar"])

parabens.cante_uma_musica()
bulls_on_parade.cante_uma_musica()
old_town_road.cante_uma_musica()
