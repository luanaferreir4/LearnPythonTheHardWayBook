from resultado import *


def notas(first, second):
    soma = first + second
    if soma < 60:
        print(soma, "- REPROVADO!")
    else:
        print(soma, "- APROVADO!")
    return soma


resultado(notas(45.5, 31.3))
resultado(notas(34.0, 23.5))
