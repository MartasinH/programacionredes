'''Autor:Marta Lugo López
Fecha de entrega:24/oct/2024'''

año = int(input("Introduce un año: "))

if año < 1582:
	print("No esta dentro del período del calendario Gregoriano")
else:
	if año % 4 != 0:
		print("Año Común")
	elif año % 100 != 0:
		print("Año Bisiesto")
	elif año % 400 != 0:
		print("Año Común")
	else:
		print("Año Bisiesto")
