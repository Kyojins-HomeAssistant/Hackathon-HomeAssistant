import requests
import urllib

def BingWebSearch(query):
    headers = {"Ocp-Apim-Subscription-Key": 'ca79c680fc4d48e08afef590fa2d31ea'}
    params = {'q': urllib.parse.quote(query), 'count': 5, "textDecorations": True}
    response = requests.get('https://api.bing.microsoft.com/v7.0/search', headers=headers, params=params)
    resultJson = response.json()
    searchResults = []

    for value in resultJson['webPages']['value']:
        searchResults.append(value['name'])

    return searchResults

# print(BingWebSearch('doge'))