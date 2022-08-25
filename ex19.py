def queijo_e_bolachas(qntd_queijo, pacotes_bolhachas):
    print(f'Você tem {qntd_queijo} queijos!')
    print(f'Você tem {pacotes_bolhachas} pacotes de bolachas!')
    print('É o suficiente para uma festa!')
    print('Pegue um cobertor. \n')


# diretamente:
queijo_e_bolachas(20, 30)

# usando variáveis:
qntd_queijo_ = 10
pacotes_bolachas = 50
queijo_e_bolachas(qntd_queijo_, pacotes_bolachas)

# usando a matemática:
queijo_e_bolachas(10 + 20, 5 + 6)

# combinando matemática e variáveis:
queijo_e_bolachas(qntd_queijo_ + 100, pacotes_bolachas + 1000)
