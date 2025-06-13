""" Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique """

# pos0 -> 0
# pos1 -> 1
# pos2 -> pos1 + pos0 = 0 + 0 = 1
# pos3 -> pos2 + pos1 = 1 + 1 = 2
# pos4 -> pos3 + pos2 = 2 + 1 = 3
# pos5 -> pos4 + pos3 = 3 + 2 = 5

# posN -> posN-1 + posN-2

# Defino la función 

def fibonacci_recur(posicion):
    if posicion == 0:   # Caso base 1
        return 0
    elif posicion == 1:  # Caso base 2
        return 1
    else:
        return fibonacci_recur(posicion-1) + fibonacci_recur(posicion-2)

# Programa principal

pos = int(input("Ingresa la posición hasta la que deseas calcular la serie Fibonacci: "))

if pos < 0:
    print("Debes ingresar un número positivo y entero.")
else:
    print(f"Serie hasta la posición {pos}: ")
    for i in range(pos + 1):
        print(f"F({i}) = {fibonacci_recur(i)}")