# Desafío - Sumar pares
# Patricio Cortés
# G18
# 30-08-2021

# Usuario ingresa un número hasta el cual se sumarán todos los números pares
numero_final = int(input("Ingrese un número hasta donde se sumarán todos los pares:\n"))

i = 0
suma = 0
contain = ""
for i in range(numero_final + 1):
    # imprime el numero si el resto del modulo es 0 y ademas i es distinto a 0
    if (i % 2 == 0) and (i != 0):
        # print("Número par {}".format(i))
        # contain = contain + " " + "+" + " " + str(i)
        # print("{} + {}".format(i,contain))
        suma += i # suma los pares encontrados

print("suma de pares = {}".format(suma))


# Fin del Programa
