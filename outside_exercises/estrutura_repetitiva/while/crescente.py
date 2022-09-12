msg = "> "

print('Digite o primeiro número:')
x = int(input(msg))
print("Digite o segundo número:")
y = int(input(msg))

while x != y:

    if x > y:
        print("Decrescente")
    else:
        print("Crescente")
    print('Digite o primeiro número:')
    x = int(input(msg))
    print("Digite o segundo número:")
    y = int(input(msg))
