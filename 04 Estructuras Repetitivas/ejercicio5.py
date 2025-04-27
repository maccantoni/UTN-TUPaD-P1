#Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. 
# Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
numero = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el numero entre 0 y 9: "))
    intentos += 1
    if intento == numero:
        print(f"Bien! es {numero}. lo adivinastes en {intentos} intentos.")
        break
