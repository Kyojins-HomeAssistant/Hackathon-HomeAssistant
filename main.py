# this main for testing right now

import speech_recognition
import HomeAssistant.SpeechRecognition as SpeechRecognition

try:
    print(SpeechRecognition.SpeechRecognize())
except speech_recognition.UnknownValueError as exception:
    print(exception)
except speech_recognition.RequestError as exception:
    print(exception)