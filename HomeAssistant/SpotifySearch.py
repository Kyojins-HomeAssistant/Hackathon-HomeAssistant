import spotipy
import requests
import urllib
import os
from dotenv import load_dotenv

load_dotenv()


clientID=os.getenv("SPOTIFY_CLIENTID")
# clientID = '<your_clientID_from_spotify'
clientSecret=os.getenv("SPOTIFY_CLIENTSECRET")
# clientSecret = '<your_client_secret_from_spotify>'
client_credentials_manager = spotipy.SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret)
token = client_credentials_manager.get_access_token()
params = {'q': '', 'type': 'track', 'limit': 5}
header = {'Authorization': 'Bearer ' + token['access_token']}

# response = requests.get(url='https://api.spotify.com/v1/search', params={'q': 'demons', 'type': 'track'}, headers=header)

def ListTracksOnName(query):
    client_credentials_manager = spotipy.SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret)
    token = client_credentials_manager.get_access_token()
    params = {'q': urllib.parse.quote(query), 'type': 'track', 'limit': 5}
    header = {'Authorization': 'Bearer ' + token['access_token']}
    response = requests.get(url='https://api.spotify.com/v1/search', params=params, headers=header)

    if response.status_code != 200:
        raise ConnectionError()

    trackNames = []

    for item in response.json()['tracks']['items']:
        trackNames.append(item['name'])

    return trackNames

def ListTracksOnArtist(query):
    client_credentials_manager = spotipy.SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret)
    token = client_credentials_manager.get_access_token()
    params = {'q': 'artist:' + urllib.parse.quote(query), 'type': 'track', 'limit': 5}
    header = {'Authorization': 'Bearer ' + token['access_token']}
    params['q'] = urllib.parse.quote(query)
    response = requests.get(url='https://api.spotify.com/v1/search', params=params, headers=header)

    if response.status_code != 200:
        raise ConnectionError()

    trackNames = []

    for item in response.json()['tracks']['items']:
        trackNames.append(item['name'])

    return trackNames

def ListTracksOnGenre(query):
    client_credentials_manager = spotipy.SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret)
    token = client_credentials_manager.get_access_token()
    params = {'q': 'genre:' + urllib.parse.quote(query), 'type': 'track', 'limit': 5}
    header = {'Authorization': 'Bearer ' + token['access_token']}
    params['q'] = urllib.parse.quote(query)
    response = requests.get(url='https://api.spotify.com/v1/search', params=params, headers=header)

    if response.status_code != 200:
        raise ConnectionError()

    trackNames = []

    for item in response.json()['tracks']['items']:
        trackNames.append(item['name'])

    return trackNames