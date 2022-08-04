import threading
import HomeAssistant.azure_speech_recognition as azure_speech_recognition
import HomeAssistant.parser_simple as parser_simple
import HomeAssistant.SpotifySearch as SpotifySearch
import os

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
os.environ["PATH"] = os.path.dirname(__file__) + os.pathsep + os.environ["PATH"]

import mpv
import HomeAssistant.PlayYt as PlayYt

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

    return nowPlaying