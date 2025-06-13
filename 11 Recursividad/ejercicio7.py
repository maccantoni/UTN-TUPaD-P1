""" Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.

Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.

Ejemplos:
- contar_bloques(1) → 1 (1)
- contar_bloques(2) → 3 (2 + 1)
- contar_bloques(4) → 10 (4 + 3 + 2 + 1)"""

# Función

def contar_bloques(n):
    if n == 1:           # Caso base. Si hay un bloque, hay un solo nivel.
        return 1
    else:
        return n + contar_bloques(n - 1)   # Bloque/s del nivel actual menos uno del nivel que le sigue (para arriba)
    

# Programa principal

nivel_inferior = int(input("Ingresa la cantidad de bloques en el nivel más bajo: "))

if nivel_inferior < 1:
    print("El número debe ser al menos 1.")
else:
    total = contar_bloques(nivel_inferior)
    print(f"El total de bloques para la pirámide es: {total}")
