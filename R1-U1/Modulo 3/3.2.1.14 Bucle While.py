bloques = int(input("Ingresa la cantidad de bloques: "))

# Inicializar las variables para la altura de la pirámide y la capa actual
altura = 0
capa = 1

# Mientras haya bloques suficientes para construir la capa actual
while bloques >= capa:
    # Restar los bloques necesarios para la capa actual
    bloques -= capa
    # Incrementar la altura de la pirámide
    altura += 1
    # Pasar a la siguiente capa
    capa += 1

# Imprimir la altura de la pirámide
print("La altura de la pirámide es:", altura)
