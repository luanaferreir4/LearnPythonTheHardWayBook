from sys import exit


def sala_dourada():
    print("Essa sala está cheia de ouro. Quanto ouro você pega?")

    msg = "> "

    escolha = input(msg)
    if "0" in escolha or "1" in escolha:  # Se o número tiver 0 e 1. ex: 51, 31, 30, 50, etc.
        quanto = int(escolha)

        if quanto < 50:
            print("Legal, você não é ambicioso, você vence!")
            exit(0)
        else:
            morte("Seu bastardo ganancioso!")

    else:
        morte("Cara, aprenda a digitar um número.")


def sala_do_urso():

    msg = "> "

    print("Tem um urso aqui.")
    print("O urso tá cheio de mel.")
    print("O urso gordo está na frente de outra porta.")
    print("Como você irá mover o urso?")
    urso_move = False

    while True:
        escolha = input(msg)

        if escolha == "tomar o mel":
            morte("O urso olha para você e então dá um tapa na sua cara.")
        elif escolha == "provocar o urso" and not urso_move:
            print("o urso se moveu da porta.")
            print("Agora você pode passar por ela.")
            urso_move = True
        elif escolha == "provocar o urso" and urso_move:
            morte("O urso se irrita e mastiga sua perna.")
        elif escolha == "abra a porta" and urso_move:
            sala_dourada()
        else:
            print("Não faço idéia do que isso significa.")


def sala_do_cthulhu():

    msg = "> "

    print("Aqui você vê o Cthulhu mais malvado.")
    print("Ele, isso, onde quer que você esteja ele mirará em você e você ficará maluco(a).")
    print("Você foge por sua vida ou come sua cabeça?")

    escolha = input(msg)

    if "fujo" in escolha:
        comecar()
    elif "cabeça" in escolha:
        morte("Bem, isso estava delicioso!")
    else:
        sala_do_cthulhu()


def morte(porque):
    print(porque, "bom trabalho!")
    exit(0)


def comecar():

    msg = "> "

    print("Você está em um quarto escuro.")
    print("Há uma porta á sua direita e sua esquerda.")
    print("Qual você entraria?")

    escolha = input(msg)

    if escolha == "esquerda":
        sala_do_urso()
    elif escolha == "direita":
        sala_do_cthulhu()
    else:
        morte("Você trupica pela sala até morrer de fome!")


comecar()

# Ambas as funções, exit(0) e exit(1), são usadas para sair do programa, mas há uma grande diferença entre exit(0)
# e exit(1). A saída (0) mostra a finalização bem-sucedida do programa e a saída(1) mostra a finalização anormal do
# programa .
