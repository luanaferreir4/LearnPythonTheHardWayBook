# Problema "pares_consecutivos" (adaptado de URI 1159)
# O programa deve ler um valor inteiro X indefinidas vezes. (O programa irá parar quando o valor de X
# for igual a 0). Para cada X lido, imprima a soma dos 5 pares consecutivos a partir de X, inclusive o X
# , se for par. Se o valor de entrada for 4, por exemplo, a saída deve ser 40, que é o resultado da operação:
# 4+6+8+10+12, enquanto que se o valor de entrada for 11, por exempo, a saída deve ser 80, que é a
# soma de 12+14+16+18+20.
# Exemplo:
# Digite um numero inteiro: 4
# SOMA = 40
# Digite um numero inteiro: 11
# SOMA = 80
# Digite um numero inteiro: 0

# 12 + 14 + 16 + 18 + 20 = 80
# 4 + 6 + 8 + 10 + 12 = 40
from util import die

numero = int(input("Digite um numero inteiro: "))

numero_final = numero + 10
soma = 0

if (numero % 2) == 0:
    for i in range(numero, numero_final, 2):
        print(i)
        soma += i
    print("SOMA:", soma)

elif (numero % 2) == 1:
    for i in range(numero + 1, numero_final, 2):
        print(i)
        soma += i
    print("SOMA:", soma)
else:
    die(f"Erro no sistema! Esperado 0 ou 1, recebido {numero % 2}.")





