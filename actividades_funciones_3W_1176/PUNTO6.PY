# Práctica 6
print("")  # Imprime una línea en blanco
print("Emmanuel_Castruita_Soto 3W_1176")  # Imprime el nombre 
print("")  # Imprime otra línea en blanco

# Define la función para validar un email
def validar_email(email):
    if '@gmail.com' in email:  # Verifica si el email contiene '@gmail.com'
        return True  # Retorna True si es válido
    else:
        return False  # Retorna False si no es válido

# Captura de la dirección de email
email_usuario = input("Introduce tu dirección de Gmail: ")

# Validación del email
if validar_email(email_usuario):  # Llama a la función de validación
    print("La dirección de email es válida.")  # Mensaje si es válido
else:
    print("La dirección de email no es válida. Asegúrate de que sea un @gmail.")  # Mensaje si no es válido
