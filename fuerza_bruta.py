# Desafío - Fuerza Bruta
# Patricio Cortés
# G18
# 04-09-2021

# importa librerías
import string

# Usuario ingresa la contraseña
password = input("Ingrese contraseña:\n")

# toma el largo de la password
largo_password = len(password)

# carga abecedario desde libreria "string"
abc = string.ascii_lowercase

# define variable "intentos"
intentos = 0

# comienza a iterar
for i in range(largo_password):
    for j in abc:
        if password[i] == j:
            intentos += 1    # sumamos 1 intento más porque no hemos hecho match aun
            break            # si hacemos match salimos del for para comparar la siguiente letra
        intentos += 1        # antes de salirnos del for sumamos 1 al valor de intentos
                    
print("Se hicieron {} intentos.".format(intentos))

# Fin de Programa