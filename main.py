import os
import json
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.realtor.com/realestateandhomes-search/Los-Angeles_CA/show-recently-sold/sby-6'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 '
                  'Safari/537.36'}

res = requests.get(url, headers=headers)


def get_total_pages():
    soup = BeautifulSoup(res.text, 'html.parser')
    recently_sold_page = soup.find(attrs={'class': 'PropertiesList_propertiesContainer__j6ct_ '
                                                   'PropertiesList_listViewGrid__oGuSL'})
    items = recently_sold_page.findAll(attrs={'class': 'BasePropertyCard_propertyCardWrap__J0xUj'})

    contents = []
    for item in items:
        try:
            broker = item.find('span', 'BrokerTitle_titleText__20u1P').text
        except:
            broker = 'Broker is not available'
        price = item.find('div', 'Price__Component-rui__x3geed-0 ibnFqH card-price').text
        adrress = item.find('div', 'card-address truncate-line').text

        data_dict = {
            'broker': broker,
            'price': price,
            'adress': adrress
        }
        contents.append(data_dict)

    # writing json file
    try:
        os.mkdir('json_result')
    except FileExistsError:
        pass

    with open('json_result/recenty_sold.json', 'w+') as json_data:
        json.dump(contents, json_data)
    print('json data created')

    # create csv
    df = pd.DataFrame(contents)
    df.to_csv('realtor_recent_sold.csv', index=False)
    df.to_excel('realtor_recent_data.xlsx', index=False)

    # data Created
    print('Data Created Success')

if __name__ == '__main__':
    get_total_pages()
