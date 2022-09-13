# Comparando listas e dicionários:

things = ['a', 'b', 'c', 'd']
print(things[1])  # b
things[1] = 'z'
print(things[1])  # z
print(things)  # ['a', 'z', 'c', 'd']

###########################################################################

stuff = {'name': 'Luana', 'age': 21, 'height': 6 * 12 + 2}  # Este é um dicionário

# Para acessá-lo:

print(stuff['name'])

# Para trocar o dado interno ou adicionar:

stuff['city'] = 'Taciba'

# Para verificar o dicionário:

print(stuff)

print(stuff['city'])

stuff1 = dict()

stuff1[1] = 'Meaw'
stuff1[2] = 'Neato'

print(stuff1)

# Como excluir coisas com a palavra-chave del:
del stuff1[1]
print(stuff1)
del stuff1
# print(stuff1) erro pois não tem mais o dicionário stuff1.

# crie um mapeamento entre estados e siglas:

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# crie um conjunto básico de estados e algumas cidades deles:

cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

# adicione mais algumas cidades:

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# imprima algumas cidades:

print('-' * 10)

print("NY state has", cities['NY'])
print("OR state has", cities['OR'])

print('-' * 10)
print("Michigan's abbreviation is:", states['Michigan'])
print("Florida's abbreviation is:", states['Florida'])

# Faça isso usando o dic states e depois o cities

print('-' * 10)
print("Michigan has:", cities[states['Michigan']])
print("New York has:", cities[states['New York']])

# imprima todas as siglas dos estados

for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# imprima cada cidade no estado

for abbrev, city in list(cities.items()):
    print(f'{city} - {abbrev}')

# agora faça ambos ao mesmo tempo

for state, abbrev in list(cities.items()):
    print(f"{state} - {abbrev}")
    print(f"and has the city {cities[states[abbrev]]}")  # tentar entender depois.