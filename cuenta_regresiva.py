# Desafío - Reemplazar instrucción for por while
# Patricio Cortés
# G18
# 30-08-2021

"""
# Reemplazar este bloque
cuenta_regresiva = int(input("Ingrese un número para comenzar la cuenta\n"))
for i in range(cuenta_regresiva):
    tmp = cuenta_regresiva
    print("Iteración {}".format(tmp - i))
"""
# Ciclo while que reemplaza a for anterior
cuenta_regresiva = int(input("Ingrese un número para comenzar la cuenta\n"))
while cuenta_regresiva > 0:
    print("Iteración {}".format(cuenta_regresiva))
    cuenta_regresiva -= 1 
 
# Fin del Programa