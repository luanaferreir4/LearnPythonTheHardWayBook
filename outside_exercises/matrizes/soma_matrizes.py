# Problema "soma_matrizes"
# Fazer um programa para ler duas matrizes de números inteiros A e B, contendo de M linhas e N colunas
# cada (M e N máximo = 10). Depois, gerar uma terceira matriz C onde cada elemento desta é a soma
# dos elementos correspondentes das matrizes originais. Imprimir na tela a matriz gerada.
# Exemplo:
# Quantas linhas vai ter cada matriz? 2
# Quantas colunas vai ter cada matriz? 3
# Digite os valores da matriz A:
# Elemento [0,0]: 3
# Elemento [0,1]: 5
# Elemento [0,2]: 2
# Elemento [1,0]: 4
# Elemento [1,1]: 5
# Elemento [1,2]: 1
# Digite os valores da matriz B:
# Elemento [0,0]: 2
# Elemento [0,1]: 4
# Elemento [0,2]: 5
# Elemento [1,0]: 1
# Elemento [1,1]: 8
# Elemento [1,2]: 8
# MATRIZ SOMA:
# 5 9 7
# 5 13 9

m = int(input('Quantas linhas vai ter cada matriz? '))
n = int(input('Quantas colunas vai ter cada matriz? '))

if m > 10 or n > 10:
    print('O máximo que podemos fazer é uma matriz 10x10!\n Digite novamente!')
    exit(0)
else:

    matriz_a = []
    matriz_b = []
    soma_matrizes = []

    print('Digite os valores da matriz A:')
    for i in range(0, m):
        linha = []
        for j in range(0, n):
            elemento = int(input(f'Elemento{[i,j]}: '))
            linha.append(elemento)
        matriz_a.append(linha)

    print('Digite os valores da matriz B:')
    for i in range(0, m):
        linha = []
        for j in range(0, n):
            elemento = int(input(f'Elemento{[i,j]}: '))
            linha.append(elemento)
        matriz_b.append(linha)

    print('MATRIZ SOMA:')

    for i in range(0, m):
        linha = []
        for j in range(0, n):
            soma = matriz_a[i][j] + matriz_b[i][j]
            linha.append(soma)
        soma_matrizes.append(linha)
    print(soma_matrizes)