# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média
# de idade da turma varia entre 0 e 25,
# 26 e 60 e
# maior que 60;
# e então, dizer se a turma é jovem, adulta
# ou idosa, conforme a média calculada. 

from functools import reduce

n = int(input('Quantas pessoas: '))

idades = []

for i in range(0, n):
    idade = float(input('Idade: '))
    idades.append(idade)
soma = reduce(lambda ac, p: ac + p, idades)
media_idade = soma / len(idades)
print(media_idade)

if media_idade > -1 and media_idade < 26:
    print('Turma jovem!')
elif media_idade < 61:
    print('Turma adulta!')
else:
    print('Turma idosa!')