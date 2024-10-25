import requests
import json
#Appi Videollamada Zoom
url = 'https://yourappsredirecturl/?code={theauthorizationcode}'

payload={}
headers = {
  'Content-Type': 'application/json',
  'x-api-key': 'live_POivMpWHCFjPV2b6Shp8HHTnbQpzFLPgXRa5s6EpJaUtavQ2wCjnXbpNon3SRARY'
}
print(url)
json_data = requests.get(url).json()

response = requests.request("GET", url, headers=headers, data=payload)