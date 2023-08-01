import os
import requests
from bs4 import BeautifulSoup

url = 'https://id.carousell.com/categories/computers-and-tablets-333'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 '
                  'Safari/537.36'}

res = requests.get(url, headers=headers)


def get_total_pages():
    soup = BeautifulSoup(res.text, 'html.parser')
    laptop_best_match = soup.find(attrs={'class': 'D_Z asm-browse-listings'})
    titles = laptop_best_match.findAll(attrs={'class': 'D_sZ D_BK'})
    for title in titles:
        print(title.find('p', attrs={
            'class': 'D_qz M_kQ D_pl M_kE D_q_ M_kR D_qE M_kV D_qH M_kY D_qK M_lb D_qM M_le D_qI M_kZ D_qQ'}).text)


if __name__ == '__main__':
    get_total_pages()
