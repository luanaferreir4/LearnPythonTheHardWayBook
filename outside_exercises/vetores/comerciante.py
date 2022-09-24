# Problema "comerciante" 
# Um comerciante deseja fazer o levantamento do lucro das mercadorias que ele comercializa. Para isto, 
# mandou digitar um conjunto de N mercadorias, cada uma contendo nome, preço de compra e preço de 
# venda das mesmas. Fazer um programa que leia tais dados e determine e escreva quantas mercadorias 
# proporcionaram: 
# - lucro < 10% 
# - 10% ≤ lucro ≤ 20% 
# - lucro > 20% 
# Determine e escreva também o valor total de compra e de venda de todas as mercadorias, assim como 
# o lucro total. 
# Exemplo: 
# Serao digitados dados de quantos produtos? 4
# Produto 1: 
# Nome: Feijao
# Preco de compra: 10.00
# Preco de venda: 11.00
# Produto 2: 
# Nome: Arroz 
# Preco de compra: 12.00 
# Preco de venda: 12.80
# Produto 3: 
# Nome: Oleo 
# Preco de compra: 
# Preco de venda: 5.00 
# Preco de venda: 5.70
# Produto 4: 
# Nome: Sal 
# Preco de compra: 3.00
# Preco de venda: 4.00
# RELATORIO: 
# Lucro abaixo de 10%: 1 
# Lucro entre 10% e 20%: 2 
# Lucro acima de 20%: 1 
# Valor total de compra: 30.00 
# Valor total de venda: 33.50 
# Lucro total: 3.50

from functools import reduce

n = int(input('Serao digitados dados de quantos produtos? '))
preco_compras_ = 0
lucro_p_produto = []
vendas = []
compras = []
porcentagens_lucro = []

for i in range(0, n):
    print(f'Produto {i+1}:')
    nome = input('Nome: ')
    preco_compra = input('Preco de compra: ')
    while preco_compra == '':
        preco_compra = input('Preco de compra: ')
    preco_compra = float(preco_compra)
    compras.append(preco_compra)
    preco_venda = input('Preco de venda: ')
    while preco_venda == '':
        preco_venda = input('Preco de venda: ')
    preco_venda = float(preco_venda)
    vendas.append(preco_venda)
    lucro_total = preco_venda - preco_compra
    porcentagem_lucro = (lucro_total / preco_compra) * 100
    porcentagens_lucro.append(porcentagem_lucro)
    lucro_p_produto.append(lucro_total)
    

# Como calcular a porcentagem de um lucro:

# Margem bruta = lucro bruto / receita total x 100

abaixo_de_10 = 0
entre_10_e_20 = 0
acima_de_20 = 0
for porcentagem_lucro in porcentagens_lucro:
    if porcentagem_lucro < 10:
        abaixo_de_10 += 1
    elif porcentagem_lucro > 9 and porcentagem_lucro < 21:
        entre_10_e_20 += 1 
    else:
        acima_de_20 += 1

print("Lucro abaixo de 10%:", abaixo_de_10)
print("Lucro entre 10% e 20%:", entre_10_e_20)
print("Lucro acima de 20%:", acima_de_20)

preco_compras = reduce(lambda ac, p: ac + p, compras)
print("Valor total de compra:", preco_compras)

preco_vendas = reduce(lambda ac, p: ac + p, vendas)
print(f"Valor total de venda:", preco_vendas)

soma_lucro =  reduce(lambda ac, p: ac + p, lucro_p_produto)
print(f"LUCRO TOTAL = {soma_lucro:.2f}")

