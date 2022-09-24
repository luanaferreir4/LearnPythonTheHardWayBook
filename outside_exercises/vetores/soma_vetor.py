# Problema "soma_vetor"
# Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida:
# - Imprimir todos os elementos do vetor
# - Mostrar na tela a soma e a média dos elementos do vetor
# Exemplo:
# Quantos numeros voce vai digitar? 4
# Digite um numero: 8.0
# Digite um numero: 4.0
# Digite um numero: 10.0
# Digite um numero: 14.0
# VALORES = 8.0 4.0 10.0 14.0
# SOMA = 36.00
# MEDIA = 9.00

from functools import reduce

numeros = []

n = int(input('Quantos números você vai digitar? '))
for i in range(0, n):
    numero = float(input('Digite um número: '))
    numeros.append(numero)

print('VALORES =', numeros)

soma = reduce(lambda ac, valor_atual: ac + valor_atual, numeros, 0)
print("SOMA =", soma)

media = soma / len(numeros)
print("MEDIA =", media)
