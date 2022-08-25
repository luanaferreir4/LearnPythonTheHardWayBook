# Comandos que podemos dar aos arquivos:
#
# close: fecha o arquivo.
# read: lê o conteúdo do arquivo. Você pode atribuir o resultado a uma variável.
# readline: lê apenas uma linha de um arquivo de texto.
# truncate: esvazia o arquivo. Tenha cuidado se o arquivo for importante.
# write('stuff'): escreve "stuff" no arquivo.
# seek(0): Move o local de leitura/gravação para o início do arquivo.
#

from sys import argv

arquivo_atual, nome_do_arquivo = argv

print(f'Vamos apagar {nome_do_arquivo}.')
print('Se não quiser apagar, aperte CTRL + C (^C).')
print('Se quiser apagar, aperte RETURN (ENTER).')

input('?')

print('Abrindo o arquivo...')
arquivo_alvo = open(nome_do_arquivo, 'w')  # 'w' significa "Quero abrir esse arquivo para escrever".

print('Esvaziando o arquivo. Adeus!')
arquivo_alvo.truncate()

print('Agora você vai responder 3 linhas de perguntas:')

line1 = input('line 1:')
line2 = input('line 2:')
line3 = input('line 3:')

print('Escrevendo isso nos arquivos...')

arquivo_alvo.write(line1)
arquivo_alvo.write('\n')
arquivo_alvo.write(line2)
arquivo_alvo.write('\n')  # Escreve no arquivo.
arquivo_alvo.write(line3)
arquivo_alvo.write('\n')

print('E finalmente, fechamos isso.')
arquivo_alvo.close()
