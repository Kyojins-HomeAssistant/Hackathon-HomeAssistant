import requests
import json
import re

import azure_geolocate

# lowercasing, whitespace removal, almost all punctuation removal
def _normalize(sentence):
    sentence = sentence.lower()
    sentence = sentence.strip()
    sentence = re.sub(r'[^\w\s.,-]', '', sentence)

    # stop_words = set(stopwords.words('english'))
    lst = [sentence][0].split()
    sentence = ""
    for i in lst:
        # if not i in stop_words:
        sentence += i+' '

    sentence = sentence[:-1]
    # lst = [sentence][0].split()
    return sentence


subscription_key = "2d2359bc090c46dba54720924fdff75f"
search_url = "https://api.bing.microsoft.com/v7.0/news/search"


def get_local_news():
    search_term = azure_geolocate.get_countryName_byIP()

    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    params = {"q": search_term,
              "textDecorations": False,
              "textFormat": "HTML",
              "setLang": "en",
              "mkt": "en-WW",
              "freshness": "Week",
              "count": "5"}

    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    # extract some fields from json and normalizing them
    descriptions = [_normalize(article["description"])
                    for article in search_results["value"]]
    names = [_normalize(article["name"])
             for article in search_results["value"]]

    providers = [article["provider"] for article in search_results["value"]]
    prov = [_normalize(provider[0]["name"]) for provider in providers]
    res = []

    # return list building
    item_dict = json.loads(json.dumps(search_results))  
    newsCount = len(item_dict["value"])

    for i in range(0, newsCount):
        res.append(" " + names[i] + ".    " +
                   descriptions[i] + ".   " + "News From " + prov[i])
    return res

