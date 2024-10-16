
#Declarar vaariables
hour = int (input ("Hora de inicio (horas) :") )
ming = int (input ("Minuto de inicio (minutos): ") )
dura = int (input ("Duración del evento (minutos): "))

#Operaciones
total = ming + dura
cociente = total // 60
residuo = total % 60
hour += cociente

#SALIDA
#print（str（hour）+'：'+str(residuo))
print (hour,':', residuo)
#print (f" (hour): (residuo) ")