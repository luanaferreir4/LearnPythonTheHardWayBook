# Interações entre arquivos
#
# Escreveremos um script Python para copiar de um arquivo para outro:
#

from sys import argv 
from os.path import exists

arquivo_atual, do_arquivo, para_arquivo = argv

print(f'Copiando do arquivo {do_arquivo} para o arquivo {para_arquivo}')

# Poderíamos fazer esses dois com uma linha, como?

arquivo_entrada = open(do_arquivo)  # open_file = open(do_arquivo).read() | 'w' é padrão, não precisamos usar.
dado_entrada = arquivo_entrada.read()

print(f'O arquivo de entrada tem {len(dado_entrada)} bytes.')

print(f'O arquivo de saída existe? {exists(para_arquivo)}')
print('Pronto, aperte ENTER para continuar, CTRL + C para abortar.')

arquivo_saida = open(para_arquivo, 'w')
arquivo_saida.write(dado_entrada)

print('Tudo bem, processo concluído!')

arquivo_saida.close()
arquivo_entrada.close()