def formula_secreta(valor_inicial):
    jujubas = valor_inicial * 500
    potes_vidro = jujubas / 1000
    caixas = potes_vidro / 100
    return jujubas, potes_vidro, caixas


valor_inicial = 10000
jujubas, potes_vidro, caixas = formula_secreta(valor_inicial)

print(f"Teríamos {jujubas} jujubas, {potes_vidro} potes de vidro e {caixas} caixas.")