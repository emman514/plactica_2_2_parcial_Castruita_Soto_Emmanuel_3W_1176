# Práctica 5
print("")  # Imprime una línea en blanco
print("Emmanuel_Castruita_Soto 3W_1176")  # Imprime el nombre 
print("")  # Imprime otra línea en blanco

# Solicita al usuario que ingrese un número para calcular el área
numero = input("Ingresa número para calcular área: ")
h = int(numero)  # Convierte la entrada a entero
numero1 = input("Ingresa número para calcular área y volumen: ")
g = int(numero1)  # Convierte la entrada a entero
import math  # Importa la biblioteca matemática

# Define la función para calcular el área de un círculo
def area_circulo(radio):
    """
    Calcula el área de un círculo.
    """
    return math.pi * radio ** 2  # Calcula el área usando la fórmula

# Define la función para calcular el volumen de un cilindro
def volumen_cilindro(radio, altura):
    """
    Calcula el volumen de un cilindro.
    """
    area = area_circulo(radio)  # Llama a la función para calcular el área
    return area * altura  # Calcula el volumen multiplicando el área por la altura

# Ejemplo de uso de las funciones
print(area_circulo(h))  # Llama a la función y muestra el área
print(volumen_cilindro(h, g))  # Llama a la función y muestra el volumen
