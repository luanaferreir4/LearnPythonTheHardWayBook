# Faça uma função que recebe um número ( n ) e retorna o n-ésimo número da sequência de fibonacci.


# 1 1 2 3 5

#     -2 -1

def fibonacci(n):

    somas = []

    for i in range(0, n):

        if len(somas) == 0 or len(somas) == 1:
            soma = 1
            somas.append(soma)
        else:
            soma = somas[-1] + somas[-2]
            somas.append(soma)

    return somas[n-1]


print(fibonacci(3))