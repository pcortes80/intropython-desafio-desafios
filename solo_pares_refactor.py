# Desafío - Números pares - Refactor
# Patricio Cortés
# G18
# 31-08-2021

# Usuario ingresa un número hasta el cual se mostrarán los números pares
numero_final = int(input("Ingrese un número hasta donde se mostrarán todos los pares:\n"))

i = 0
for i in range(numero_final + 1):
    # imprime el numero si el resto del modulo es 0
    if (i % 2 == 0) and (i != 0):
        print("Número par {}".format(i))
        
# Fin del Programa
