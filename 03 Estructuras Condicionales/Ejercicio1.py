# TRABAJO PRÁCTICO 3: ESTRUCTURAS CONDICIONALES
# ALUMNO: CANTONI MARIA MACARENA

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Por favor, ingresá tu edad: "))

if (edad >= 18):
    print("Es mayor de edad")
else:
    print("Es menor de edad")