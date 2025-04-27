# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. 
# (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor). 

#Definimos e inicializamos la variables

suma = 0
cantNum = 100
i = 0
media = 0
numero = 0

#Mientras i sea menor que cantidad
while i < cantNum:
    numero = int(input("Ingresa un numero entero: "))
    suma += numero
    i += 1

#Calculamos la media dividiendo la suma entre la cantidad
media = suma / cantNum
print("La media de los numeros ingresados es:", media)