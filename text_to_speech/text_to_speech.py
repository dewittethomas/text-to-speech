import os
from gtts import gTTS
from playsound import playsound

def play(file):
    playsound(file, True)

def speak(text, lang = "en", slow = False):
    file = "speech.mp3"
    
    if slow == True:
        slow = True
    elif slow ==  False:
        slow = False
    else:
        raise ValueError(f"'{slow}' is not defined")
    
    tts = gTTS(text=text, lang=lang, slow=slow)
    tts.save(file)

    play(file)
    os.unlink(file)