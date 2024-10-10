# Práctica 7
print("")  # Imprime una línea en blanco
print("Emmanuel_Castruita_Soto 3W_1176")  # Imprime el nombre 
print("")  # Imprime otra línea en blanco

# Define la función para obtener la longitud de la última palabra
def longitud_ultima_palabra(texto):
    # Eliminar espacios en blanco y dividir por espacios
    palabras = texto.strip().split()  # Limpia el texto y lo divide en palabras
    
    # Verificar si hay palabras en la lista
    if palabras:  # Si la lista no está vacía
        return len(palabras[-1])  # Regresa la longitud de la última palabra
    else:
        return 0  # Si no hay palabras, devolver 0

# Captura de texto del usuario
texto_usuario = input("Introduce una cadena de texto: ")

# Obtener longitud de la última palabra
longitud = longitud_ultima_palabra(texto_usuario)  # Llama a la función y guarda el resultado

# Mostrar el resultado
print(f"La longitud de la última palabra es: {longitud}")  # Imprime la longitud
