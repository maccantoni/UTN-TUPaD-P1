""" Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario"""

# Funcion

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)
    

# Programa

# Pido al usuario que ingrese un número
num = int(input("Ingresa un número entero: "))

# Valido que el núm ingresado sea entero y positivo
# Uso for para recorrer los nums del 1 al ingresado, llamando a la funcion factorial definida arriba.
if num < 1:
    print("El número debe ser entero y positivo")
else:
    print(f"Los factoriales del 1 a {num}: ")
    for i in range(1, num +1):                 # Recorre desde el 1, sumando a num 1 en cada vuelta hasta el numero ingresado.
        print(f"{i}! = {factorial(i)}")

