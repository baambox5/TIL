import requests
from bs4 import BeautifulSoup

url = requests.get('https://finance.naver.com/marketindex/').text
soup = BeautifulSoup(url, 'html.parser')
exchange = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text

print(exchange)
