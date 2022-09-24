# Problema "aprovados" 
# Fazer um programa para ler um conjunto de N nomes de alunos, bem como as notas que eles tiraram 
# no 1º e 2º semestres. Cada uma dessas informações deve ser armazenada em um vetor. Depois, imprimir 
# os nomes dos alunos aprovados, considerando aprovados aqueles cuja média das notas seja maior ou 
# igual a 6.0 (seis). 
# Exemplo: 
# Quantos alunos serao digitados? 4
# Digite nome, primeira e segunda nota do 1o aluno: 
# Joao Silva 
# 7.0 
# 8.5 
# Digite nome, primeira e segunda nota do 2o aluno: 
# Maria Teixeira 
# 9.2 
# 6.5 
# Digite nome, primeira e segunda nota do 3o aluno: 
# Carlos Carvalho 
# 5.0 
# 6.0 
# Digite nome, primeira e segunda nota do 4o aluno: 
# Teresa Pires 
# 5.5 
# 6.5 
# Alunos aprovados: 
# Joao Silva 
# Maria Teixeira 
# Teresa Pires 

n = int(input("Quantos alunos serao digitados? "))

msg = '> '

nomes = []
notas1 = []
notas2 = []
alunos_aprovados = []
medias = []

for i in range(0, n):
    print(f'Digite nome, primeira e segunda nota do {i+1}o aluno:')
    nome = input(msg)
    nomes.append(nome)
    nota1 = float(input(msg))
    notas1.append(nota1)
    nota2 = float(input(msg))
    notas2.append(nota2)
    media = (nota1 + nota2) / 2
    medias.append(media)
    if media >= 6:
        alunos_aprovados.append(nome)

print('Alunos aprovados: ')
for aluno_aprovado in alunos_aprovados:
    print(aluno_aprovado)
