import speech_recognition as sr
from gtts import gTTS
import os
import subprocess
import sys
sys.stderr = open(os.devnull, "w")
# 음성 인식 객체 생성
recognizer = sr.Recognizer()

# 마이크 설정 (장치 인덱스를 card 2로 설정)
mic = sr.Microphone(device_index=2)

# TTS로 음성을 출력하는 함수
def speak(text):
    tts = gTTS(text=text, lang='ko')  # 한국어 설정
    tts.save("output.mp3")  # 음성 파일로 저장
    os.system("mpg321 output.mp3")  # 음성 파일 재생
while True:
    with mic as source:
        print("음성을 입력하세요...")
        audio = recognizer.listen(source)  # 음성 녹음

        try:
            # 음성 인식
            text = recognizer.recognize_google(audio, language="ko-KR")
            print(f"인식된 텍스트: {text}")

            # 특정 텍스트가 인식되었을 때 파일 실행
            if "꺼" in text:  # "실행"이라는 단어가 포함된 경우
                speak("불을끄겠습니다.")
                print("파일을 실행합니다.")
                # 특정 파이썬 파일 실행
                subprocess.Popen(["python3", "neopixel_control_off.py"])  # 파일 경로 수정
            if "켜" in text:  # "실행"이라는 단어가 포함된 경우
                speak("불을 켜겠습니다.")
                print("파일을 실행합니다.")
                # 특정 파이썬 파일 실행
                subprocess.Popen(["python3", "neopixel_control.py"])  # 파일 경로 수정
            if "델타" in text:  # "실행"이라는 단어가 포함된 경우
                speak("네?")
                print("파일을 실행합니다.")
                # 특정 파이썬 파일 실행
            if "게임" in text:  # "실행"이라는 단어가 포함된 경우
                speak("즐거운 게임 되세요.")
                print("파일을 실행합니다.")
                # 특정 파이썬 파일 실행
                subprocess.Popen(["python3", "gamemode.py"])  # 파일 경로 수정
            if "휴식" in text:  # "실행"이라는 단어가 포함된 경우
                speak("편안한 시간 되세요.")
                print("파일을 실행합니다.")
                # 특정 파이썬 파일 실행
                subprocess.Popen(["python3", "neopixel_control.py"])  # 파일 경로 수정
                
                # 특정 텍스트가 인식되었을 때 프로그램 종료
            if "종료" in text:  # "종료"라는 단어가 포함된 경우
                print("프로그램을 종료합니다.")
                break  # 프로그램 종료

        except sr.UnknownValueError:
	        pass
        except sr.RequestError as e:
            print(f"Google API 요청 실패: {e}")
