# Animal é um object (sim, é meio confuso), veja o crédito extra
class Animal(object):

    def apresentacao(self, tipo):
        print(f"Sou um {tipo}")


## Herdou de Animal (herança)
class Cachorro(Animal):

    def __init__(self, nome):
        # atributo nome de Dog
        self.nome = nome


class Gato(Animal):

    def __init__(self, nome):
        self.nome = nome


class Pessoa(object):

    def __init__(self, nome):
        self.nome = nome
        # Pessoa tem-um pet de algum tipo
        self.pet = None


class Empregado(Pessoa):

    def __init__(self, nome, salario):
        # pegar atributos de uma classe maior usando "super(NomeDaClasse, self).__init__(atributo)"
        super(Empregado, self).__init__(nome)
        self.salario = salario


class Peixe(object):
    pass


class Salmao(Peixe):
    pass


class Halibut(Peixe):
    pass


# rover é-um Cachorro
rover = Cachorro("Rover")

# satan é-um Gato
satan = Gato("Satan")

# mary é-uma Pessoa
mary = Pessoa("Mary")

# colocando o nome do pet de Mary que estava indefinido
mary.pet = satan

# empregado frank e seu salario
frank = Empregado("Frank", "120000")

# Pet de Frank é o cão rover
frank.pet = rover

# flipper é-um peixe
flipper = Peixe()

# crouse é-um Salmao
crouse = Salmao()

# harry é-um halibut q é um peixe
harry = Halibut()

animal = Animal()
animal.apresentacao("Gato")
halibut = Halibut()
halibut.nome = 'Alfafa'
halibut.idade = 10
print(halibut.idade)

# O que super(Empregado, self).__init__(name) faz?
#
# É como você pode executar o método __init__ de uma classe-mãe com segurança.
