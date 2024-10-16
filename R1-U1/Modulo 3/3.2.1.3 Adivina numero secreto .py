

num_secreto = 111

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
numero = int(input ("Adivina el numero"))

while  numero != num_secreto :
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")

    numero = int(input ("Intentalo otra vez :"))
print(num_secreto ," ¡Bien hecho, muggle! Eres libre ahora." )