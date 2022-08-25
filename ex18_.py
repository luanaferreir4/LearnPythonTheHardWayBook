def print_two(*args):

    arg1, arg2 = args

    print(f'arg1: {arg1}, arg2: {arg2}')


def print_two_again(arg1, arg2):

    print(f'arg1: {arg1}, arg2: {arg2}')


def print_one(arg1):

    print(f'arg1: {arg1}')


def print_none():

    print('Não tem nenhum argumento aqui!')


# chamando função:

print_two('Luana', 'Ferreira')
print_two_again('Luana', 'Ferreira')
print_one('Lu')
print_none()
