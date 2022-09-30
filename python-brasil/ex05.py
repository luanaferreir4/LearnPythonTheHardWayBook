# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.

pop_pais_a = int(input('Populacao do pais A: '))
taxa_de_cres_a = float(input('Taxa de crescimento populacional do pais A por ano: '))
pop_pais_b = int(input('Populacao do pais B: '))
taxa_de_cres_b = float(input('Taxa de crescimento populacional do pais B por ano: '))

ano = 0

while pop_pais_a < pop_pais_b:
    pop_pais_a = pop_pais_a + pop_pais_a * taxa_de_cres_a
    pop_pais_b = pop_pais_b + pop_pais_b * taxa_de_cres_b
    ano += 1

print("posição:", ano)

