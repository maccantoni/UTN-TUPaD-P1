#Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.


suma_total = 0

# Bucle para el ingreso de los numeros
while True:
    numero = int(input("Ingrese un numero entero (0 para salir): "))
    
    # Verificar si el número ingresado es 0
    if numero == 0:
        # Si es 0, salir del bucle, el break fuerza la salida del bucle
        break
    
    # Sumar el número ingresado a la suma total
    suma_total += numero

# Mostrar la suma total acumulada
print("La suma total acumulada es:", suma_total)