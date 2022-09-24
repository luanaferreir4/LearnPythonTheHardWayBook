coisas = ['a', 'b', 'c', 'd']
print(coisas[1])  # 'b'

coisas[1] = 'z'
print(coisas[1])  # 'z'

print(coisas)  # ['a', 'z', 'c', 'd']

print('-' * 20)

coisa = {'nome': 'Luana', 'idade': 21, 'altura': 1.57}

print(coisa['nome'])
print(coisa['idade'])
print(coisa['altura'])

print('-' * 10)
coisa['cidade'] = 'Taciba'
print(coisa['cidade'])

coisa[1] = 'Uau'
coisa[2] = 'Angel'
print(coisa[1])  # Uau
print(coisa[2])  # Angel
print(coisa)

del coisa['cidade']
del coisa[1]
del coisa[2]
print(coisa)  # {'nome': 'Luana', 'idade': 21, 'altura': 1.57}