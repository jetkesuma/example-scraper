import os
import requests
from bs4 import BeautifulSoup

url = 'https://www.loker.id/cari-lowongan-kerja?'
site = 'https://www.loker.id/'
params = {
    'q': 'web developer',
    'lokasi': 'jakarta',
    'category': '0',
    'pendidikan': '0',
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

res = requests.get(url, params=params, headers=headers)

def get_total_pages():
    params = {
        'q': 'web developer',
        'lokasi': 'jakarta',
        'category': '0',
        'pendidikan': '0',
    }

    res = requests.get(url, params=params, headers=headers)

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()

    total_pages = []
    # scraping Step
    soup = BeautifulSoup(res.text, 'html.parser')
    pagination = soup.find('ul', 'pagination pagination-sm')
    pages = pagination.find_all('li')
    for page in pages:
        total_pages.append(page.text)

    total = int(max(total_pages))
    return total

def get_all_items():
    params = {
        'q': 'web developer',
        'lokasi': 'jakarta',
        'category': '0',
        'pendidikan': '0',
    }
    res = requests.get(url, params=params, headers=headers)
    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()
    soup = BeautifulSoup(res.text, 'html.parser')

    # Scraping Process
    contents = soup.find_all('div', 'm-b-40')

    # Pick Items

    for item in contents:
        pkk = item.find('h2', 'media-heading h4')
        title = pkk.text
        try:
            link = site + pkk.find('a')['href']
        except:
            link = 'Link Not Available'
        print(link)




if __name__ == '__main__':
    get_all_items()
