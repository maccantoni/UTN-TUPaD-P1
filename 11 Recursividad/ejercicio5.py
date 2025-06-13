""" Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.

Requisitos:
- La solución debe ser recursiva.
- No se debe usar [::-1] ni la función reversed()."""

""" Palabra o frase cuyas letras están dispuestas de tal manera
    que resulta la misma leída de izquierda a derecha que de derecha a izquierda"""

# Función

def es_palindromo(palabra):
    if len(palabra) <= 1:                     # Caso base 1 - Palabra con 0 o 1 letra.
        return True
    elif palabra[0] != palabra[-1]:           # Caso base 2 - Primera letra es distinta de la última.
        return False
    else:
        return es_palindromo(palabra[1:-1])    # Si la primera letra y la última son iguales se evaluan las del medio.


# Programa princial

texto = input("Ingresa una palabra sin espacios ni tildes: ").lower()

if es_palindromo(texto):
    print(f"'{texto}' es un palíndromo.")
else:
    print(f"'{texto}' no es un palíndromo.")