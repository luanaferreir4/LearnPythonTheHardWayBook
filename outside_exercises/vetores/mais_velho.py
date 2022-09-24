# Problema "mais_velho" 
# Fazer um programa para ler um conjunto de nomes de pessoas e suas respectivas idades. Os nomes 
# devem ser armazenados em um vetor, e as idades em um outro vetor. Depois, mostrar na tela o nome 
# da pessoa mais velha. 
# Exemplo: 
# Quantas pessoas voce vai digitar? 5
# Dados da 1a pessoa: 
# Nome: Joao
# Idade: 16
# Dados da 2a pessoa: 
# Nome: Maria
# Idade: 21
# Dados da 3a pessoa: 
# Nome: Teresa
# Idade: 15
# Dados da 4a pessoa: 
# Nome: Carlos
# Idade: 23
# Dados da 5a pessoa: 
# Nome: Paulo
# Idade: 17
# PESSOA MAIS VELHA: Carlos 

from functools import reduce


n = int(input("Quantas pessoas voce vai digitar? "))

idades = []
nomes = []

for i in range(0, n):
    print(f'Dados da {i+1}a pessoa:')
    nome = input("Nome: ")
    nomes.append(nome)
    idade = float(input("Idade: "))
    idades.append(idade)
    
    
max_numero = max(idades)
print("MAIOR VALOR =", max_numero)

maior_posicao = idades.index(max_numero)
print("PESSOA MAIS VELHA =", nomes[maior_posicao])
