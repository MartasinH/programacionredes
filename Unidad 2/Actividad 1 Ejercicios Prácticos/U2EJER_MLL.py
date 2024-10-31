#La API de ANIMES
import requests
import json


url = 'https://api.jikan.moe/v4/top/anime'
#print (url)
data = requests.get(url)
if data.status_code == 200:
    data = data.json()
    for e in data ['data']:
        print("El titulo del anime es :")
        print(e['title'])
        print("Su año fue en :")
        print(e['year'])
        print("La duracion de este es : ")
        print(e['duration'])




