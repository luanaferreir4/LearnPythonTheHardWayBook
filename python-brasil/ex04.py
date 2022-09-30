# Supondo que a população de um país A seja da ordem de 80000 habitantes
# com uma taxa anual de crescimento de 3% e que a população de B seja 200000
# habitantes com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva o número de anos necessários para que
# a população do país A ultrapasse ou iguale a população do país B, mantidas as
# taxas de crescimento.

taxa_de_cres_a = 0.03
taxa_de_cres_b = 0.015
pop_pais_a = 80000
pop_pais_b = 200000

ano = 0

while pop_pais_a < pop_pais_b:
    pop_pais_a = pop_pais_a + pop_pais_a * taxa_de_cres_a
    pop_pais_b = pop_pais_b + pop_pais_b * taxa_de_cres_b
    ano += 1

print("posição:", ano)

    



