# Problema "negativos_matriz" 
# Ler dois números M e N (máximo = 10), e depois ler uma matriz MxN de números inteiros, conforme 
# exemplo. Em seguida, mostrar na tela somente os números negativos da matriz. 
# Exemplo: 
# Qual a quantidade de linhas da matriz? 2 
# Qual a quantidade de colunas da matriz? 3
# Elemento [0,0]: 12 
# Elemento [0,1]: -8 
# Elemento [0,2]: 5
# Elemento [1,0]: -13
# Elemento [1,1]: 10 
# Elemento [1,2]: -6
# VALORES NEGATIVOS: 
# -8 
# -13 
# -6 

m = int(input('Qual a quantidade de linhas da matriz? '))
n = int(input('Qual a quantidade de colunas da matriz? '))

if m > 10 or n > 10:
    print('O máximo que podemos fazer são matrizes 10x10! Tente novamente!')
    exit(0)
else:

    elementos = []

    for i in range(0, m):
        for j in range(0, n):
            elemento = int(input(f'Elemento {[i, j]}: '))
            elementos.append(elemento)

    print('VALORES NEGATIVOS:')
    for elemento in elementos:
        if elemento < 0:
            print(elemento)

