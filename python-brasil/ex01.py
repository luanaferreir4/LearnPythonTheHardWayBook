# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja
# inválido e continue pedindo até que o usuário informe um valor válido.

nota = float(input('Nota: '))

while nota < 0 or nota > 10:
    nota = float(input('Digite uma nota válida (0 - 10): '))
print("Valor computado! \n NOTA =", nota)
