# Problema "dados_pessoas" 
# Tem-se um conjunto de dados contendo a altura e o gênero (M, F) de N pessoas. Fazer um programa 
# que calcule e escreva a maior e a menor altura do grupo, a média de altura das mulheres, e o número 
# de homens. 
# Exemplo: 
# Quantas pessoas serao digitadas? 5
# Altura da 1a pessoa: 1.70
# Genero da 1a pessoa: F
# Altura da 2a pessoa: 1.83 
# Genero da 2a pessoa: M
# Altura da 3a pessoa: 1.54 
# Genero da 3a pessoa: M
# Altura da 4a pessoa: 1.61 
# Genero da 4a pessoa: F
# Altura da 5a pessoa: 1.75 
# Genero da 5a pessoa: F
# Menor altura = 1.54 
# Maior altura = 1.83 
# Media das alturas das mulheres = 1.69 
# Numero de homens = 2 

n = int(input("Quantas pessoas serao digitadas? "))
masculino = 0
feminino = 0
soma_fem = 0

alturas = []
alturas_femininas = []
alturas_masculinas = []

for i in range(0, n):
    print(f'Dados da {i+1}a pessoa: ')
    altura = float(input(f'Altura:'))
    genero = input('Genero: ')
    if genero.capitalize() == "M":
        masculino += 1
        alturas.append(altura)
        alturas_masculinas.append(altura)
    elif genero.capitalize() == "F":
        feminino += 1
        alturas.append(altura)
        alturas_femininas.append(altura)
        soma_fem += altura
        media_fem = soma_fem / feminino
    else:
        print("Esse programa apenas aceita 'M' para masculino e 'F' para feminino, tente novamente!")


altura_min = min(alturas)
print("MENOR ALTURA =", altura_min)

altura_max = max(alturas)
print("MAIOR ALTURA =", altura_max)

print(f"Media das alturas das mulheres = {media_fem:.2f}")
print("Numero de homens =", masculino)

