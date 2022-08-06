import requests
import urllib
import os
from dotenv import load_dotenv

load_dotenv()

def LocationSearch(query):
    subscription_key=os.getenv("LOCATION_ROUTE_SEARCH_KEY")
    # headers = {"Ocp-Apim-Subscription-Key": 'ca79c680fc4d48e08afef590fa2d31ea'}
    params = {'query': urllib.parse.quote(query), 'api-version': 1, 'subscription-key': subscription_key}
    response = requests.get('https://atlas.microsoft.com/search/address/json', params=params)
    resultJson = response.json()
    searchResult = (resultJson['results'][0]['position']['lat'], resultJson['results'][0]['position']['lon'])

    return searchResult

# print(LocationSearch('dhaka'))