# Problema "matriz_geral"
# Ler uma matriz quadrada de ordem N (máximo = 10), contendo números reais. Em seguida, fazer as
# seguintes ações:
# a) calcular e imprimir a soma de todos os elementos positivos da matriz.
# b) fazer a leitura do índice de uma linha da matriz e, daí, imprimir todos os elementos desta linha.
# c) fazer a leitura do índice de uma coluna da matriz e, daí, imprimir todos os elementos desta coluna.
# d) imprimir os elementos da diagonal principal da matriz.
# e) alterar a matriz elevando ao quadrado todos os números negativos da mesma. Em seguida imprimir
# a matriz alterada.
# Exemplo:
# Qual a ordem da matriz? 3
# Elemento [0,0]: 7.0
# Elemento [0,1]: -8.0
# Elemento [0,2]: 10.0
# Elemento [1,0]: -2.0
# Elemento [1,1]: 3.0
# Elemento [1,2]: 5.0
# Elemento [2,0]: 11.0
# Elemento [2,1]: -15.0
# Elemento [2,2]: 4.0
# SOMA DOS POSITIVOS: 40.0
# Escolha uma linha: 1
# LINHA ESCOLHIDA: -2.0 3.0 5.0
# Escolha uma coluna: 2
# COLUNA ESCOLHIDA: 10.0 5.0 4.0
# DIAGONAL PRINCIPAL: 7.0 3.0 4.0
# MATRIZ ALTERADA:
# 7.0 64.0 10.0
# 4.0 3.0 5.0
# 11.0 225.0 4.0

n = int(input('Qual a ordem da matriz? '))

if n > 10:
    print('Trabalhamos no máximo com matrizes 10x10 e com números positivos! Tente novamente!')
    exit(0)
else:

    soma_pos = 0
    diagonal_p = []
    matriz = []

    for i in range(0, n):
        linha = []
        for j in range(0, n):
            elemento = float(input(f'Elemento {[i,j]}: '))
            linha.append(elemento)
            if i == j:
                diagonal_p.append(elemento)
            if elemento > 0:
                soma_pos += elemento
        matriz.append(linha)
    
    print(matriz)

    print("SOMA DOS POSITIVOS =", soma_pos)
    print("DIAGONAL PRINCIPAL =", diagonal_p)

    
    x = int(input('Escolha uma linha: '))
    for i in range(0, n):
        linha = []
        for j in range(0, n):
            linha.append(matriz[x][j])
    print("LINHA ESCOLHIDA =", linha)


    y = int(input('Escolha uma coluna: '))
    coluna = []
    for k in range(0, n):
        for l in range(0, 1):
            coluna.append(matriz[k][y])
    print("COLUNA ESCOLHIDA =", coluna)


    print("MATRIZ ALTERADA:")
    def matriz_alterada(matriz):

        matriz_alt = []
        for numero in matriz:
            valor = numero ** 2 if numero < 0 else numero
            matriz_alt.append(valor)

        return matriz_alt

matriz_alt = list(map(matriz_alterada, matriz))
print(matriz_alt)