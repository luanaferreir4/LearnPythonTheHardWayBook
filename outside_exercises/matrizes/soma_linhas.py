# Problema "soma_linhas" 
# Fazer um programa para ler dois números inteiros M e N (máximo = 10). Em seguida, ler uma matriz 
# de M linhas e N colunas contendo números reais. Gerar um vetor de modo que cada elemento do vetor 
# seja a soma dos elementos da linha correspondente da matriz. Mostrar o vetor gerado. 
# Exemplo: 
# Qual a quantidade de linhas da matriz? 2 
# Qual a quantidade de colunas da matriz? 3
# Digite os elementos da 1a. linha: 
# 7.0 
# 8.0 
# 10.0 
# Digite os elementos da 2a. linha: 
# 2.0 
# 3.0 
# 5.0 
# VETOR GERADO: 
# 25.0 
# 10.0 

from functools import reduce

m = int(input('Qual a quantidade de linhas da matriz? '))
n = int(input('Qual a quantidade de colunas da matriz? '))

if m > 10 and n > 10:
    print('O máximo que podemos fazer é uma matriz 10x10!\n Digite novamente!')
else:

    matriz = []

    for i in range(0, m):
        linha = []
        print(f'Digite os elementos da {i+1}a linha:')
        for j in range(0, n):
            elemento = float(input())
            linha.append(elemento)
        matriz.append(linha)

print("VETOR GERADO:")
for linha in matriz:
    soma_linha = reduce(lambda ac, p: ac + p, linha)
    print(soma_linha)

    