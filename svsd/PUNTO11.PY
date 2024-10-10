# Práctica 11
print("")  # Imprime una línea en blanco
print("Emmanuel_Castruita_Soto 3W_1176")  # Imprime el nombre
print("")  # Imprime otra línea en blanco

# Define la función para calcular la distancia dirigida entre dos números
def distancia_dirigida(num1, num2):
    # Calcula la distancia dirigida
    return num2 - num1  # Retorna la diferencia entre num2 y num1

# Pedir al usuario que ingrese dos números
num1 = float(input("Ingresa el primer número: "))  # Convierte la entrada a float
num2 = float(input("Ingresa el segundo número: "))  # Convierte la entrada a float

# Calcular la distancia dirigida
distancia = distancia_dirigida(num1, num2)  # Llama a la función y guarda el resultado

# Mostrar el resultado
print(f"La distancia dirigida entre {num1} y {num2} es: {distancia}")  # Imprime la distancia calculada