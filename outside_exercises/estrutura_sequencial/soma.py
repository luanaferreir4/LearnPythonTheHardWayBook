# Problema "soma"
# Fazer um programa para ler dois valores inteiros X e Y, e depois mostrar na tela o valor da soma destes
# números.
#
# Exemplo 1:
# Digite o valor de X: 8
# Digite o valor de Y: 10
# SOMA = 18
#
# Exemplo 2:
# Digite o valor de X: 12
# Digite o valor de Y: 31
# SOMA = 43

msg = '> '

print('Digite o valor de X:')
x = int(input(msg))
print('Digite o valor de Y:')
y = int(input(msg))
print(f'SOMA = {x + y}')
