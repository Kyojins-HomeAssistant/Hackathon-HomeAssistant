import spotipy
import requests
import urllib

clientID = 'cd58630a1991416abb9ec5b15e658b16'
clientSecret = 'f671004387df431997923cf75d18a6fc'
client_credentials_manager = spotipy.SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret)
token = client_credentials_manager.get_access_token()
params = {'q': '', 'type': 'track', 'limit': 5}
header = {'Authorization': 'Bearer ' + token['access_token']}

# response = requests.get(url='https://api.spotify.com/v1/search', params={'q': 'demons', 'type': 'track'}, headers=header)

def ListTracksOnName(query):
    clientID = 'cd58630a1991416abb9ec5b15e658b16'
    clientSecret = 'f671004387df431997923cf75d18a6fc'
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
    clientID = 'cd58630a1991416abb9ec5b15e658b16'
    clientSecret = 'f671004387df431997923cf75d18a6fc'
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
    clientID = 'cd58630a1991416abb9ec5b15e658b16'
    clientSecret = 'f671004387df431997923cf75d18a6fc'
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