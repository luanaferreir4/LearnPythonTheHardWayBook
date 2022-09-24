# Problema "abaixo_da_media" 
# Fazer um programa para ler um número inteiro N e depois um vetor de N números reais. Em seguida, 
# mostrar na tela a média aritmética de todos elementos com três casas decimais. Depois mostrar todos 
# os elementos do vetor que estejam abaixo da média, com uma casa decimal cada. 
# Exemplo: 
# Quantos elementos vai ter o vetor? 4
# Digite um numero: 10.0
# Digite um numero: 15.5
# Digite um numero: 13.2
# Digite um numero: 9.8
# MEDIA DO VETOR = 12.125 
# ELEMENTOS ABAIXO DA MEDIA: 
# 10.0 
# 9.8 

from functools import reduce

n = int(input("Quantos elementos vai ter o vetor? "))

numeros = []

for i in range(0, n):
    numero = float(input("Digite um numero: "))
    numeros.append(numero)

soma = 0

for numero in numeros:
    soma += numero
    media_do_vetor = soma / len(numeros)
print("MEDIA DO VETOR =", media_do_vetor)


print("ELEMENTOS ABAIXO DA MEDIA:")
for numero in numeros:
    if numero < media_do_vetor:
        print(numero)