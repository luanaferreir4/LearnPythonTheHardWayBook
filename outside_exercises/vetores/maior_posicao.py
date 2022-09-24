# Problema "maior_posicao" 
# Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida, mostrar na tela 
# o maior número do vetor (supor não haver empates). Mostrar também a posição do maior elemento, 
# considerando a primeira posição como 0 (zero). 
# Exemplo: 
# Quanto numeros voce vai digitar? 6
# Digite um numero: 8.0
# Digite um numero: 4.0
# Digite um numero: 10.0
# Digite um numero: 14.0
# Digite um numero: 13.0
# Digite um numero: 7.0
# MAIOR VALOR = 14.0 
# POSICAO DO MAIOR VALOR = 3 


from functools import reduce


n = int(input("Quanto numeros voce vai digitar? "))

numeros = []

for i in range(0, n):
    numero = float(input("Digite um numero: "))
    numeros.append(numero)
    
    
max_numero = max(numeros)
print("MAIOR VALOR =", max_numero)

maior_posicao = numeros.index(max_numero)
print("POSICAO DO MAIOR VALOR =", maior_posicao)

  