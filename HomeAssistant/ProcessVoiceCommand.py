import threading
import os
from HomeAssistant.AzureLocationSearch import LocationSearch
from HomeAssistant.AzureRouteSearch import GetRouteCoordinates
from HomeAssistant.azure_speech_synth import text_to_speech

import azure_speech_recognition
import parser_simple
import SpotifySearch
import BingWebSearch
import azure_newsSearch
import AzureLocationSearch
import AzureRouteSearch
import azure_speech_synth


os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
os.environ["PATH"] = os.path.dirname(__file__) + os.pathsep + os.environ["PATH"]

import mpv
import PlayYt as PlayYt

player = mpv.MPV(ytdl=True, video=False)
nowPlaying = ''

def TakeVoiceCommand(nowPlaying):
    speechText = azure_speech_recognition.recognize_from_microphone()

    print('you said: ' + speechText)

    parsedCommand = parser_simple.extractCommandFromText(speechText)

    print(parsedCommand)

    if parsedCommand[0] == 'play':
        songName = parsedCommand[2]
        thread = threading.Thread(target=PlayYt.PlaySong, args=(songName, player, ))
        
        thread.start()

        nowPlaying = songName
    elif parsedCommand[0] == 'search':
        if parsedCommand[1] == 'track':
            print(SpotifySearch.ListTracksOnName(parsedCommand[2]))
        elif parsedCommand[1] == 'artist':
            print(SpotifySearch.ListTracksOnArtist(parsedCommand[2]))
        elif parsedCommand[1] == 'genre':
            print(SpotifySearch.ListTracksOnGenre(parsedCommand[2]))
        elif parsedCommand[1] == 'web':
            print(BingWebSearch.BingWebSearch(parsedCommand[2]))
        else:
            print('error')
    elif parsedCommand[0] == 'pause':
        player.stop()

        nowPlaying = ''
    elif parsedCommand[0] == 'nowplaying':
        if nowPlaying == '':
            print('nothing playing now')
        else:
            print('now playing ' + nowPlaying)
    
    elif parsedCommand[0] == 'news':
        holder = True
        # just call news and get them, recite them
        res = azure_newsSearch.get_local_news()

        for item in res:
            # azure_speech_synth.text_to_speech(item)
            print(item)
    elif parsedCommand[0] == 'go':
        holder = True
        src = parsedCommand[2][0]
        dest = parsedCommand[2][1]
        src_coord = LocationSearch(src)
        dest_coord = LocationSearch(dest)
        path_detail = GetRouteCoordinates([(src_coord, dest_coord)])
        print(path_detail)
        # eikhane returning ki ta sure na
        # !!!!!!!! MUST CHECK !!!!!!!
        # text_to_speech(path_detail)
        # just call location then route and get them, recite them
    elif parsedCommand[0] == 'FAILURE':
        gotError = True
        text_to_speech('I could not understand the command')
    return nowPlaying

while True:
    input('tip de...')

    nowPlaying = TakeVoiceCommand(nowPlaying)