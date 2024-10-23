import requests
import time
while True:
    id = input('Ingresa el Id:')
    if id =='salir' or id =='s':
        break
    url = f'https://fakestoreapi.com/products/{id}'
#https://fakestoreapi.com/products sirve para invocar a los productos 

#print(productos.status_code) #tiene que salir un 200 con eso se verifica que esta bien el Api
#for prod in productos.json():
    #print(prod['title'], '\t  ',prod['price'])  #para que salga solo el titulo y precio
    productos = requests.get(url).json()    
    print(productos)
    time.sleep(2)
    
    

    






   