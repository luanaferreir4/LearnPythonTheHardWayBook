# Problema "par_impar" (adaptado de URI 1074)
# Leia um valor inteiro N. Este valor será a quantidade de números inteiros que serão lidos em seguida.
# Para cada valor lido, mostre uma mensagem dizendo se este valor lido é PAR ou IMPAR, e também
# se é POSITIVO ou NEGATIVO. No caso do valor ser igual a zero (0), seu programa deverá imprimir
# apenas NULO.
# Exemplo:
# Quantos numeros voce vai digitar? 4
# Digite um numero: -5
# IMPAR NEGATIVO
# Digite um numero: 0
# NULO
# Digite um numero: 3
# IMPAR POSITIVO
# Digite um numero: -4
# PAR NEGATIVO
from util import die

n = int(input("Quantos numeros voce vai digitar? "))

for i in range(0, n):
    valor = int(input("Digite um numero: "))
    if valor == 0:
        print("NULO")
    elif valor > 0 and (valor % 2) == 0:
        print("PAR POSITIVO")
    elif valor > 0 and (valor % 2) == 1:
        print("IMPAR POSITIVO")
    elif valor < 0 and (valor % 2) == 0:
        print("PAR NEGATIVO")
    elif valor < 0 and (valor % 2) == 1:
        print("IMPAR NEGATIVO")
    else:
        die("Erro inesperado!")
