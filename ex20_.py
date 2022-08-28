from sys import argv

script, arquivo_texto = argv

arquivo_texto_aberto = open(arquivo_texto)


def imprima_uma_linha(conta_linhas, f):
    print(conta_linhas, f.readline())


linha = 1  # linha 1.

imprima_uma_linha(linha, arquivo_texto_aberto)

linha = linha + 1  # linha 2.

imprima_uma_linha(linha, arquivo_texto_aberto)

linha = linha + 1  # linha 3.

imprima_uma_linha(linha, arquivo_texto_aberto)

linha = linha + 1

imprima_uma_linha(linha, arquivo_texto_aberto)