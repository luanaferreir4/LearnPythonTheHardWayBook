def somar(a, b):
    print(f'Somando {a} + {b}')
    return a + b


def subtrair(a, b):
    print(f'Subtraindo {a} - {b}')
    return a - b


def multiplicar(a, b):
    print(f'Multiplicando {a} * {b}')
    return a * b


def dividir(a, b):
    print(f'Dividindo {a} / {b}')
    return a / b


print('Vamos executar algumas operações com apenas as funções:')

idade = somar(30, 5)
altura = subtrair(78, 4)
peso = multiplicar(90, 2)
qi = dividir(100, 2)

print(f'Idade: {idade}, Altura: {altura}, Peso: {peso}, QI: {qi}')

print('Aqui está um quebra-cabeça!')

o_que_eh = somar(altura, subtrair(idade, multiplicar(qi, dividir(peso, 2))))
                                                            # 50 * 90 = 4500
                          # 35 - 4500 = -4.465
          # 74 - 4.465 = -4.391

print("Isso se torna: ", o_que_eh, "Você pode fazer isso a mão?")
