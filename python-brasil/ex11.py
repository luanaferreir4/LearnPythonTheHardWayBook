# Altere o programa anterior para mostrar no final a soma dos números.

ni = int(input('Número inicial: '))
nf = int(input('Número final: '))

soma = 0

for i in range(ni+1, nf):
    soma += i
    print(i)
print("SOMA DOS NUMEROS =", soma)
