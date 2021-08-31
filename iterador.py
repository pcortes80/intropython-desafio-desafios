# Desafío Reemplazar while por for
# Patricio Cortés
# G18
# 30-08-2021

"""
# Reemplazar la siguiente estructura:
i = 0
while i < 50:
    print("Iteración {}".format(i + 1))
    i +=1
"""
# Ciclo for que reemplaza el anterior while
i = 0
for i in range(50):
    print("Iteración {}".format(i + 1))
    i +=1

# Fin del programa