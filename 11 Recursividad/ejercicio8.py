""" Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.

Ejemplos:

- contar_digito(12233421, 2) → 3
- contar_digito(5555, 5) → 4 
- contar_digito(123456, 7) → 0 """

# Función 

def contar_digito(numero, digito):
    if numero == 0:                                      # Caso base. No hay dígitos (o es 0)
        return 0
    elif numero % 10 == digito:                          # Obtengo el último dígito
        return 1 + contar_digito(numero // 10, digito)   # Sumo 1 y sigue
    else:
        return contar_digito(numero // 10, digito)

# Programa principal

numero = int(input("Ingresa un número entero y positivo: "))
digito = int(input("Ingresa un dígito del 0 al 9: "))

if numero < 0 or not (0 <= digito <= 9):
    print("Entrada inválida. El número debe ser positivo y el dígito debe estar entre 0 y 9.")
else:
    cantidad = contar_digito(numero, digito)
    print(f"El dígito {digito} aparece {cantidad} veces en {numero}.")