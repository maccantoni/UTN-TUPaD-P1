""" Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro e imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función."""

# Funciones

def tabla_multiplicar(numero):
    for i in range (1,11):
        print(f"{numero} X {i} = {numero * i}")

# Programa

numero_ingresado = int(input(" Ingresa un número: "))

tabla_multiplicar(numero_ingresado)