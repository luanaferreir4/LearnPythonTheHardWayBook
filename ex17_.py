from sys import argv
from os.path import exists

arquivo_atual, de_arquivo, para_arquivo = argv

print(f'Copiando arquivo {de_arquivo} para o arquivo {para_arquivo}')

print(f'O tamanho do arquivo {de_arquivo} é {len(de_arquivo)} bytes.')

print('Abrindo e lendo o arquivo {}'.format(de_arquivo))
abrir_arquivo1 = open(de_arquivo).read() # Abrir arquivo e lê-lo.
#ler_arquivo1 = abrir_arquivo1.read()

print(f'O arquivo de saída existe? {exists(para_arquivo)}')

print('Abrindo arquivo {} para escrita.'.format(para_arquivo))
abrir_arquivo2 = open(para_arquivo, 'w')  # abrir arquivo 2 para escrita.
print('Escrevendo no arquivo {}...'.format(para_arquivo))
abrir_arquivo2.write(abrir_arquivo1)  # escrever no arquivo 2 como no arquivo 1.

