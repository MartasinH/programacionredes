import requests
import json

url = 'https://dog.ceo/api/breeds/list/all'

payload={}
headers = {
  'Content-Type': 'application/json',
  'x-api-key': 'live_POivMpWHCFjPV2b6Shp8HHTnbQpzFLPgXRa5s6EpJaUtavQ2wCjnXbpNon3SRARY'
}
print(url)
json_data = requests.get(url).json()

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text)


#print(f'Raza de Perro:  {json_data['message']}')
while True:
    id = input('Ingrese la raza de perro que deses : ')
    if id == 'salir' or id == 's':
        break
    print('******************************************************************************')
    subraza = json_data['message'][id]
    if len(subraza) == 0:
        print('Esta raza no tiene subrazas')
    else:    
        print(f'La subraza de {id} es : {subraza}')
    





