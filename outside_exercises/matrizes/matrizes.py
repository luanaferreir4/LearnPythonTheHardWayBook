# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final mostre a matriz na tela, com a formatação correta.

carros = ['HRV', 'Focus', 'Argo', 'Golf']  # lista

carros.append('Ford')
carros[1] = 'Volkswagen'

for carro in carros:
    print(carro)

# Matriz é uma lista com uma lista dentro, temos 2 indices que vao controlar teoricamente a linha e a coluna.
# [Cada posicao do list seria um novo list.]

carros = [
    ["Modelo", "HRV"],
    ["Fabricante", "Honda"],
    ["Ano", 2016]
]  # cada posição desse list vai receber um novo list.

# adicionar linhas na matriz:
carros.append(["Cor", "Prata"])

# Se quero mudar o ano:
carros[2][1] = 2018

print(carros[0][0])  # Modelo
print(carros[1][1])  # Honda
print(carros[2][0])  # Ano
print(carros[2][1])

for linha,coluna in carros:
    print(linha + ": " + str(coluna))

