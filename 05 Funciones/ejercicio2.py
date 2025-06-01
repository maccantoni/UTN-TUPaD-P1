""" Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. 
Llamar a esta función desde el programa principal solicitando el nombre al usuario."""

# Definir funcion

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Programa principal

nombre_ingresado = input("Ingresa tu nombre: ")
saludo = saludar_usuario(nombre_ingresado)
print(saludo)
