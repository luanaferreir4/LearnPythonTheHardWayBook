carros = 100
espaco_em_um_carro = 4
motoristas = 30
passageiros = 90
carros_nao_usados = carros - motoristas
carros_usados = motoristas
capacidade_carona = carros_usados * espaco_em_um_carro
media_passageiros_por_carro = passageiros / carros_usados

print("Há", carros, "carros disponíveis.")
print("Há apenas", motoristas, "motoristas disponíveis.")
print("Haverá", carros_nao_usados, "carros que não serão usados (vazios).")
print("Podemos transportar", capacidade_carona, "passageiros hoje.")
print("Nós temos", passageiros, "passageiros para dar carona hoje.")
print("Precisamos colocar em média", media_passageiros_por_carro, "passageiros em cada carro.")

# == : igual a

