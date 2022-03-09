from bs4 import BeautifulSoup
from datetime import datetime
import requests as re

today = datetime.today().strftime("%Y-%m-%d")

# 네이버 코로나 확진자 페이지
url = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%BD%94%EB%A1%9C%EB%82%9819'

html = re.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

corona_info = soup.select_one("div.status_info").text.strip()
area_corona = "".join([x.text.strip() for x in soup.select("table.table > tbody")])

print(corona_info)
print(area_corona)