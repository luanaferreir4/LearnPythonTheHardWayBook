# Problema "negativos"
# Faça um programa que leia um número inteiro positivo N (máximo = 10) e depois N números inteiros
# e armazene-os em um vetor. Em seguida, mostrar na tela todos os números negativos lidos.
# Exemplo:
# Quantos numeros voce vai digitar? 6
# Digite um numero: 8
# Digite um numero: -2
# Digite um numero: 9
# Digite um numero: 10
# Digite um numero: -3
# Digite um numero: -7
# NUMEROS NEGATIVOS:
# -2
# -3
# -7

valores = []
n = int(input('Quantos numeros voce vai digitar? '))
for i in range(0, n):
    valor = int(input('Digite um numero: '))
    valores.append(valor)
print(valores)

negativos = list(filter(lambda p: p < 0, valores))
print(negativos)
