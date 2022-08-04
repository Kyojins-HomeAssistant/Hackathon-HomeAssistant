import speech_recognition
import pyaudio

# ami bujhi...

recognizer = speech_recognition.Recognizer()
recognizer.energy_threshold = 1000

with speech_recognition.Microphone() as source:
    print('calibrating mic...')
    recognizer.adjust_for_ambient_noise(source)
    print('record shuru holo...')

    audio = recognizer.listen(source)

print('record shesh')

# source hoilo amar mic re python variable e nilam
# recognizer object er listen method voice recognize
# kore dibe
# pause threshold function 1 second silence pele record off korbe

try:
    print(recognizer.recognize_google(audio))

    # google er api use kore text dibe
    # ref https://github.com/Uberi/speech_recognition/blob/master/examples/microphone_recognition.py
except speech_recognition.UnknownValueError:
    print('kisu bujhi nai')
except speech_recognition.RequestError:
    print('request google er kase jay i nai lol')