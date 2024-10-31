try:
    num  = int(input("Ingresa tu dedad "))
    res = 1/num
    print (num)
except ValueError as error :
    print(f"Estas haciendolo malllllll \n Es ingresar un numero ")
except ZeroDivisionError:
    print("Ingresa un numero distinto a cero changana")
#el EXCEPTION avarca todos los errores pero no te dice cual es el error
#finally si no sucede de todas formas se ejecuta 
finally:
    print("De todas formas me voy a imprimir changana")
    