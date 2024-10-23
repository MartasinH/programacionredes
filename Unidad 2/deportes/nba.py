import http.client

conn = http.client.HTTPSConnection("netflix54.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "81bc4975f7msh00cf8093a534c35p18806ejsne625c1cb1a8f",
    'x-rapidapi-host': "netflix54.p.rapidapi.com"
}

conn.request("GET", "/season/episodes/?ids=80077209%2C80117715&offset=0&limit=25&lang=en", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))