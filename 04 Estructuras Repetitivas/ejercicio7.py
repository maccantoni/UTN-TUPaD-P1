#Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

numero = int(input("ingresa un numero entero positivo: "))
if numero < 0:
    print("Por favor, ingresa un nnmero entero positivo.")
    exit()
suma = 0
for i in range(1, numero + 1):
    suma += i
print("La suma de los numeros entre 0 y", numero, "es:", suma)