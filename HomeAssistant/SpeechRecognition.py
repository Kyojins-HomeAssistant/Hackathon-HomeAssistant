import speech_recognition

def SpeechRecognize():
    recognizer = speech_recognition.Recognizer()
    recognizer.energy_threshold = 10000

    with speech_recognition.Microphone() as source:
        print('calibrating')
        recognizer.adjust_for_ambient_noise(source)
        print('start recording')

        audio = recognizer.listen(source)

    print('done recording')

    # text = recognizer.recognize_google(audio)
    text = recognizer.recognize_google(audio)

    return text