# Um loop while é executado até que a expressão seja False.


def debugger(incremento):

    numeros = []
    maximo = 10

    for i in range(0, maximo, incremento):
        print(f"No topo i é {i}")
        numeros.append(i)

        print("numeros agora:", numeros)
        print(f"No fundo i é {i}")

    print("Os números")

    for numero in numeros:
        print(numero)

    return numeros


def debugger2(incremento):

    i = 0
    numeros = []
    maximo = 10

    while i < maximo:
        print(f"No topo i é {i}")
        numeros.append(i)

        i += incremento
        print("numeros agora:", numeros)
        print(f"No fundo i é {i}")

    print("Os números")

    for numero in numeros:
        print(numero)

    return numeros
