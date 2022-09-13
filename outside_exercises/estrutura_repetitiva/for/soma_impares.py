# Problema "soma_impares" (adaptado de URI 1071)
# Leia 2 valores inteiros X e Y (em qualquer ordem). A seguir, calcule e mostre a soma dos números
# impares entre eles.
# Exemplo 1:
# Digite dois numeros:
# 2
# 9
# SOMA DOS IMPARES = 15
# Exemplo 2:
# Digite dois numeros:
# 15
# 10
# SOMA DOS IMPARES = 24
# Exemplo 3:
# Digite dois numeros:
# 6
# -5
# SOMA DOS IMPARES = 5
from util import die

print("Digite dois numeros:")
msg = "> "
num1 = int(input(msg))
num2 = int(input(msg))

soma = 0
if num1 < num2:
    for i in range(num1 + 1, num2):
        if (i % 2) == 1:
            soma += i
    print("SOMA DOS ÍMPARES:", soma)
elif num1 > num2:
    for i in range(num2 + 1, num1):
        if (i % 2) == 1:
            soma += i
    print("SOMA DOS ÍMPARES:", soma)
else:
    die("Erro inesperado!")
