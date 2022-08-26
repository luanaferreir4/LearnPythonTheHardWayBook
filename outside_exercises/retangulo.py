# Problema "retangulo"
# Fazer um programa para ler as medidas da base e altura de um retângulo. Em seguida, mostrar o valor
# da área, perímetro e diagonal deste retângulo, com quatro casas decimais, conforme exemplos.
# Exemplo 1:
# Base do retangulo: 4.0
# Altura do retangulo: 5.0
# AREA = 20.0000
# PERIMETRO = 18.0000
# DIAGONAL = 6.4031
# Exemplo 2:
# Base do retangulo: 10.3
# Altura do retangulo: 13.1
# AREA = 134.9300
# PERIMETRO = 46.8000
# DIAGONAL = 16.6643
#

import math

msg = '> '

print('Base do retângulo:')
base_retangulo = float(input(msg))
print('Altura do retângulo:')
altura_retangulo = float(input(msg))

area = base_retangulo * altura_retangulo
print(f'AREA = {area:.4f}')
perimetro = 2 * (base_retangulo + altura_retangulo)
print(f'PERIMETRO = {perimetro:.4f}')
diagonal1 = pow(base_retangulo, 2) + pow(altura_retangulo, 2)
diagonal2 = math.sqrt(diagonal1)
print(f'DIAGONAL = {diagonal2:.4f}')
