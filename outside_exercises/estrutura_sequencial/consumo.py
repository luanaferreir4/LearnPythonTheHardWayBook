# Problema "consumo" 
# Fazer um programa para ler a distância total (em km) percorrida por um carro, bem como o total de 
# combustível gasto por este carro ao percorrer tal distância. Seu programa deve mostrar o consumo 
# médio do carro, com três casas decimais. 
# Exemplo 1: 
# Distancia percorrida: 500
# Combustível gasto: 38.5
# Consumo medio = 12.987 
# Exemplo 2: 
# Distancia percorrida: 1108
# Combustível gasto: 71.4
# Consumo medio = 15.518 

def calcular_consumo_medio(distancia_percorrida, combustivel_gasto):
    return distancia_percorrida / combustivel_gasto


def coletar_dados():
    print("Distancia percorrida:", end=' ')
    distancia_percorrida = float(input())
    print("Combustivel gasto:", end=' ')
    combustivel_gasto = float(input())
    return distancia_percorrida, combustivel_gasto

def consumo():  # Para saber o gasto de combustivel por distancia: distancia_percorrida / combustivel_gasto.
    dados = coletar_dados()
    distancia_percorrida, combustivel_gasto = dados
    consumo = calcular_consumo_medio(distancia_percorrida, combustivel_gasto)
    return f"Consumo medio = {consumo:.3f}"