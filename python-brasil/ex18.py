# Faça um programa que, dado um conjunto de N números, determine o menor valor,
# o maior valor e a soma dos valores.

from functools import reduce

n = int(input('Quantos numeros quer comparar? '))
valores = []

for i in range(0, n):
    numeros = float(input('Numero: '))
    valores.append(numeros)

maior = max(valores)
menor = min(valores)

print("MAIOR =", maior, "\nMENOR =", menor)

soma = reduce(lambda ac, p: ac + p, valores)

print("SOMA DOS VALORES =", soma)

