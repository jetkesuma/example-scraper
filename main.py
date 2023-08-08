import os
import json
import requests
from bs4 import BeautifulSoup
import pandas as pd

loc = 'California'
url = 'https://www.realtor.com/realestateandhomes-search/{}/pg-2'.format(loc)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 '
                  'Safari/537.36'}

res = requests.get(url, headers=headers)


def get_total_pages():
    soup = BeautifulSoup(res.text, 'html.parser')
    items = soup.findAll('div', 'BasePropertyCard_propertyCardWrap__J0xUj')
    for item in items:
        broker = item.find('span', 'BrokerTitle_titleText__20u1P').text
        status = item.find('div', 'Text__StyledText-rui__sc-1j9ntoo-0 hkRBUb TypeInfo__StyledInfo-rui__m9gzjc-0 '
                                  'eVFIjb message').text
        price = item.find('div', 'Price__Component-rui__x3geed-0 ibnFqH card-price').text
        try :
            wide = item.find('span', {'data-testid': 'screen-reader-value'}).text
        except :
            wide = 'No Value'
        loc = item.find('div', 'card-address truncate-line').text
        try:
            img = item.find('div', 'Picture_photo-wrap__xFx0Q').find('img')['src']
        except:
            img = 'No Image'
        print(img)



if __name__ == '__main__':
    get_total_pages()
