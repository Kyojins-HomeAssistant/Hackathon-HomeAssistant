import requests
import urllib

def LocationSearch(query):
    # headers = {"Ocp-Apim-Subscription-Key": 'ca79c680fc4d48e08afef590fa2d31ea'}
    params = {'query': urllib.parse.quote(query), 'api-version': 1, 'subscription-key': 'OSiV2wi91HWTlH0xX-eNqqicz-tudl8Iuwi5FCoPfo4'}
    response = requests.get('https://atlas.microsoft.com/search/address/json', params=params)
    resultJson = response.json()
    searchResult = (resultJson['results'][0]['position']['lat'], resultJson['results'][0]['position']['lon'])

    return searchResult

# print(LocationSearch('dhaka'))