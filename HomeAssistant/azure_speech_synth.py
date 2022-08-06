import re
import numpy
import azure.cognitiveservices.speech as speechsdk
#print("ekhane")

speech_config = speechsdk.SpeechConfig(subscription="<Azure_cognitive_services_subscription_key>", region="eastus")
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

# The language of the voice that speaks.
speech_config.speech_synthesis_voice_name='en-US-JennyNeural'

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

# return normalized sentence to read
def _normalize(sentence):
    sentence = sentence.lower()
    sentence = sentence.strip()
    sentence = re.sub(r'[^\w\s.,-?!:$&@%*()"{}[]]', '', sentence)

    # stop_words = set(stopwords.words('english'))
    lst = [sentence][0].split()
    sentence = ""
    for i in lst:
        # if not i in stop_words:
        sentence += i+' '

    sentence = sentence[:-1]
    # lst = [sentence][0].split()
    return sentence


def text_to_speech(text):
    text = _normalize(text)
    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()
    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(text))
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")

# text_to_speech("So for $12  i'm not That bAd -for you, right?")