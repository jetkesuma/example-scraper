import os
import json
import requests
from bs4 import BeautifulSoup
import pandas as pd

loc = 'California'
page = 'pg-2'
url = 'https://www.realtor.com/realestateandhomes-search/{}/{}'.format(loc, page)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 '
                  'Safari/537.36'}

res = requests.get(url, headers=headers)


def get_total_pages():
    soup = BeautifulSoup(res.text, 'html.parser')
    items = soup.findAll('div', 'BasePropertyCard_propertyCardWrap__J0xUj')
    for item in items:
        broker = item.find('span', 'BrokerTitle_titleText__20u1P').text


if __name__ == '__main__':
    get_total_pages()
