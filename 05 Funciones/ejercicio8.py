"""Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales."""

# Función

def calcular_imc(peso, altura):
    return peso / (altura * altura)  # (IMC = peso (kg) / (altura (m))^2)

# Programa

peso_ingresado = float(input("Ingresa tu peso en kg: "))
altura_ingresada = float(input("Ingresa tu altura en metros: "))

resultado_imc = round(calcular_imc(peso_ingresado,altura_ingresada),2)

print(f" Tu índice de masa corporal es de {resultado_imc}")