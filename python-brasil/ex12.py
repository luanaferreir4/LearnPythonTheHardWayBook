# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja ver a tabuada.
# A saída deve ser conforme o exemplo abaixo:

tabuada = int(input('Qual tabuada deseja ver? '))

if tabuada > 10 or tabuada < 0:
    print('Valor inválido! Só aceitamos valores < 11 e > -1')
else:
    print(f'Tabuada do {tabuada}:')
    for i in range(1, 11):
        print(f'{tabuada} X {i} = {tabuada * i}')
