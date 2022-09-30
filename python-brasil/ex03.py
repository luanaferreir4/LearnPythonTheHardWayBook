# Faça um programa que leia e valide as seguintes informações:
#
#     Nome: maior que 3 caracteres;
#     Idade: entre 0 e 150;
#     Salário: maior que zero;
#     Sexo: 'f' ou 'm';
#     Estado Civil: 's', 'c', 'v', 'd';

nome = input('Nome: ')

while len(nome) < 4:
    nome = input('Nome: ')


idade = float(input('Idade: '))

while idade < 0 or idade > 150:
    idade = float(input('Idade: '))


salario = float(input('Salario: '))

while salario < 0.1:
    salario = float(input('Salario: '))


sexo = input('Sexo: ')

while sexo.upper() != "F" and sexo.upper() != "M":
    print('Tente novamente! F: feminino, M: masculino')
    sexo = input('Sexo: ')


estados_civis = ['C', 'V', 'S', 'D']
estado_civil = input('Estado Civil: ').upper()

while estado_civil not in estados_civis:
    estado_civil = input('Estado Civil inválido \n Tente novamente: ').upper()


