nome = input('Qual seu nome? ')
idade = input('Quantos anos você tem? ')
altura = input('Qual sua altura? ')
peso = input('Qual seu peso? ')

print(f'{nome}, você tem {idade} anos, tem {altura} de altura e pesa {peso}kg.')

# comandos pydoc: (pydoc é como uma documentação de todos os comandos Python no terminal.)
#
# direto no terminal:  `python -m pydoc {comando}` -> podemos até pesquisar libs como time.
#
# dentro do Python:  1) python
#                    2) help({comando})
#
# Para abrir a interface e poder procurar diretamente lá todas as documentações oficiais:
#
# python -m pydoc -p 314
#                  ^
#                porta
#
# `b` para abrir o server no navegador.
# `q` para sair do server.
