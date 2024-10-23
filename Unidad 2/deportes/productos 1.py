import requests
url = 'https://fakestoreapi.com/products'

productos = requests.get(url)
#print(productos.status_code) #tiene que salir un 200 con eso se verifica que esta bien el Api
for prod in productos.json():
    print(prod['title'], '\t  ',prod['price'])  #para que salga solo el titulo y precio