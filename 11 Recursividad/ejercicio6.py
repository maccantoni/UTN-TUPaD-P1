""" Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.

Restricciones:
- No se puede convertir el número a string.
- Usá operaciones matemáticas (%, //) y recursión.

Ejemplos:
- suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
- suma_digitos(9) → 9
- suma_digitos(305) → 8 (3 + 0 + 5)"""

# Defino función

def suma_digitos(n):
    if n < 10:           # Caso base
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

# Programa principal

numero = int(input("Ingresa un número entero positivo: "))

if numero < 0:
    print("El número debe ser positivo.")
else:
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado}")
