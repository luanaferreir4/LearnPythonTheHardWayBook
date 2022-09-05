cabelos = ['castanhos', 'loiros', 'ruivos']
olhos = ['castanhos', 'azuis', 'verdes']
pesos = [1, 2, 3, 4]

contagem = [1, 2, 3, 4, 5]
frutas = ['maçãs', 'laranjas', 'pêras', 'damascos']
trocados = [1, 'um centavo', 2, 'dez centavos', 3, 'vinte e cinco centavos']

# Esse primeiro tipo de loop percorre uma lista:
for numero in contagem:
    print(f"Essa é a contagem {numero}")


# Esse faz a mesma coisa:
for fruta in frutas:
    print(f"Uma fruta do tipo: {fruta}")


# Também podemos percorrer listas mistas:
for i in trocados:
    print(f"Eu peguei: {i}")


# Também podemos construir listas, comece com uma vazia:

elementos = []

# Então use a função range para fazer a contagem de 0 a 5:
for i in range(0, 6):
    print(f"Adicionando {i} a lista.")
# append é uma função que as listas entendem:
    elementos.append(i)


# Agora podemos imprimi-la:
for i in elementos:
    print(f"O elemento foi: {i}")


elementos1 = []

for i in range(0, 6):
    elementos2 = []
    for j in range(0, 6):
        elementos2.append(j)
        elementos1.append(elementos2)

print(elementos1)

leo1 = []
MAX = 4
for i in range(0, MAX):
    leo2 = []
    for j in range(0, MAX):
        leo2.append(i * MAX + j)         # Para ficar: [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    leo1.append(leo2)

print(leo1)


elementos2 = [i + 1 for i in range(0, 6)]
# i + 1 = O que eu quero.
# for i in range = Como obter o que quero.
print(elementos2)

# Macete de for:
elementos3 = [a for a in range(1, 7)]
print(elementos3)

lista = ['amora', 'uva', 'jabuticaba']

lista_percorrida = [elemento + "_deliciosa" for elemento in lista]
print(lista_percorrida)
