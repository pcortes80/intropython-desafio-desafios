# Desafío - Generador de Lorem ipsum
# Patricio Cortés
# G18
# 01-09-2021

# Usuario ingresa el número de párrafos
num_parrafos = int(input("Ingrese el número de párrafos deseados:\n"))

# define la variable "lorem" que guardará el párrafo
lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse porta ligula ac tempor placerat. Integer ligula odio, malesuada nec varius vitae, aliquet id orci. Morbi ullamcorper ante sit amet mattis ornare. Pellentesque at ante eget magna auctor hendrerit eu sit amet dolor. Curabitur vitae magna diam. Vivamus in porta elit. Maecenas porttitor lectus quis risus tincidunt, eget porta est cursus. Etiam elit enim, convallis vitae purus sed, varius viverra nulla."

# iteraciones
for i in range(num_parrafos):
    texto = lorem + "\n" # le agrega un salto de linea al párrafo
    print(texto) # imprimer el párrafo 
    
# Fin de Programa


