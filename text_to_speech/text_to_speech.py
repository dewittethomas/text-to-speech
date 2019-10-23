from gtts import gTTS
from playsound import playsound
import os

filename = 'temp.mp3'

def speak(text, language):
    tts = gTTS(text, lang=language)
    tts.save(filename)
    playsound(filename)
    os.remove(filename)
        


   
