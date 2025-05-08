# Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:

# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

lista_3 = compras[2]
lista_3.append("jugo")

lista_2 = compras[1]
lista_2[1] = "tallarines"

lista_1 = compras[0]
lista_1.remove("pan")

print(compras)