# Faça um programa que calcule o número médio de alunos por turma.
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
# As turmas não podem ter mais de 40 alunos. 
from functools import reduce

qntd_turmas = int(input('Quantidade turmas: '))

qntd_alunos_list = []

for i in range(0, qntd_turmas):
    qntd_alunos = int(input('Quantidade alunos: '))
    qntd_alunos_list.append(qntd_alunos)
soma = reduce(lambda ac, p: ac + p, qntd_alunos_list)
media = soma / len(qntd_alunos_list)
print('NUMERO MEDIO DE ALUNOS POR TURMA =', media)