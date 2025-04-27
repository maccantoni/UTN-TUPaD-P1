# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. 
# Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingresa un numero: ")
invertido = ""
cantidad = len(numero)
for i in range(cantidad):
    # Se recorre el numero de atras hacia adelante 
    # y se va concatenando el nuevo numero
    invertido += numero[cantidad - 1 - i]

print("El numero invertido es:", invertido)