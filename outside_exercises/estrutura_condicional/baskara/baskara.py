import math


def bhaskara(coefa, coefb, coefc):
    delta = pow(coefb, 2) - 4 * coefa * coefc
    if delta < 0:
        erro = "Esta equacao nao possui raizes reais"
        print(erro)
        return None, None
    else:
        x1 = (-coefb + math.sqrt(delta)) / (2 * coefa)
        x2 = (-coefb - math.sqrt(delta)) / (2 * coefa)
        return x1, x2


def resultado(coefa, coefb, coefc):
    x1, x2 = bhaskara(coefa, coefb, coefc)
    print(f"X1: {x1:.4f}")
    print(f"X2: {x2:.4f}")
    return x1, x2


resultado(1, 0, -9)
resultado(2, -4.5, 1.7)
resultado(1, 3, 4)
