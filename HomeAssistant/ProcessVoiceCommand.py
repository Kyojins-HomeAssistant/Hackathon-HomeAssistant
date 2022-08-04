import PlayYt as PlayYt
import mpv
import threading
import HomeAssistant.azure_speech_recognition as azure_speech_recognition
import HomeAssistant.parser_simple as parser_simple
import HomeAssistant.SpotifySearch as SpotifySearch
import HomeAssistant.BingWebSearch as BingWebSearch
import HomeAssistant.PlayYt as PlayYt
from PySide6 import QtGui, QtCore, QtWidgets

def TakeVoiceCommand(nowPlaying, mainWindow, player):
    speechText = azure_speech_recognition.recognize_from_microphone(mainWindow)

    print('you said: ' + speechText)

    parsedCommand = parser_simple.extractCommandFromText(speechText)

    print(parsedCommand)

    if parsedCommand[0] == 'play':
        songName = parsedCommand[2]
        thread = threading.Thread(
            target=PlayYt.PlaySong, args=(songName, player, ))

        thread.start()

        nowPlaying.nowPlaying = songName
    elif parsedCommand[0] == 'search':
        if parsedCommand[1] == 'track':
            res = SpotifySearch.ListTracksOnName(parsedCommand[2])
            print(res)
        elif parsedCommand[1] == 'artist':
            res = SpotifySearch.ListTracksOnArtist(parsedCommand[2])
            print(res)
        elif parsedCommand[1] == 'genre':
            res = SpotifySearch.ListTracksOnGenre(parsedCommand[2])
            print(res)
        elif parsedCommand[1] == 'web':
            res = BingWebSearch.BingWebSearch(parsedCommand[2])
            print(res)
            text_to_speech("Search results for " + parsedCommand[2] + ":")
            for item in res:
                # text_to_speech(item)
                print(item)
            
        else:
            text_to_speech("I could not understand the command")
            print('error')
    elif parsedCommand[0] == 'pause':
        player.stop()

        nowPlaying.nowPlaying = ''
    elif parsedCommand[0] == 'nowplaying':
        if nowPlaying.nowPlaying == '':
            print('nothing playing now')
        else:
            print('now playing ' + nowPlaying.nowPlaying)

    mainWindow.button.setDisabled(False)
