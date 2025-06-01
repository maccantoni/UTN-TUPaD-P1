""" Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
Calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados."""

import math

# Funciones

def calcular_area_circulo(radio):
    return math.pi * radio * radio # area: π * r²

def calcular_perimetro_circulo(radio):
    return  2 * math.pi * radio  # 2π * r


# Programa

radio_ingresado = int(input("Ingresa el radio del círculo: "))

resultado_area = calcular_area_circulo(radio_ingresado)
resultado_perimetro = calcular_perimetro_circulo(radio_ingresado)

print(f"el área del círculo es {resultado_area}. Y el perímetro es {resultado_perimetro}")