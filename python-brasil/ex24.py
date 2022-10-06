# Faça um programa que calcule e mostre a média aritmética de N notas. 
from functools import reduce

n = int(input('Quantas notas quer usar para obter a media aritmetica? '))

notas = []
x = 0

for i in range(0, n):
    nota = float(input('Nota: '))
    notas.append(nota)
    x += 1 
soma = reduce(lambda ac, p: ac + p, notas)
media = soma / len(notas)
print("MEDIA ARITMETICA SIMPLES =", media)