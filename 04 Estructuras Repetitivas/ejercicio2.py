#Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

numero = input("Ingresa un numero entero: ")

#guardamos el número como string para poder contar los digitos
cant_digitos = len(str(numero))
print (f'El numero contiene: {cant_digitos} digitos.')