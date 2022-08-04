# this main for testing right now

import speech_recognition
import SpeechRecognition

try:
    print(SpeechRecognition.SpeechRecognize())
except speech_recognition.UnknownValueError:
    print('kisu bujhi nai')
except speech_recognition.RequestError:
    print('google data pay na lol')