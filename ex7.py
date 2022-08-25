print('Mari tinha um cordeirinho.')
print('A lã dele era branca como {}'.format('neve'))
print('E todo lugar que a Mari foi.')

print('.' * 10)  # O que isso fez? '..........'

a1 = 'C'
a2 = 'h'
a3 = 'e'
a4 = 'e'
a5 = 's'
a6 = 'e'
a7 = 'B'
a8 = 'u'
a9 = 'r'
a10 = 'g'
a11 = 'e'
a12 = 'r'

# Concatena todas as strings formando 'CheeseBurger' e com o kwarg "end=''" separado por vírgulas podemos dar espaços a
# palavras concatenadas:
print(a1 + a2 + a3 + a4 + a5 + a6, end=' ')  # end torna as frases inline, sem quebrá-las em duas.
print(a7 + a8 + a9 + a10 + a11 + a12)

# Output:
# Cheese Burger

# Diferente do uso de sep que as quebra:
print(a1 + a2 + a3 + a4 + a5 + a6, sep=' ')
print(a7 + a8 + a9 + a10 + a11 + a12)

# Output:
# Cheese
# Burger
