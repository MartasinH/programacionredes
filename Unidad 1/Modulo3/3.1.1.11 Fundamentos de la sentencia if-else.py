'''Autor:Marta Lugo López
Fecha de entrega:26/sep/2024'''


#Entrada
ingreso = float(input("Introduce el ingreso anual: "))
#Condicion
if ingreso < 85528:
	tax = ingreso * 0.18 - 556.02
else:
	tax = (ingreso - 85528) * 0.32 + 14839.02

if tax < 0.0:
	tax = 0.0

tax = round(tax, 0)
#Salida
print("El impuesto es:", tax, "pesos")