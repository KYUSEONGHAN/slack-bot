from bs4 import BeautifulSoup
import requests as re

def get_weather_info(area: str):
    # 네이버 날씨 페이지
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=' + area + '+날씨'

    html = re.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')

    temperature = soup.select_one("div.temperature_text").text.strip()
    status = soup.select_one("div.temperature_info > p").text.strip()
    weather_etc = soup.select_one("div.temperature_info > dl").text.strip()
    weather_etc2 = [etc_info.text.strip() for etc_info in soup.select_one("div.report_card_wrap > ul")][1:-1:2]

    message = temperature + '\n' + status + '\n' + weather_etc + '\n'

    for info in weather_etc2:
        message += info + '\n'

    return message