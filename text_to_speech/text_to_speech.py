from gtts import gTTS
from playsound import playsound
from mutagen.mp3 import MP3
import os
import time

file = "speech.mp3"

def play(file):
    playsound(file, True)

def get_length(file):
    audio = MP3(file)
    return audio.info.length

def speak(text, lang):
    tts = gTTS(text=text, lang=lang)
    tts.save(file)

    play(file)
    
    length = get_length(file)
    time.sleep(length)

    os.remove(file)