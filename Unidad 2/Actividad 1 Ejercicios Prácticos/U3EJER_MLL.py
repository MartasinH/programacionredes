import requests
import json


#Api de fotos de la Nasa
url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY"

payload = {}
headers = {
    'Content-Type': 'application/json',
    'x-api-key': 'Y0ZH5MkDIf019Q701rv9vGd2KNOBn9nPfRk7Fx1B'
}
opciones = {
    12: "http://mars.jpl.nasa.gov/msl-raw-images/msss/01000/mcam/1000MR0044631260503686E03_DXXX.jpg",
    7: "http://mars.jpl.nasa.gov…631290305226E03_DXXX.jpg",
    28:"http://mars.jpl.nasa.gov…631180503678E01_DXXX.jpg"
}
print("----------------------------------------------------------------------------------------------")

# Pedir al usuario que seleccione una opción
opcion = int(input("Sorteo de imágenes \n - Escoge un número \n - 12 \n - 7 \n - 28 \n 'Introduce :' "))

if opcion in opciones:
    print(f"La imagen seleccionada es: {opciones[opcion]}")
else:
     print("Byee")

   