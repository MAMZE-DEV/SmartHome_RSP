from gtts import gTTS
import os
import playsound

def speak(text):
    tts = gTTS(text=text, lang='ko')
    filename='voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

speak("만나서 반가워요")
