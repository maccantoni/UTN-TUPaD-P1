""" Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
Mostrar los resultados de forma clara."""

# Funciones

def operaciones_basicas(a, b):
    lista_operaciones = []
    suma = a + b
    resta = a - b
    multi = a * b
    division = a / b
    lista_operaciones.append(f"Suma = {suma}")
    lista_operaciones.append(f"Resta = {resta}")
    lista_operaciones.append(f"Multiplicación  = {multi}")
    lista_operaciones.append(f"División = {division}")

    return lista_operaciones


# Programa

num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))

lista_resultados = operaciones_basicas(num1, num2)

for operacion in lista_resultados:
    print(operacion)