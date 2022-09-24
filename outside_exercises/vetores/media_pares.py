# Problema "media_pares " 
# Fazer um programa para ler um vetor de N números inteiros. Em seguida, mostrar na tela a média 
# aritmética somente dos números pares lidos, com uma casa decimal. Se nenhum número par for 
# digitado, mostrar a mensagem "NENHUM NUMERO PAR" 
# Exemplo 1: 
# Quantos elementos vai ter o vetor? 6
# Digite um numero: 8 
# Digite um numero: 2 
# Digite um numero: 11 
# Digite um numero: 14 
# Digite um numero: 13 
# Digite um numero: 20
# MEDIA DOS PARES = 11.0 
# Exemplo 2: 
# Quantos elementos vai ter o vetor? 3
# Digite um numero: 7 
# Digite um numero: 9 
# Digite um numero: 11 
# NENHUM NUMERO PAR 

from functools import reduce

n = int(input("Quantos elementos vai ter o vetor? "))

numeros_pares = []

for i in range(0, n):
    numero = int(input("Digite um numero: "))
    if (numero % 2) == 0:
        numeros_pares.append(numero)
        
if len(numeros_pares) == 0:
    print("NENHUM NUMERO PAR")
else:                
    soma = reduce(lambda ac, valor: ac + valor, numeros_pares, 0)
    media_pares = soma / len(numeros_pares)
    print("MEDIA DOS PARES =", media_pares)

