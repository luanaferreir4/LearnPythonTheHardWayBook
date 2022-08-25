# Essa aqui é como seus scripts com argv:

def print_two(*args):
    arg1, arg2 = args
    print(f'arg1: {arg1}, arg2: {arg2}')


# Ok, aquele *args é desnecessário, podemos simplesmente fazer isso:

def print_two_again(arg1, arg2):
    print(f'arg1: {arg1}, arg2: {arg2}')


# Essa recebe apenas um argumento:

def print_one(arg1):
    print(f'arg1: {arg1}')


# Essa não recebe nenhum argumento:

def print_none():
    print('Eu não tenho nenhum argumento!')


# invocando/chamando funções
print_two('Luana', 'Ferreira')
print_two_again('Luana', 'Ferreira')
print_one('Lu')
print_none()
