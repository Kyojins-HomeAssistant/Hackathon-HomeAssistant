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
        thread = threading.Thread(target=PlayYt.PlaySong, args=(songName, player, ))
        
        thread.start()

        nowPlaying.nowPlaying = songName
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

        nowPlaying.nowPlaying = ''
    elif parsedCommand[0] == 'nowplaying':
        if nowPlaying.nowPlaying == '':
            print('nothing playing now')
        else:
            print('now playing ' + nowPlaying.nowPlaying)

    mainWindow.button.setDisabled(False)