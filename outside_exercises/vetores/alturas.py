# Problema "alturas"
# Fazer um programa para ler nome, idade e altura de N pessoas, conforme exemplo. Depois, mostrar na
# tela a altura média das pessoas, e mostrar também a porcentagem de pessoas com menos de 16 anos,
# bem como os nomes dessas pessoas caso houver.
# Exemplo:
# Quantas pessoas serao digitadas? 5
# Dados da 1a pessoa:
# Nome: Joao
# Idade: 15
# Altura: 1.82
# Dados da 2a pessoa:
# Nome: Maria
# Idade: 16
# Altura: 1.60
# Dados da 3a pessoa:
# Nome: Teresa
# Idade: 14
# Altura: 1.58
# Dados da 4a pessoa:
# Nome: Carlos
# Idade: 21
# Altura: 1.65
# Dados da 5a pessoa:
# Nome: Paulo
# Idade: 17
# Altura: 1.78
# Altura média: 1.69
# Pessoas com menos de 16 anos: 40.0%
# Joao
# Teresa

from functools import reduce

n = int(input('Quantas pessoas serão digitadas? '))

alturas = []
nomes_menos_16 = []
soma_ = 0

for i in range(0, n):
    print(f'Dados da {i+1}a pessoa:')
    nome = input('nome: ')
    idade = int(input('idade: '))
    altura = float(input('altura: '))
    alturas.append(altura)
    if idade < 16:
        nomes_menos_16.append(nome)
        soma_ += 1

        

soma = reduce(lambda ac, valor_atual: valor_atual + ac, alturas, 0)
altura_media = soma / len(alturas)
print(f'Altura media : {altura_media:.2f}')


percentual = (soma_ / n) * 100
print(f"Pessoas com menos de 16 anos: {percentual}%")
print(nomes_menos_16)




