# Problema "combustivel" (adaptado de URI 1134)
# Um posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes.
# Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma:
# 1.Álcool 2.Gasolina 3.Diesel 4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a
# 4) deve ser solicitado um novo código (até que seja válido). O programa será encerrado quando o
# código informado for o número 4, devendo então mostrar a mensagem "MUITO OBRIGADO", bem
# como as quantidades de cada combustível.
# Exemplo:
# Informe um codigo (1, 2, 3) ou 4 para parar: 8
# Informe um codigo (1, 2, 3) ou 4 para parar: 1
# Informe um codigo (1, 2, 3) ou 4 para parar: 7
# Informe um codigo (1, 2, 3) ou 4 para parar: 2
# Informe um codigo (1, 2, 3) ou 4 para parar: 2
# Informe um codigo (1, 2, 3) ou 4 para parar: 4
# MUITO OBRIGADO
# Alcool: 1
# Gasolina: 2
# Diesel: 0

combustivel = int(input("Informe um codigo (1, 2, 3) ou 4 para parar: "))

alcool = 0
gasolina = 0
diesel = 0

while combustivel != 4:
    if combustivel == 1:
        alcool += 1
    elif combustivel == 2:
        gasolina += 1
    elif combustivel == 3:
        diesel += 1
    else:
        print("Valor inesperado! Tente novamente.")
    combustivel = int(input("Informe um codigo (1, 2, 3) ou 4 para parar: "))

print("MUITO OBRIGADO!")
resultado = f"Alcool: {alcool}\nGasolina: {gasolina}\nDiesel: {diesel}"
print(resultado)

