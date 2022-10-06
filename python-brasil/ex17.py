# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
# Ex.: 5!=5.4.3.2.1=120

from functools import reduce

n = int(input('Quer calcular o fatorial de qual numero? '))

fatorial = []

for i in range(n, 0, -1):
    fatorial.append(i)
reduce = reduce(lambda ac, p: p * ac, fatorial)
print('*', fatorial, '=', f'{reduce:.2f}')
