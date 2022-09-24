# Problema "numeros_pares" 
# Faça um programa que leia N números inteiros e armazene-os em um vetor. Em seguida, mostre na 
# tela todos os números pares, e também a quantidade de números pares. 
# Exemplo: 
# Quantos numeros voce vai digitar? 6
# Digite um numero: 8
# Digite um numero: 2
# Digite um numero: 11
# Digite um numero: 14
# Digite um numero: 13
# Digite um numero: 20
# NUMEROS PARES: 
# 8 2 14 20 
# QUANTIDADE DE PARES = 4 

n = int(input("Quantos numeros voce vai digitar? "))

numeros_pares = []

for i in range(0, n):
    numero = int(input("Digite um numero: "))
    if (numero % 2) == 0:
        numeros_pares.append(numero)
print("NUMEROS PARES:", numeros_pares)
print("QUANTIDADE DE PARES:", len(numeros_pares))
