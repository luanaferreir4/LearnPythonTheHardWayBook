# Problema "idades"
# Fazer um programa para ler o nome e idade de duas pessoas. Ao final mostrar uma mensagem com os
# nomes e a idade média entre essas pessoas, com uma casa decimal, conforme exemplo.
#
# Exemplo:
#
# Dados da primeira pessoa:
# Nome: Maria Silva
# Idade: 19
#
# Dados da segunda pessoa:
# Nome: Joao Melo
# Idade: 20
# A idade média de Maria Silva e Joao Melo é de 19.5 anos

msg = '> '

print('Dados da primeira pessoa')
print('Nome:')
nome1 = input(msg)
print('Idade:')
idade1 = float(input(msg))

print('Dados da segunda pessoa')
print('Nome:')
nome2 = input(msg)
print('Idade:')
idade2 = float(input(msg))

idade_media = (idade1 + idade2) / 2

print(f'A idade média de {nome1} e {nome2} é de {idade_media} anos.')
