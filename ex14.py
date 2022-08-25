from sys import argv

file, nome_de_usuario = argv

prompt = '> '  # Vai aparecer isso antes do que vamos escrever em seguida.

print(f'Oi {nome_de_usuario}, Eu sou o arquivo {file}')
print('Gostaria de te fazer algumas perguntas.')

print(f'Você gosta de mim, {nome_de_usuario}?')
gosto = input(prompt)

print(f'Onde você mora, {nome_de_usuario}?')
endereco = input(prompt)

print(f'Que tipo de computador você tem?')
computador = input(prompt)

print(f'''
Tudo bem, então você disse {gosto} sobre gostar de mim.
Você mora em {endereco}. Não tenho certeza de onde é.
E você tem um computador {computador}. Legal =D
''')


