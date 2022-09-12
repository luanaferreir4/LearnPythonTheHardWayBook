# Problema "medidas" 
# Fazer um programa para ler três medidas A, B e C. Em seguida, calcular e mostrar (imprimir os dados 
# com quatro casas decimais): 
# a) a área do quadrado que tem lado A 
# b) a área do triângulo retângulo que base A e altura B 
# c) a área do trapézio que tem bases A e B, e altura C 
# Exemplo 1: 
# Digite a medida A: 4.0
# Digite a medida B: 3.5
# Digite a medida C: 5.2
# AREA DO QUADRADO = 16.0000 
# AREA DO TRIANGULO = 7.0000 
# AREA DO TRAPEZIO = 19.5000 
# Exemplo 2: 
# Digite a medida A: 7.13
# Digite a medida B: 8.05
# Digite a medida C: 11.912
# AREA DO QUADRADO = 50.8369 
# AREA DO TRIANGULO = 28.6983 
# AREA DO TRAPEZIO = 90.4121 

def coletar_dados():
    print("Digite medida A:", end=' ')
    medida_a = float(input())
    print("Digite a medida B:", end=' ')
    medida_b = float(input())
    print("Digite a medida C:", end=' ')
    medida_c = float(input())
    return medida_a, medida_b, medida_c


def area_do_quadrado(medida_a):
    area_quadrado = medida_a * medida_a
    return area_quadrado


def area_do_triangulo_retangulo(medida_a, medida_b):
    area_triangulo_retangulo = (medida_a * medida_b) / 2
    return area_triangulo_retangulo


def area_do_trapezio(medida_a, medida_b, medida_c):
    area_trapezio = (medida_a + medida_b) * medida_c / 2
    return area_trapezio


def medidas():
    medida_a, medida_b, medida_c = coletar_dados()
    area_quadrado = area_do_quadrado(medida_a)
    area_triangulo_retangulo = area_do_triangulo_retangulo(medida_a, medida_b)
    area_trapezio = area_do_trapezio(medida_a, medida_b, medida_c)
    return f"AREA DO QUADRADO: {area_quadrado:.4f} - AREA DO TRIANGULO RETANGULO: {area_triangulo_retangulo:.4f} - " \
           f"AREA DO TRAPEZIO: {area_trapezio:.4f}"

