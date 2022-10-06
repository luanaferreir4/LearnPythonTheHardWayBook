# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo,
# por quais número ele é divisível. 

n = int(input('Digite um numero: '))

# Agora vamos ver se ele é primo: um número primo só é divisível por um (1) e por ele mesmo (n)
#  [tem que dar um número inteiro]. 

tot = 0
numeros_divisiveis = []

for c in range(1, n + 1):
    if n % c == 0:
        numeros_divisiveis.append(c)
        tot += 1
    
if tot != 2:
    print(f'NUMEROS DIVISIVEIS POR {n} =', numeros_divisiveis)
else:
    print(f'Numero primo!')
