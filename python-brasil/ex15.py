# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo. 

n = int(input('Termo final da série de Fibonacci: '))

fibonacci = []

for i in range(0, n):
    if len(fibonacci) < 2:
        fibonacci.append(i)
    else:
        soma = fibonacci[-2] + fibonacci[-1] 
        fibonacci.append(soma)
print(fibonacci)


