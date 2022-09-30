# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a
# quantidade de números impares.

par = 0
impar = 0

for i in range(0, 10):
    numero = int(input('numero: '))
    if (numero % 2) == 0:
        par += 1
    else:
        impar += 1
print("NUMEROS PARES =", par)
print("NUMEROS IMPARES =", impar)