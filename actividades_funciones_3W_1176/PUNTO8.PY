# Práctica 8
print("")  # Imprime una línea en blanco
print("Emmanuel_Castruita_Soto 3W_1176")  # Imprime el nombre 
print("")  # Imprime otra línea en blanco

# Solicita al usuario que ingrese tres valores
a = int(input("Ingresa el 1 valor: "))  # Primer valor
b = int(input("Ingresa el 2 valor: "))  # Segundo valor
c = int(input("Ingresa el 3 valor: "))  # Tercer valor

# Define la función para encontrar el mayor de tres números
def mayor_de_tres(a, b, c):
    """
    Devuelve el mayor de tres números.
    """
    return max(a, b, c)  # Utiliza la función max para encontrar el mayor

# Ejemplo de uso
print(mayor_de_tres(a, b, c))  # Llama a la función y muestra el resultado