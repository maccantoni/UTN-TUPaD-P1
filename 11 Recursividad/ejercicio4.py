""" Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto """

# Defino la función

# Convertir un número a binario

def decimal_a_binario(num):
    if num == 0:          # Caso base 1
        return "0" 
    elif num == 1:        # Caso base 2
        return "1" 
    else:
        return decimal_a_binario(num // 2) + str(num % 2) # Conversión a binario

# Programa principal

num_entero = int(input("Ingresa un número entero positivo: "))

if num_entero < 0:
    print("El número debe ser entero y positivo.")
else:
    num_binario = decimal_a_binario(num_entero)
    print(f"El {num_entero} convertido a binario es: {num_binario}")


