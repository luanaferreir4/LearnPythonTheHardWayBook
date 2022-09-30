# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual
# ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome_de_usuario = input('Nome de usuário: ')
senha = input('Senha: ')

while nome_de_usuario == senha:
    print('Nome de usuário e senha iguais! Digite novamente!')
    nome_de_usuario = input('Nome de usuário: ')
    senha = input('Senha: ')