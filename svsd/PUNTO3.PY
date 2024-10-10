# Actividad 3
print("")  # Imprime una línea en blanco
print("Emmanuel_Castruita_Soto 3W_1176")  # Imprime el nombre 
print("")  # Imprime otra línea en blanco

# Solicita al usuario que ingrese un número entero positivo
n = int(input("Ingresa un número entero positivo: "))  

# Define la función para calcular el factorial de un número
def factorial(n):
    """
    Calcula el factorial de un número positivo.
    """
    if n < 0:  # Verifica si el número es negativo
        return "Número no válido"  # Retorna un mensaje de error si es negativo
    if n == 0:  # Caso especial: el factorial de 0 es 1
        return 1
    resultado = 1  # Inicializa el resultado
    for i in range(1, n + 1):  # Itera desde 1 hasta n
        resultado *= i  # Multiplica el resultado por i
    return resultado  # Retorna el resultado del factorial

# Imprime el mensaje y llama a la función factorial
print("Factorial de", n)  # Muestra el número cuyo factorial se calculará
print(factorial(n))  # Llama a la función y muestra el resultado
