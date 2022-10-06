# Faça um programa que calcule o valor total investido por um colecionador
# em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário
# deverá informar a quantidade de CDs e o valor para em cada um. 

qntd_cds = int(input('Quantidade CDs: '))

valor_total = 0

for i in range(0, qntd_cds):
    valor = float(input('Valor: '))
    valor_total += valor
valor_medio = valor_total / qntd_cds
print("VALOR TOTAL INVESTIDO =", valor_total, "\nQUANTIDADE DE CDS:", qntd_cds,"CDs.",
f"\nVALOR MEDIO GASTO EM CADA UM DELES: {valor_medio:.2f}")
