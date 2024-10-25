import requests

def get_seoul_weather(api_key):
    # API URL 설정 (서울의 날씨 데이터를 JSON 형식으로 요청)
    url = f"http://api.openweathermap.org/data/2.5/weather?q=Seoul&appid={api_key}&lang=kr&units=metric"

    # API 요청 및 응답 데이터 파싱
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        
        # 날씨 데이터 추출
        weather = data['weather'][0]['description']  # 날씨 설명
        temp = data['main']['temp']  # 현재 기온
        feels_like = data['main']['feels_like']  # 체감 온도
        humidity = data['main']['humidity']  # 습도
        
        # 출력
        print(f"서울의 현재 날씨: {weather}")
        print(f"현재 기온: {temp}°C")
        print(f"체감 온도: {feels_like}°C")
        print(f"습도: {humidity}%")
    else:
        print("날씨 정보를 가져오는 데 실패했습니다.")

# OpenWeatherMap에서 발급받은 API 키를 여기에 넣으세요
api_key = "a9a887ca68ffc162285de732d0c33398"
get_seoul_weather(api_key)
