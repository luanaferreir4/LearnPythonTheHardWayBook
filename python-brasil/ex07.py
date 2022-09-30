# Faça um programa que leia 5 números e informe o maior número.

numeros = []

for i in range(0, 5):
    numero = float(input())
    numeros.append(numero)
maior = max(numeros)
print("Maior numero:", maior)
