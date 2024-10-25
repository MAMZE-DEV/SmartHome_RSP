import pygame
import subprocess
import time
import schedule

# 첫 번째 스크립트 실행
subprocess.Popen(["python3", "/home/mamze/myDev/python/stt/neopixel_control_off.py"])

def job():
    # 두 번째 스크립트 실행
    subprocess.Popen(["python3", "/home/mamze/myDev/python/stt/neopixel_control.py"])

    # Pygame mixer 초기화 (이미 초기화되었는지 확인)
    if not pygame.mixer.get_init():
        pygame.mixer.init()

    try:
        mp3_file_path = 'wakeup.mp3'  # 파일 경로 확인 필요
        pygame.mixer.music.load(mp3_file_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(1)
    except Exception as e:
        print(f"오류 발생: {e}")

# 스케줄 작업 설정
schedule.every().day.at("13:47").do(job)

# 스케줄 실행 루프
try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("스케줄러가 중지되었습니다.")
