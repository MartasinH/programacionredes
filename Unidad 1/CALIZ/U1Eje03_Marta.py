'''
Descripcion del scrip:El participante aprenderá a utilizar y manipular el manejo de colecciones y
listas en el lenguaje de programación Python
Nombre:Marta Lugo López
Fecha:03/Oct/2024
Tema:Manejo de colecciones
'''

GIR0641 =()

 #Crea una lista llamada numeros_control e inicialízala con cinco números de control de tus compañeros. Véase la siguiente figura
numeros_control = [1223100388, 1223100125, 1223100476, 1223100478, 1223100111]
#Escribe la instrucción que imprima todo el contenido de la lista.
print(numeros_control)
#Mediante un foreach que itera la lista de los números de control
for numcontrol in numeros_control:
    #a. Solicite los nombres de los estudiantes de acuerdo al número control
    print("Ingresa el nombre del No. Control", numcontrol)
    #b. Mediante la función input solicite el nombre
    nombre = input("Ingresa el nombre: ")
    #Una vez que se capture el nombre agrega el dato a la colección haciendo corresponder el número de control con el nombre
    GIR0641[numcontrol]=nombre;
#Imprime el contenido de la colección.
print(GIR0641)
#Escribe un ciclo infinito que busque en la colección un número de control existente
