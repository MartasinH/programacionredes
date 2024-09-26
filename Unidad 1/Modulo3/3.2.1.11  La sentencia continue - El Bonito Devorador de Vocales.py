'''Autor:Marta Lugo López
Fecha de entrega:26/sep/2024'''

word_without_vowels = ""
# Indicar al usuario que ingrese una palabra
user_word = input("Ingresa tu palabra: ")
# y asignarlo a la variable user_word.
user_word = user_word.upper()
# Completa el cuerpo del bucle for.
for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels += letter
		
print(word_without_vowels)


