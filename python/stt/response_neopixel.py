import subprocess
import speech_recognition as sr
import playsound
from gtts import gTTS
import os
import playsound

def speak(text):
    tts = gTTS(text=text, lang='ko')
    filename='voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def listen_and_recognize(target_text):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("듣고 있습니다...")
        recognizer.adjust_for_ambient_noise(source)

        while True:
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio, language='ko-KR')
                print("인식된 텍스트:", text)

                # 디버깅 메시지
                print(f"비교할 텍스트: '{target_text}' vs 인식된 텍스트: '{text}'")

                if text.strip() == target_text:  # 공백 제거
                    print(f"목표 텍스트 '{target_text}'이(가) 인식되었습니다.")
                    speak("불을켜겠습니다.")
                    subprocess.run(["python3", "neopixel_control.py"])
                    subprocess.run(["python3", "response_neopixel_off.py"])
                break  # 목표 텍스트가 인식되면 루프 종료

            except sr.UnknownValueError:
                print("음성을 인식할 수 없습니다.")
            except sr.RequestError:
                print("서비스에 접근할 수 없습니다.")
target_text = '불 켜 줘'
listen_and_recognize(target_text)

