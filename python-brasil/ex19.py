# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

from functools import reduce

valores = []

n = int(input('Quantos numeros quer comparar? '))

if n < 0 or n > 1000:
    print('Aceitamos apenas numeros entre 0 e 1000! Tente novamente!')
    exit(0)
else:
    for i in range(0, n):
        numeros = float(input('Numero: '))
        valores.append(numeros)

maior = max(valores)
menor = min(valores)

print("MAIOR =", maior, "\nMENOR =", menor)

soma = reduce(lambda ac, p: ac + p, valores)

print("SOMA DOS VALORES =", soma)

