import os
import requests
from bs4 import BeautifulSoup

url = 'https://karirhub.kemnaker.go.id/vacancies/industrial?'
site = 'https://glints.com/id/opportunities/'
params = {
    'keyword': 'marketing',
    'region': 'DKI%20JAKARTA,%20Indonesia',
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

res = requests.get(url, params=params, headers=headers)
print(res.status_code)
def get_total_pages():
    params = {
        'keyword': 'marketing',
        'region': 'DKI%20JAKARTA,%20Indonesia',
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
    pagination = soup.find('div', 'pagination')
    pages = pagination.find_all('li')
    for page in pages:
        total_pages.append(page.text)

    total = int(max(total_pages))
    return total

def get_all_items():
    params = {
        'q': 'marketing',
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
        title = item.find('h2', 'media-heading h4').text
        print(title)





if __name__ == '__main__':
    get_all_items()
