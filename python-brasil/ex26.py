# Numa eleição existem três candidatos. Faça um programa que peça o número total de 
# eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de 
# cada candidato. 

ciro = 0
lula = 0
bolsonaro = 0

n = int(input('Numero de eleitores: '))

print('12 - Ciro\n13 - Lula\n22 - Bolsonaro')

for i in range(0, n):
    voto = int(input('Nº candidato: '))
    if voto == 12:
        ciro += 1
    elif voto == 13:
        lula += 1
    elif voto == 22:
        bolsonaro += 1
    else:
        print('Candidato nao existente no sistema!')
print("CIRO =", ciro, "votos.")
print("LULA =", lula, "votos.")
print("BOLSONARO =", bolsonaro, "votos.")
