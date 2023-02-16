from gtts import gTTS
import os.path

def save(text, lang = "en", slow = False, lang_check = False, file = ""):
    extension = extension = os.path.splitext(file)[1].lower()
    ready = False

    if file != "" and extension == ".mp3":
        file = file
        ready = True
    elif file == "":
        file = "speech.mp3"
        ready = True
    elif extension != ".mp3":
        raise ValueError(f"{file} is in a '{extension}' format, it should be in a '.mp3' format.")
    
    if ready:
        tts = gTTS(text=text, lang=lang, slow=slow, lang_check=lang_check)
        tts.save(file)