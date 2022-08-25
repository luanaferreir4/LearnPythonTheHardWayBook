from sys import argv

arquivo_atual, arquivo_de_texto = argv

txt = open(arquivo_de_texto)  # abertura de arquivo.

print(f'Aqui está o seu arquivo {arquivo_de_texto}:')

print(txt.read())  # leitura.

txt.close()

print('Digite o nome do arquivo novamente:')
nome_do_arquivo = input('> ')

print(f'Aqui está o seu arquivo: {nome_do_arquivo}')

txt_again = open(nome_do_arquivo)
print(txt_again.read())

txt_again.close()

# open() = abrir arquivo pelo nome dele.
# .read() = lê arquivo que antes já foi aberto só que dessa vez usando o método {filename}.read().
# .close() = fecha arquivo após o uso.
