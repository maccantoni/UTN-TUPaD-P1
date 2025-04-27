# Escribe un programa que permita al usuario ingresar 100 números enteros. 
# Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. 
# (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# Definimos e incializamos las variables
pares = 0
impares = 0
negativos = 0
positivos = 0
cantNum = 100
for i in range(cantNum):

    numero = int(input("Ingresa un nnmero entero: "))
    # Verificamos si el número es par o impar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero < 0:
        negativos += 1
    elif numero > 0:
        positivos += 1
        
# Imprimimos los resultados
print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)
print("Cantidad de negativos:", negativos)
print("Cantidad de positivos:", positivos)

