"""Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados."""

# Funciones 

def informacion_personal(nombre, apellido, edad, residencia):
    print(f" Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Programa principal

nombre_ingresado = input("Ingresa tu nombre: ")
apellido_ingresado = input("Ingresa tu apellido: ")
edad_ingresada = input("Ingresa tu edad: ")
residencia_ingresada = input("Ingresa tu lugar de residencia: ")

informacion_personal(nombre_ingresado, apellido_ingresado, edad_ingresada, residencia_ingresada)

# informacion_personal(nombre=nombre_ingresado, edad=edad_ingresada,residencia=residencia_ingresada, apellido=apellido_ingresado)