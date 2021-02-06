import os
from gtts import gTTS
from playsound import playsound
from datetime import datetime

def play(file):
    playsound(file, True)

def speak(text, lang = "en", slow = False, save = False, file = ""):
    dt = datetime.now().strftime("%d%m%Y%H%M%S")

    if save == True and file != "":
        file = file
    elif save == True and file == "":
        file = f"speech{dt}.mp3"
    elif save == False:
        file = f"speech{dt}.mp3"
    else:
        raise ValueError(f"'{file}' is not defined")
    
    if slow == True:
        slow = True
    elif slow ==  False:
        slow = False
    else:
        raise ValueError(f"'{slow}' is not defined")
    
    tts = gTTS(text=text, lang=lang, slow=slow)

    if os.path.splitext(file)[1] == ".mp3":
        tts.save(file)
        
        play(file)

        if save == False:
            os.unlink(file)
        elif save == True:
            pass
        else:
            raise ValueError(f"'{save}' is not defined")
    else:
        raise ValueError(f"'{file}' is not a valid mp3 format")