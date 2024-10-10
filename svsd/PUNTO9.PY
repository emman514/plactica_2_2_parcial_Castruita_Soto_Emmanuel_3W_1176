# Práctica 9
print("")  # Imprime una línea en blanco
print("Emmanuel_Castruita_Soto 3W_1176")  # Imprime el nombre 
print("")  # Imprime otra línea en blanco

# Solicita al usuario que ingrese cuatro valores
a = int(input("Ingresa el 1 valor: "))  
b = int(input("Ingresa el 2 valor: "))  
c = int(input("Ingresa el 3 valor: "))  
d = int(input("Ingresa el valor 4: "))  

# Define la función para sumar todos los números de una lista
def suma(numeros):
    """
    Suma todos los números de una lista.
    """
    total = 0  # Inicializa el total
    for numero in numeros:  # Itera a través de cada número en la lista
        total += numero  # Suma el número al total
    return total  # Retorna el total

# Define la función para multiplicar todos los números de una lista
def multiplicar(numeros):
    """
    Multiplica todos los números de una lista.
    """
    resultado = 1  # Inicializa el resultado
    for numero in numeros:  # Itera a través de cada número en la lista
        resultado *= numero  # Multiplica el número al resultado
    return resultado  # Retorna el resultado

# Imprime la suma de los números ingresados
print("la suma de los numeros es ")#se implime este mensaje
print(suma([a, b, c, d]))  #implime el resultado de la suma
print("la mutiplicacion de los numeros es :")#se implime este mensaje
print(multiplicar([a, b, c, d]))  #implime el resultado de la multiplicacion