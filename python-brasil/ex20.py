# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e
# limitando o fatorial a números inteiros positivos e menores que 16.

# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e
# limitando o fatorial a números inteiros positivos e menores que 16.

def fatorial(f):
  mult = 1
  fatorial = []
  for i in range(f, 0, -1):
        mult *= i
        fatorial.append(i)
  return fatorial, mult

repete = input('Quer calcular o fatorial? ')

while repete.upper() == 'S':

    f = int(input('Quer calcular o fatorial de qual número? '))
    valor_fatorial, mult = fatorial(f)
    print(valor_fatorial, '=', mult)
    repete = input('Quer novamente calcular o fatorial? ')
