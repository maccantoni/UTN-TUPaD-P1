# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee: 
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 

nombre = input("Ingresa tu nombre: ")
texto = input("¿Como deseas que se muestre? Ingresa la opción que prefieras: 1. Todo en mayúsuculas. 2. Todo en minúsculas. 3. Primera letra en mayúscula: ")


if texto == "1":
    print(nombre.upper())
elif texto == "2":
    print (nombre.lower())
elif texto == "3":
    print(nombre.title())
else:
    pass