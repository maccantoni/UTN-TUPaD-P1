""" Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 
𝑛^𝑚 = 𝑛 ∗ 𝑛 (𝑚−1). Prueba esta función en un algoritmo general."""

# Función

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
    
# Programa principal

base = int(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente. Debe ser entero y positivo: "))

if exponente < 0:
    print("El exponente debe ser un número entero y positivo.")
else:
    resultado = potencia(base, exponente)
    print(f"{base}^{exponente} = {resultado}")
