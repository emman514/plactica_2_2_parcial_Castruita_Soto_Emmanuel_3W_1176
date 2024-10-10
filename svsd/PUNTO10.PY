# Práctica 10
print("")  # Imprime una línea en blanco
print("Emmanuel_Castruita_Soto 3W_1176")  # Imprime el nombre 
print("")  # Imprime otra línea en blanco

# Define la función para verificar si un carácter es una vocal
def es_vocal(caracter):
    vocales = 'aeiouAEIOU'  # Define las vocales en minúsculas y mayúsculas
    return caracter in vocales  # Retorna True si el carácter es una vocal, False en caso contrario

# Pedir al usuario que ingrese una letra
letra = input("Ingresa una letra: ")

# Verificar que solo se ingrese un carácter
if len(letra) == 1:  # Si la longitud de la entrada es 1
    if es_vocal(letra):  # Llama a la función es_vocal para verificar
        print(f"{letra} es una vocal.")  # Imprime si es una vocal
    else:
        print(f"{letra} no es una vocal.")  # Imprime si no es una vocal
else:
    print("Por favor, ingresa solo un carácter.")  # Mensaje de error si se ingresan múltiples caracteres