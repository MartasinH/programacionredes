
numero = int(input("Ingrese un número entero positivo: "))
pasos = 0

while numero != 1:
    pasos += 1  
    if numero % 2 == 0:  
        numero = numero // 2
        print(numero)
    else:  
        numero = 3 * numero + 1
        print(numero)

print("pasos =", pasos)