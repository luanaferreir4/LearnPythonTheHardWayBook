# Problema "terreno"
#
# Fazer um programa para ler as medidas da largura e comprimento de um terreno retangular com uma
# casa decimal, bem como o valor do metro quadrado do terreno com duas casas decimais. Em seguida,
# o programa deve mostrar o valor da área do terreno, bem como o valor do preço do terreno, ambos com
# duas casas decimais, conforme exemplo.
#
# Exemplo 1:
# Digite a largura do terreno: 10.0
# Digite o comprimento do terreno: 30.0
# Digite o valor do metro quadrado: 200.00
# Area do terreno = 300.00
# Preco do terreno = 60000.00
#
# Exemplo 2:
# Digite a largura do terreno: 12.0
# Digite o comprimento do terrano: 20.0
# Digite o valor do metro quadrado: 150.00
# Area do terreno = 240.00
# Preco do terreno = 36000.00

print('Largura do terreno:')
largura = float(input('> '))
print('Comprimento do terreno:')
comprimento = float(input('> '))
area = largura * comprimento
print(f'A área do terreno é: {area:.2f}m².')
print('Digite o valor do metro quadrado:')
valor_metro_quadrado = float(input('> '))
print(f'Valor do metro quadrado: {valor_metro_quadrado:.2f}m².')
preco_terreno = (valor_metro_quadrado * largura) * comprimento
print(f'Preço do terreno: R$ {preco_terreno:.2f}')
