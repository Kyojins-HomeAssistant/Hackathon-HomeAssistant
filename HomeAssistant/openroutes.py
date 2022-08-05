import requests
# 

headers = {
    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
}
call = requests.get('https://api.openrouteservice.org/v2/directions/driving-car?api_key=5b3ce3597851110001cf6248b70f8b23b5d44477a4cddd1fad6ab0d9&start=8.681495,49.41461&end=8.687872,49.420318', headers=headers)

print(call.status_code, call.reason)
# print(call.text)

ls = call.json()

res = ls["features"]

with open("open.json", "w") as f:
    f.write(call.text)