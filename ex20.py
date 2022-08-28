from sys import argv

script_atual, arquivo_entrada = argv


def imprima_tudo(f):
    print(f.read())


def rebobinar(f):
    f.seek(0)  # seek(0): Move o local de leitura/gravação para o início do arquivo.


def imprima_uma_linha(conta_linhas, f):
    print(conta_linhas, f.readline())  # conta_linhas: geralmente usando while ou for.


arquivo_atual = open(arquivo_entrada)


print('PRIMEIRO, vamos printar o arquivo inteiro: \n')

imprima_tudo(arquivo_atual)

print('Agora vamos rebobinar, tipo uma fita-cassete!')

rebobinar(arquivo_atual)

print('Vamos printar 3 linhas:')

linha_atual = 1  # linha 1.

imprima_uma_linha(linha_atual, arquivo_atual)  # imprime tal arquivo em tal linha.

linha_atual = linha_atual + 1  # linha 2.

imprima_uma_linha(linha_atual, arquivo_atual)

linha_atual = linha_atual + 1  # linha 3.

imprima_uma_linha(linha_atual, arquivo_atual)

linha_atual = linha_atual + 1  # linha 4.

imprima_uma_linha(linha_atual, arquivo_atual)

linha_atual = linha_atual + 1  # linha 5.

imprima_uma_linha(linha_atual, arquivo_atual)

