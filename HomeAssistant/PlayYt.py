import googleapiclient.discovery
# import mpv

def PlaySong(query, player):
    apiServiceName = 'youtube'
    apiVersion = 'v3'
    apiKey = 'AIzaSyDOYfCfX95k7s81Z8MfJtyFelD_yKid32w'
    youtube = googleapiclient.discovery.build(serviceName=apiServiceName, version=apiVersion, developerKey=apiKey)
    request = youtube.search().list(q=query, part='snippet')
    response = request.execute()

    player.play('https://www.youtube.com/watch?v=' + response['items'][0]['id']['videoId'])
    print('started playing ' + query + ' song id: ' + response['items'][0]['id']['videoId'])
    player.wait_for_playback()
    # player.wait_for_play()
    print('completed song')

# PlaySong("Demons by imagine dragon", mpv.MPV(ytdl=True, video=False))