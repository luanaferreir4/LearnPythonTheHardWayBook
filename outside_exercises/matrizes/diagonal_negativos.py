# Problema "diagonal_negativos" 
# Fazer um programa para ler um número inteiro N (máximo = 10) e uma matriz quadrada de ordem N 
# contendo números inteiros. Em seguida, mostrar a diagonal principal e a quantidade de valores 
# negativos da matriz. 
# Exemplo: 
# Qual a ordem da matriz? 3
# Elemento [0,0]: 5 
# Elemento [0,1]: -3 
# Elemento [0,2]: 10
# Elemento [1,0]: 15 
# Elemento [1,1]: 8 
# Elemento [1,2]: 2
# Elemento [2,0]: 7 
# Elemento [2,1]: 9 
# Elemento [2,2]: -4
# DIAGONAL PRINCIPAL: 
# 5 8 -4 
# QUANTIDADE DE NEGATIVOS = 2

negativos = [] 
diagonal_p = []
negativos_cont = 0

n = int(input('Qual a ordem da matriz? '))
if n > 10:
    print('O máximo que podemos fazer é uma matriz 10x10!\n Digite novamente!')
else:
    for i in range(0, n):
        for j in range(0, n):
            elemento = int(input(f'Elemento {[i, j]}: '))
            if elemento < 0:
                negativos.append(elemento)
                negativos_cont += 1
            if i == j:
                diagonal_p.append(elemento)

# Diagonal principal: i == j
print("DIAGONAL PRINCIPAL =", diagonal_p)
print("QUANTIDADE DE NEGATIVOS =", negativos_cont)