import requests
from bs4 import BeautifulSoup
import datetime


#converted_gold_price=price[0:5]
def gold_price():
    url = 'https://www.monex.com/gold-prices/111'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='productTitle')
    gold_price = soup.find('span', id="span-813-5").get_text()
    currentDate = datetime.date.today()
    currentMonthName = currentDate.strftime("%B")
    return (f"{currentMonthName} {currentDate.day}, {currentDate.year} : ") + gold_price
