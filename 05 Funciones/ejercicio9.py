""" Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función."""

# Función

def celsius_a_fehrenheit(celsius):
   return 1.8 * celsius + 32             # 1.8 * C + 32

# Programa

temp_en_celsius = float(input("Ingrese la temperatura en Celsius: "))

conversion_celsius_far = celsius_a_fehrenheit(temp_en_celsius)

print(f"{temp_en_celsius}° Celsius equivalen a {conversion_celsius_far} Fahrenheit")