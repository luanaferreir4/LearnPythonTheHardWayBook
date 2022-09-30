# Faça um programa que receba dois números inteiros e gere os números inteiros que
# estão no intervalo compreendido por eles.

ni = int(input('Número inicial: '))
nf = int(input('Número final: '))

for i in range(ni+1, nf):
    print(i)