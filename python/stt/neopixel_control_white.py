import serial
import time

# 아두이노의 시리얼 포트와 보드레이트 설정
ser = serial.Serial('/dev/ttyACM0', 9600)  # USB 포트에 맞게 수정
time.sleep(2)  # 아두이노 초기화 대기

# RGB 값 설정
r = 0
g = 0
b = 20
brightness = 10  # 밝기를 255로 설정

# RGB 값 전송
ser.write(bytes([r, g, b, brightness]))


# RGB 값 전송
ser.write(bytes([r, g, b, brightness]))
ser.close()
