
'''
Descripcion del scrip:El participante aprenderá a utilizar y manipular el manejo de listas en el
lenguaje de programación Python
Nombre:Marta Lugo López
Fecha:03/Oct/2024
Tema:Manejo de listas
'''
#Escribe las instrucciones para agregar comentarios en Python como: Descripción delejercicio, nombre del participante, fecha de creación y tema.

print("Manejo de Listas")
print("Marta Lugo López")
print("Fecha:02/oct/2024")
print("Tema:Manejo de Listas ")

#Escribe la instrucción para realizar un salto de línea
print( )
#Crea una lista con cuatro de tus mejores compañeros del grupo: Francisco, Pedro,Juan, Fernando

nombres = ['Pedro', 'Pablo', 'Barron', 'Miranda']

#Escribe la instrucción para desplegar el tamaño de la lista a través de la leyenda “Eltamaño de la lista es”.

print(f"El tamaño de la lista es: {len(nombres)}")

#Escribe la instrucción para imprimir el contenido de la lista a través de la leyenda “Elcontenido de la lista es ”

print(f"El contenido de la lista es: {nombres}")
 #. Cambiar el segundo elemento de la lista por “Joaquín”
nombres[1] = "Joaquín"
 
#Agrega un elemento más a la lista con el nombre “Luis Miguel”, utiliza la instrucción:nombres.append()

nombres.append("Luis Miguel")
#Elimina el tercer elemento de la lista

del nombres[2]

#Despliega la lista en orden inverso y separados con un carácter cada nombre
print('*'.join(nombres[::-1]))