import requests
import os
from dotenv import load_dotenv

load_dotenv()

def GetRouteCoordinates(queries):
    queryString = ''

    for i in range(0, len(queries)):
        if i != 0:
            queryString += ':'
        
        queryString += str(queries[i][0]) + ',' + str(queries[i][1])
    
    subscriptio_key=os.getenv("LOCATION_ROUTE_SEARCH_KEY")
    params = { 'query': queryString, 'api-version': '1.0', 'subscription-key':subscriptio_key}
    response = requests.get('https://atlas.microsoft.com/route/directions/json', params=params)
    
    resultJson = response.json()
    # data = {
    #     'lengthMeters': resultJson['routes'][0]['summary']['lengthInMeters'],
    #     'travelTimeInSeconds': resultJson['routes'][0]['summary']['travelTimeInSeconds'],
    #     'points': []
    # };   

    return resultJson


# import json
# route = GetRouteCoordinates([(23.781265414861046,90.35777289865626),(23.76524531999058,90.36620759038298)])
        
# stRoute = json.loads(json.dumps(route))
# if ("error" in stRoute):
#     print("Could not find any suitable route")
#             # mainWindow.label.setText("Could not find any suitable route")
# else:
#         # mainWindow.label.setText("Found a suitable route, printing here" + route["routes"][0]["summary"])
#     print(route["routes"][0]["summary"])