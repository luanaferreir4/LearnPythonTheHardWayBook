estados = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cidades = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cidades['NY'] = 'New York'
cidades['OR'] = 'Portland'

print('-' * 20)
print('Estado de NY tem', cidades['NY'])
print("Estado de OR tem", cidades['OR'])

print('-' * 20)
print('A abreviaçao de Michigan é', estados['Michigan'])
print('A abreviacao de Florida é', estados['Florida'])

print('-' * 20)
print('Michigan tem', cidades[estados['Michigan']])
print('Florida tem', cidades[estados['Florida']])

print('-' * 20)
for estado, abrev in list(estados.items()):
    print(f"A abreviação de {estado} é {abrev}")

print('-' * 20)
for abrev, cidade in list(cidades.items()):
    print(f"{abrev} tem a cidade {cidade}")

print('-' * 20)
for estado, abrev in list(estados.items()):
    print(f"A abreviação do estado {estado} é {abrev}")
    print(f"E tem a cidade {cidades[abrev]}")

print('-' * 20)
estado = estados.get('TX')  # Pra dar True precisa ocupar o segundo parâmetro de get.

if not estado:
    print("Desculpa, não há Texas.")

cidade = cidades.get('TX', 'Não existe')
print(f"A cidade do estado do 'TX' é: {cidade}")