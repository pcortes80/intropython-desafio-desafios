# Desafío - Generar Patrón
# Patricio Cortés
# G18
# 01-09-2021

# define variable "patron"
patron = ""

# Usuario ingresa un número de filas que se deben generar
filas = int(input("Ingrese el número de filas que se deben generar:\n"))

# iteraciones
for i in range(filas + 1):
    patron += "\n"
    for j in range(i + 1):
        if j != 0:
            patron += str(j)

# imprime el resultado en pantalla
print(patron)

# Fin del Programa