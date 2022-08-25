# String de formatação
# nome = "Luana"
# print(f"Meu nome é {nome}")

name = "Zed A. Shaw"
age = 35
height = 74  # polegadas
weight = 180  # libras
eyes = "Blue"
teeth = "White"
hair = "Brown"

print(f"Let's talk about {name}")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# Essa linha é capciosa, tente escrever exatamente como está.
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# 2. Tente escrever algumas variáveis que convertam polegadas e libras em centímetros e quilogramas.
# Não digite apenas as medidas, calcule-as no python.

to_cm = height * 2.54
to_kg = weight / 2.205

print(f"{height} polegadas em centímetros: {to_cm}cm.")
print(f"{weight} libras em quilogramas: {to_kg}kg.")
# Poderia arredondar números com ponto flutuante com `round()`
