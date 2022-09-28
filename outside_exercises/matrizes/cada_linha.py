# Problema "cada_linha" 
# Ler um inteiro N e uma matriz quadrada de ordem N (máximo = 10). Mostrar qual o maior elemento 
# de cada linha. Suponha não haver empates. 
# Exemplo: 
# Qual a ordem da matriz? 4
# Elemento [0,0]: 5 
# Elemento [0,1]: -3 
# Elemento [0,2]: 10
# Elemento [0,3]: 8
# Elemento [1,0]: 15 
# Elemento [1,1]: 8 
# Elemento [1,2]: 2
# Elemento [1,3]: 10
# Elemento [2,0]: 7 
# Elemento [2,1]: 9 
# Elemento [2,2]: -4
# Elemento [2,3]: 3
# Elemento [3,0]: 8 
# Elemento [3,1]: -7 
# Elemento [3,2]: 4
# Elemento [3,3]: 13
# MAIOR ELEMENTO DE CADA LINHA: 
# 10 
# 15 
# 9 
# 13 

n = int(input('Qual a ordem da matriz? '))

if n > 10:
    print('O máximo que podemos fazer é uma matriz 10x10!\n Digite novamente!')
    exit(0)
else:
    matriz = []
    for i in range(0, n):
        lista = []
        for j in range(0, n):
            elemento = int(input(f'Elemento{i,j}: '))
            lista.append(elemento)
        matriz.append(lista)

    print('MAIOR ELEMENTO DE CADA LINHA:')
    for lista in matriz:
        maior_numero = max(lista)
        print(maior_numero)
