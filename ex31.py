print("""
Você entra em um quarto escuro com duas portas.
Você passa pela porta #1 ou porta #2?
""")

msg = "> "

door = input(msg)

if door == "1":
    print("""
    Tem um urso gigante aqui comendo um bolo de queijo.\n
    O que você faz?\n
    1. Leve o bolo.\n
    2. Grite com o urso.
    """)

    bear = input(msg)

    if bear == "1":
        print("O urso arranca sua cara. Bom trabalho!")
    elif bear == "2":
        print("O urso arranca sua perna fora. Bom trabalho!")
    else:
        print(f"Bem, fazer {bear} é provavelmente melhor. \nO urso foge")


elif door == "2":
    print("""
    Você olha para o abismo sem fim na retina de Cthulhu.\n
    1. Amoras.\n
    2. Prendedores de roupa de jaqueta amarela.
    3. Entendendo revólveres gritando melodias.
    """)

    insanity = input(msg)

    if insanity == "1" or insanity == "2":
        print("Seu corpo sobrevive energizado por um cérebro de gelatina.\nGood job!")
    else:
        print("A insanidade tomou conta dos seus olhos dentro de uma piscina de musgo.\nBom trabalho!")


else:
    print("Você tropeça e cai sobre uma faca e morre. Bom trabalho!")
