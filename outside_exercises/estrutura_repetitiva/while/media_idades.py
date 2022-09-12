msg = "> "

print('Digite as idades:')

idade = int(input(msg))


idades = []

while idade >= 0:
    idades.append(idade)
    idade = int(input(msg))
print(idades)

soma = 0

for idade in idades:
    soma += idade
dividendo = len(idades)
if dividendo > 0:
    media = soma / dividendo
    print(f"MÉDIA = {media:.2f}")
else:
    print("IMPOSSIVEL CALCULAR")
