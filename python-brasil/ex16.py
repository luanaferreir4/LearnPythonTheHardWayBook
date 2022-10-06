# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa que gere a série até que o valor seja maior que 500. 


fibonacci = [0]
i = 1

while fibonacci[-1] < 500:
    if len(fibonacci) < 2:
        fibonacci.append(i)
    else:
        soma = fibonacci[-2] + fibonacci[-1]
        fibonacci.append(soma)
    print(fibonacci)

