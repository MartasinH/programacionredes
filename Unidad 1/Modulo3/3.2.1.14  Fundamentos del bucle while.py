'''Autor:Marta Lugo López
Fecha de entrega:26/sep/2024'''

blocks = int(input("Ingresa el número de bloques: "))

height = 0
bloques_usados = 0

while bloques_usados <= blocks:
  height += 1
  bloques_usados += height
  if bloques_usados > blocks:
    height -= 1
    break

print("La altura de la pirámide:", height)