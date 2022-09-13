# Problema "experiencias" (adaptado de URI 1094)
# Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para
# organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano,
# quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada. Este
# laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas
# informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia
# utilizada e a quantidade de cobaias utilizadas em cada experimento. Faça um programa que leia um
# valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um
# inteiro que representa a quantidade de cobaias utilizadas e uma letra ('C', 'R' ou 'S'), indicando o tipo
# de cobaia (R:Rato S:Sapo C:Coelho). Apresente o total de cobaias utilizadas, o total de cada tipo de
# cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o
# percentual deve ser apresentado com dois dígitos após o ponto.
# Exemplo:
# Quantos casos de teste serao digitados? 10
# Quantidade de cobaias: 10
# Tipo de cobaia: C
# Quantidade de cobaias: 6
# Tipo de cobaia: R
# Quantidade de cobaias: 15
# Tipo de cobaia: S
# Quantidade de cobaias: 5
# Tipo de cobaia: C
# Quantidade de cobaias: 14
# Tipo de cobaia: R
# Quantidade de cobaias: 9
# Tipo de cobaia: C
# Quantidade de cobaias: 6
# Tipo de cobaia: R
# Quantidade de cobaias: 8
# Tipo de cobaia: S
# Quantidade de cobaias: 5
# Tipo de cobaia: C
# Quantidade de cobaias: 14
# Tipo de cobaia: R
# RELATORIO FINAL:
# Total: 92 cobaias
# Total de coelhos: 29
# Total de ratos: 40
# Total de sapos: 23
# Percentual de coelhos: 31.52
# Percentual de ratos: 43.48
# Percentual de sapos: 25.00

from util import die

x = int(input("Quantos casos de testes serão digitados? "))
ratos = 0
sapos = 0
coelhos = 0
cobaias = 0

print("Antes de começar saiba que as siglas para os tipos de cobaias são:\t\nC : coelhos\n R : ratos\n S : sapos")

for i in range(0, x):
    qntd = int(input("Quantidade de cobaias: "))
    tipo = input("Tipo de cobaia: ")

    if tipo.upper() == 'R':
        ratos += qntd
        cobaias += qntd
    elif tipo.upper() == 'S':
        sapos += qntd
        cobaias += qntd
    elif tipo.upper() == 'C':
        coelhos += qntd
        cobaias += qntd
    else:
        print('Tente novamente e lembre-se:\n C : coelhos\n R : ratos\n S : sapos')
        die('Valor não encontrado.')
print(f"TOTAL de cobaias: {cobaias}")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {(coelhos / cobaias) * 100:.2f}%")
print(f"Percentual de ratos: {(ratos / cobaias) * 100:.2f}%")
print(f"Percentual de sapos: {(sapos / cobaias) * 100:.2f}%")