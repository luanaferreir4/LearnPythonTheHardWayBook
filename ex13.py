# - Como fazer um script que também aceita argumentos:

from sys import argv

script, first, second, third = argv  # descompacta o argv.

print('O nome do script é', script)
print('Sua primeira variável é', first)
print('Sua segunda variável é', second)
print('Sua terceira variável é', third)


# Como colocar no terminal?
#
# python ex13.py 1st 2nd 3rd (adicionando argumentos)
#          ^      ^   ^   ^
#        script first sec third
#
# - Output:
#
# O nome do script é ex13.py
# Sua primeira variável é 1st
# Sua segunda variável é 2nd
# Sua terceira variável é 3rd
#
# - *Se der esse erro:
# Traceback (most recent call last):
#  File "C:\Users\luana\lpythw\ex13.py", line 5, in <module>
#    script, first, second, third = argv  # descompacta o argv.
# ValueError: not enough values to unpack (expected 4, got 3)
#
# Significa que colocamos menos argumentos que deveríamos.
# 
# sys é um módulo.
#
# `import` é usado para trazermos mais recursos para dentro do 
# programa em Python.

