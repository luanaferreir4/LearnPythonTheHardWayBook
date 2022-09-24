# Exercícios de Frases

# cria uma classe **X** que é-um **Y**.
class X(Y)
# A classe **X** tem-um __init__ que recebe os parâmetros self e J.
class X(object):
    def __init__(self, J):
# A classe **X** tem-uma função chamada M, que recebe os parâmetros self e J
class X(object):
    def M(self, J):
# Define foo como uma instancia da classe X
foo = X()
# A partir de foo, obtém a função M e chama-a com os parâmetros self, J
foo.M(J)
# A partir de foo, obtém o atributo K e define-o como Q
foo.K = Q

