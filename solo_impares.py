# Desafío - Números impares
# Patricio Cortés
# G18
# 31-08-2021

# Usuario ingresa un número hasta el cual se mostrarán los números impares
numero_final = int(input("Ingrese un número hasta donde se mostrarán todos los impares:\n"))

i = 0
for i in range(numero_final + 1):
    # imprime el numero si el resto del modulo es distinto a cero, a diferencia de los pares
    if (i % 2 != 0) and (i != 0):
        print("Número impar {}".format(i))
        
# Fin del Programa
