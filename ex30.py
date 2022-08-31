pessoas = 40
carros = 40
caminhoes = 15

if carros > pessoas:
    print("Deveríamos levar os carros.")
elif carros < pessoas:
    print("Não deveríamos levar os carros.")
else:
    print("Não conseguimos decidir.")


if caminhoes > carros:
    print("Tem caminhões demais.")
elif caminhoes < carros:
    print("Talvez possamos levar os caminhões.")
else:
    print("Ainda não conseguimos decidir.")


if pessoas > caminhoes:
    print("Ok. Bora levar apenas os caminhões.")
else:
    print("Ok, vamos ficar em casa então.")


# O que acontecerá se vários blocos elif forem True? 
# O Python inicia no topo e executa o primeiro bloco que é True, portanto,  executará apenas o primeiro.