import serial
import time

# 아두이노 시리얼 포트 설정
arduino = serial.Serial('/dev/ttyACM0', 9600)  # 포트 이름은 다를 수 있음
time.sleep(2)  # 아두이노가 초기화될 때까지 대기

# RGB 값 설정
r = 67  # 빨간색
g = 0    # 초록색
b = 255    # 파란색

# 밝기 값 설정 (0~255)
brightness = 255  # 예를 들어, 50% 밝기

# RGB 값과 밝기 값을 아두이노에 전송
arduino.write(bytes([r, g, b, brightness]))

# 시리얼 포트 닫기
arduino.close()
