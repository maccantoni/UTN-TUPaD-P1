#Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores

valor1 = int(input("ingresa el primer valor: "))
valor2 = int(input("ingresa el segundo valor: "))
suma = 0

# Comprobamos cual es el mayor de los dos valores
if valor1 < valor2:
    for i in range(valor1 + 1, valor2):
        suma += i
else:
    for i in range(valor2 + 1, valor1):
        suma += i

print("La suma de los nnmeros entre", valor1, "y", valor2, "es:", suma)