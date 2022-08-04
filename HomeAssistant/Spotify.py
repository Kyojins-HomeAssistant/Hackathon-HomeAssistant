import spotipy

client_id = 'c3b39820384e4020803b795cd75825aa'
client_secret = '756b659590dd4af38f5b2e13d101ca08'
spotify = None

def SpotifySetup():
    return spotipy.Spotify(auth_manager=spotipy.SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

def ListTracks(query):
    results = spotify.search(q=query, limit=5)

    print(results)

spotify = SpotifySetup()
ListTracks('demons')