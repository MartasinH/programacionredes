import requests

latitud = 25.68
longitud = -100.31
clave = "60ccd32f3f85bc2e9eab9e9d9c0a96c1"
main_api=  f"https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={clave}"

print(main_api)

json_data = requests.get(main_api).json()
print(json_data)
#llamar a uno de ldiccionario
print(json_data['name'])

