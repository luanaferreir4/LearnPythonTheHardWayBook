# Problema "acima_diagonal"
# Ler um inteiro N (máximo = 10) e uma matriz quadrada de ordem N
# contendo números inteiros. Mostrar a soma dos elementos acima da
# diagonal principal. Um exemplo de números acima da diagonal
# principal é mostrado ao lado (no caso as células com fundo cinza).
# Exemplo:
# Entrada
# Qual a ordem da matriz? 4
# Elemento [0,0]: 5
# Elemento [0,1]: 2
# Elemento [0,2]: 3
# Elemento [0,3]: 1
# Elemento [1,0]: 8
# Elemento [1,1]: 2
# Elemento [1,2]: 4
# Elemento [1,3]: 5
# Elemento [2,0]: 7
# Elemento [2,1]: 3
# Elemento [2,2]: 1
# Elemento [2,3]: 3
# Elemento [3,0]: 9
# Elemento [3,1]: 12
# Elemento [3,2]: 9
# Elemento [3,3]: 5
# SOMA DOS ELEMENTOS ACIMA DA DIAGONAL PRINCIPAL = 18

n = int(input('Qual a ordem da matriz? '))

if n > 10:
    print('O máximo que podemos fazer são matrizes 10x10! Tente novamente!')
    exit(0)
else:
    matriz = []
    for i in range(0, n):
        linha = []
        for j in range(0, n):
            elemento = int(input(f'Elemento {[i, j]}: '))
            linha.append(elemento)
        matriz.append(linha)
    print(matriz)

    soma = 0

    for i in range(0, n):
        for j in range(i + 1, n):
            soma += matriz[i][j]
    print("SOMA DOS ELEMENTOS ACIMA DA DIAGONAL PRINCIPAL =", soma)


