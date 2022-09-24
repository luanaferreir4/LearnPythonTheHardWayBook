# O Python é chamado de "linguagem de programação orientada a objetos". Isso significa que há uma construção
# nele chamada classe, que permite estruturar o software de um modo particular.

# Os módulos são como Dicionários

# Se tiver uma chave apple e quiser obtê-la, faça isso:
minha_coisa = {'apple': 'EU SOU MACAS!'}
print(minha_coisa['apple'])

# Mantenha a idéia de "obter X de Y" em mente e agora pense nos módulos. Você criou alguns até agora e deve
# saber que eles são:

# 1. um arquivo Python com algumas funções e variáveis...
# 2. que pode importar...
# 3. e acessar as funções ou variáveis com o operador . (ponto).

import minha_coisa
minha_coisa.apple()
print(minha_coisa.tangerina)

# minha_coisa['apple']  # obtém um apple do dic
# minha_coisa.apple()  # Obtém um apple do módulo
# minha_coisa.tangerina  # mesma coisa, é apenas uma variável

# Agora, tenho 3 modos de obter coisas de coisas:

# estilo dic
minha_coisa['apples']

# estilo modulo
minha_coisa.apples()

# estilo classe
coisa = MinhaCoisa()
coisa.apples()
print(coisa.tangerine)
