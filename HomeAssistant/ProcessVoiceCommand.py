import HomeAssistant.PlayYt as PlayYt
import os
import time

os.environ["PATH"] = os.path.dirname(__file__) + os.pathsep + os.environ["PATH"]

import mpv
import threading
import HomeAssistant.azure_speech_recognition as azure_speech_recognition
import HomeAssistant.parser_simple as parser_simple
import HomeAssistant.SpotifySearch as SpotifySearch
import HomeAssistant.BingWebSearch as BingWebSearch
import HomeAssistant.PlayYt as PlayYt
import HomeAssistant.azure_speech_synth as azure_speech_synth
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
        mainWindow.label.setText('Playing ' + songName)
    elif parsedCommand[0] == 'search':
        if parsedCommand[1] == 'track':
            res = SpotifySearch.ListTracksOnName(parsedCommand[2])
            
            for track in res:
                azure_speech_synth.text_to_speech(track)
        elif parsedCommand[1] == 'artist':
            res = SpotifySearch.ListTracksOnArtist(parsedCommand[2])
            
            for track in res:
                azure_speech_synth.text_to_speech(track)
        elif parsedCommand[1] == 'genre':
            res = SpotifySearch.ListTracksOnGenre(parsedCommand[2])
            
            for track in res:
                azure_speech_synth.text_to_speech(track)
        elif parsedCommand[1] == 'web':
            res = BingWebSearch.BingWebSearch(parsedCommand[2])
            
            for track in res:
                azure_speech_synth.text_to_speech(track)
        else:
            text_to_speech("I could not understand the command")
    elif parsedCommand[0] == 'pause':
        player.stop()

        nowPlaying.nowPlaying = ''
    elif parsedCommand[0] == 'nowplaying':
        if nowPlaying.nowPlaying == '':
            azure_speech_synth.text_to_speech('nothing playing now')
        else:
            azure_speech_synth.text_to_speech('now playing ' + nowPlaying.nowPlaying)

    def ResetText(mainWindow):
        time.sleep(3)
        mainWindow.label.setText('')

    thread = threading.Thread(target=ResetText, args=(mainWindow, ))

    thread.start()
    mainWindow.button.setDisabled(False)