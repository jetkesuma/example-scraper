import pandas as pd
import requests
from bs4 import BeautifulSoup



loca = input('please enter the location, if using spaces use the "-" sign:')
url = 'https://www.realtor.com/realestateandhomes-search/{}/pg-'.format(loca)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 '
                  'Safari/537.36'}

datas = []

def get_total_pages():
    count_page = 0
    for page in range(1, 5):
        count_page += 1
        print('Scraping page :', count_page)
        res = requests.get(url + str(page), headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        items = soup.findAll('div', 'BasePropertyCard_propertyCardWrap__J0xUj')
        for item in items:
            broker = item.find('span', 'BrokerTitle_titleText__20u1P').text
            status = item.find('div', 'Text__StyledText-rui__sc-1j9ntoo-0 hkRBUb TypeInfo__StyledInfo-rui__m9gzjc-0 '
                                      'eVFIjb message').text
            price = item.find('div', 'Price__Component-rui__x3geed-0 ibnFqH card-price').text
            try:
                wide = item.find('span', {'data-testid': 'screen-reader-value'}).text
            except:
                wide = 'No Value'
            loc = item.find('div', 'card-address truncate-line').text
            img = item.find('div', 'Picture_photo-wrap__xFx0Q').find('img')['src']

            # sorting data
            data_dict = {
                'broker': broker,
                'status': status,
                'price': price,
                'wide': wide,
                'location': loc,
                'image': img
            }
            datas.append(data_dict)

    # create csv
    df = pd.DataFrame(datas)
    df.to_csv('{}.csv'.format(loca), index=False)
    df.to_excel('{}.xlsx'.format(loca), index=False)
    print('Done Created Data')

if __name__ == '__main__':
    get_total_pages()
