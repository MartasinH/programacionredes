'''Autor:Marta Lugo López
Fecha de entrega:24/oct/2024'''

hora = int(input("Hora de inicio (horas): "))
minutos = int(input("Minuto de inicio (minutos): "))
duracion = int(input("Duración del evento (minutos): "))
minutos = minutos + duracion # encuentra el número total de minutos
hora = hora + minutos // 60 # encuentra el número de horas ocultas en los minutos y actualiza las horas
minutos = minutos % 60 # corrige los minutos para que estén en un rango de (0..59)
hora = hora % 24 # corrige las horas para que estén en un rango de (0..23) 
print(hora, ":", minutos )
