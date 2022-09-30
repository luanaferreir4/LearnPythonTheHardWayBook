# Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
v = 0

for i in range(0, 5):
    numero = int(input('Número: '))
    soma += numero
    v += 1
print("SOMA =", soma)
print("MEDIA =", soma / v)
