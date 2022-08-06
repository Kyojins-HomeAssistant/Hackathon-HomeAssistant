import requests
import urllib
import os
from dotenv import load_dotenv

load_dotenv()

def BingWebSearch(query):
    subscription_key=os.getenv("BING_WEBSEARCH_KEY")
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    params = {'q': urllib.parse.quote(query), 'count': 5, 'answerCount': 1, 'responseFilter': 'webpages'}
    response = requests.get('https://api.bing.microsoft.com/v7.0/search', headers=headers, params=params)
    resultJson = response.json()

    searchResults = []

    for value in resultJson['webPages']['value']:
        searchResults.append(value['name'])

    return searchResults

# print(BingWebSearch('doggy'))