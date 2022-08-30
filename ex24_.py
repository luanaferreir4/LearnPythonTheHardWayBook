def formula_secreta(valor_inicial):
    jujubas = valor_inicial * 500
    potes_vidro = jujubas / 1000
    caixas = potes_vidro / 100
    return jujubas, potes_vidro, caixas


ponto_inicial = 10000
# jujubas, potes_vidro, caixas = formula_secreta(ponto_inicial)  # desestruturando.

formula = formula_secreta(ponto_inicial)

# Essa variável chama dentro dela a função ""

print("Teríamos {} jujubas, {} potes de vidro e {} caixas.".format(*formula))
