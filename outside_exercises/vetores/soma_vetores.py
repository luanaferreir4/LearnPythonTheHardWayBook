# Problema "soma_vetores" 
# Faça um programa para ler dois vetores A e B, contendo N elementos cada. Em seguida, gere um 
# terceiro vetor C onde cada elemento de C é a soma dos elementos correspondentes de A e B. Imprima 
# o vetor C gerado. 
# Exemplo: 
# Quantos valores vai ter cada vetor? 6
# Digite os valores do vetor A: 
# 8 
# 2 
# 11 
# 14 
# 13 
# 20 
# Digite os valores do vetor B: 
# 5 
# 10 
# 3 
# 1 
# 10 
# 7 
# VETOR RESULTANTE: 
# 13 
# 12 
# 14 
# 15 
# 23 
# 27 

a = []
b = []

n = int(input("Quantos valores vai ter cada vetor? "))

print("Digite os valores do vetor A: ")
for i in range(0, n):
    numero_a = int(input())
    a.append(numero_a)
    
    
print("Digite os valores do vetor B: ")
for j in range(0, n):
    numero_b = int(input())
    b.append(numero_b)

print("VETOR RESULTANTE:")
for k in range(0, n):
    print(f"{a[k] + b[k]}")