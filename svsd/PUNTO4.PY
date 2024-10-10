# Práctica 4
print("")  # Imprime una línea en blanco
print("Emmanuel_Castruita_Soto 3W_1176")  # Imprime el nombre 
print("")  # Imprime otra línea en blanco

# Solicita al usuario que ingrese el total de una factura
j = int(input("Ingresa total: "))  

# Define la función para calcular el total de una factura incluyendo IVA
def calcular_factura(j, iva=21):
    """
    Calcula el total de una factura incluyendo IVA.
    """
    total = j * (1 + iva / 100)  # Calcula el total aplicando el IVA
    print("IVA = 21%")  # Imprime el porcentaje del IVA
    return total  # Retorna el total calculado

# Ejemplo de uso de la función calcular_factura
print(calcular_factura(j))  # Llama a la función y muestra el resultado