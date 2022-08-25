from sys import argv

file, nome, idade, cidade_natal = argv  # descompactando.

print('Estamos no arquivo', file)
print('Meu nome é', nome)
print('Minha idade é', idade, 'anos')
print('Nasci em', cidade_natal)

print('Alguma sugestão de melhora aos nossos programas?', end=' ')
user_input = input()
print('Sugestão de melhora:', user_input)

# python ex13_.py Luana 21 "São Paulo" -> Quando algo são duas palavras ou mais, usar nos argumentos " antes e " depois.
# '' não funciona nesse caso.
