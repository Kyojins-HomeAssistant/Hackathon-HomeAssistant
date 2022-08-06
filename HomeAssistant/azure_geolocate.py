import os
import pycountry
import requests
from dotenv import load_dotenv

import socket

load_dotenv()

def return_ip_address():
    h_name = socket.gethostname()
    IP_address = socket.gethostbyname(h_name)
    return IP_address


# api-endpoint
URL = "https://atlas.microsoft.com/geolocation/ip/json?api-version=1.0"
# apiKey = "<azure_map_api_key>"
apiKey = os.getenv("GEOLOCATE_APIKEY")
# print(apiKey)

def get_countryName_byIP():
    countryName = ''
    # basically event wifi ip addressess were not getting a country 
    # response from azure geolocate, so hardcoded a bangladeshi ip 
    # PARAMS = {'ip': return_ip_address(), "subscription-key": apiKey}
    PARAMS = {'ip': "45.251.229.255", "subscription-key": apiKey}
    r = requests.get(url=URL, params=PARAMS)

    # extracting data in json format
    data = r.json()

    countryCode = ""

    # get country name from two letter code
    if ("countryRegion" in data):
        countryCode = data['countryRegion']['isoCode']
        countryName = pycountry.countries.get(alpha_2=countryCode).name


    return countryName
