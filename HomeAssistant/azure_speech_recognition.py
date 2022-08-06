import os
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk
from PySide6 import QtGui, QtCore, QtWidgets


def recognize_from_microphone(mainWindow):
    # print("ekhane")
    res = ""
    load_dotenv()
    subscription_key=os.getenv("AZURE_COGNITIVESPEECH_SERVICE_KEY")
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region="eastus")
    speech_config.speech_recognition_language="en-US"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        res = speech_recognition_result.text

        mainWindow.label.setText('You said: ' + res)
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        mainWindow.label.setText("No speech could be recognized. Please try again.")
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        mainWindow.label.setText("Speech Recognition canceled. Please try again.")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            mainWindow.label.setText("Error details: {}".format(cancellation_details.error_details))
            # mainWindow.label.setText("Did you set the speech resource key and region values?")
    
    return res

