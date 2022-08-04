import json
import pycountry
import requests

import socket

def return_ip_address():
    h_name = socket.gethostname()
    IP_address = socket.gethostbyname(h_name)
    return IP_address


# def get_country_by_ip(ip_address):
# importing the requests library

# api-endpoint
URL = "https://atlas.microsoft.com/geolocation/ip/json?api-version=1.0"
apiKey = "iDEex7cx7DWGwZXOWza8A0AxdNznLALRYVce3_N7PBw"


def get_countryName_byIP():
    countryName = ''
    PARAMS = {'ip': "45.251.229.255", "subscription-key": apiKey}
    r = requests.get(url=URL, params=PARAMS)

    # extracting data in json format
    data = r.json()

    countryCode = ""
    if ("countryRegion" in data):
        countryCode = data['countryRegion']['isoCode']
        countryName = pycountry.countries.get(alpha_2=countryCode).name


    return countryName
