from sys import argv

arquivo_atual, arquivo_de_texto = argv

print(f'Abrindo o arquivo: {arquivo_de_texto}')
txt = open(arquivo_de_texto, 'w')

print(f'Deseja esvaziar o arquivo {arquivo_de_texto}? (Sim: Enter, Não: Ctrl + C)')

input('? ')

print('Esvaziando o arquivo... Adeus!')
txt.truncate()

print('Agora preciso que escreva 2 linhas: ')
line1 = input('linha 1: ')
line2 = input('linha 2: ')

print('Agora vou passar essas linhas para o arquivo de texto...')

txt.write(line1)
txt.write('\n')
txt.write(line2)
txt.write('\n')

print('E finalmente fechamos o arquivo...')
txt.close()