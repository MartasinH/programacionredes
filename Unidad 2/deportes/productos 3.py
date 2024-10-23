import requests
import time 

while True:
    id = input('Ingrese la id del producto: ')
    if id == 'salir' or id == 's':
        break
    
    url = f"https://fakestoreapi.com/products/{id}"
    response = requests.delete(url)
    print(f"Producto con ID *{id}* eliminado correctamente.")
    time.sleep(2)
    
    

    #print(productos.json())
