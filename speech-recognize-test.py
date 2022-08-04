import speech_recognition

# ami bujhi...

recognizer = speech_recognition.Recognizer()

with speech_recognition.Microphone() as source:
    audio = recognizer.listen(source)

# source hoilo amar mic re python variable e nilam
# recognizer object er listen method voice recognize
# kore dibe

try:
    print(recognizer.recognize_google(audio))

    # google er api use kore text dibe
    # ref https://github.com/Uberi/speech_recognition/blob/master/examples/microphone_recognition.py
except speech_recognition.UnknownValueError:
    print('kisu bujhi nai')
except speech_recognition.RequestError:
    print('request google er kase jay i nai lol')