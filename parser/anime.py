import requests
from bs4 import BeautifulSoup

URL = "https://ru.sputnik.kg/news/"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}


def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


# print(get_html(URL))

def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_='list__content')
    newskg = []
    for item in items:
        newskg.append({
            'title': item.find('a', class_='list__title').getText(),
            'date': item.find("span", class_="list__date").getText(),
            'link': 'https://ru.sputnik.kg' + item.get('href'),
            'photo': 'https://ru.sputnik.kg' + item.find('img', class_='responsive_img m-list-img').get('src')
        })
        return newskg
#
#     print(items)
#
#
# html = get_html(URL)
# print(html.text)


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        answer = get_data(html.text)
        return answer
    else:
        raise Exception('Error in parser')


