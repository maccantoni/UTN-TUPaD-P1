# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
# El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("¿En que hemisferio te encuentras? Ingresa N si estás en el hermiferio Norte, o S si estas en el hemisferio Sur: ").upper()
mes = int(input("Ingresa el mes del año (del 1 al 12): "))
dia = int(input("Ingresa que día es hoy (del 1 al 31): "))

if hemisferio == "N":
    if (mes == 12 and dia >=21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        print("Estas en invierno.")
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        print("Estas en primavera.")
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        print("Estas en verano.")
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        print("Estas en otoño")
    else:
        print("Ingresa una opción válida")

if hemisferio == "S":
    if (mes == 12 and dia >=21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        print("Estas en verano.")
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        print("Estas en otoño.")
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        print("Estas en invierno.")
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20): 
        print("Estas en primavera")
    else:
        print("Ingresá una opción válida")