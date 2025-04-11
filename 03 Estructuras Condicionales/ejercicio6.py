# 6) escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 


import random
from statistics import mode, median, mean 

# Se genera la lista de numeros aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 

# imprimo en pantalla la lista de números generados para tener mas info
print(f"Los números generados son {numeros_aleatorios}")

# Defino cada una de las variables con los parámetros.
media = mean(numeros_aleatorios)
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)

# Calculo los sesgos
if (media > mediana) and (mediana > moda):
    print("Hay sesgo positivo")
elif (media < mediana) and (mediana < moda):
    print("Hay sesgo negativo")
else:
    print("No hay sesgo")
