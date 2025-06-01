""" Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. 
Solicitar al usuario los segundos y mostrar el resultado usando esta función."""

# Funciones

def segundos_a_horas(segundos):
    print(segundos / 3600)

# Programa

segundos_ingresados = int(input("Ingresa la cantidad de segundos que quieras calcular: "))
segundos_a_horas(segundos_ingresados)