tipos_de_pessoas = 10
x = f"Há {tipos_de_pessoas} tipos de pessoas!"
# 10 pois 10 é 2 em números binários.

binario = "binário"
nao = "não"
y = f"Aquelas que sabem código {binario} e aquelas que {nao} sabem."

print(x)
print(y)

print(f"Se eu disse: {x}")
print(f"Eu também disse: '{y}'")


muito_engracada = False
avaliacao_piada = "Essa piada não é engraçada?! {}"
# Tá pedindo a validação dessa piada. Se ela fosse usaríamos True, se não, usamos False.
print(avaliacao_piada.format(muito_engracada))  # Outra maneira de usar formatted strings.

w = "Esse é o lado esquerdo de..."
e = "uma string com um lado direito."

print(w + e)

# 3. São 5 strings dentro de outras strings.

# 4. concatenação.

