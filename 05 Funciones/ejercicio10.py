"""Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta función."""

# Función

def calcular_promedio(a, b, c):
    print((a + b + c) / 3)

# Programa

num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))
num3 = int(input("Ingresa un número mas: "))

calcular_promedio(num1,num2,num3)