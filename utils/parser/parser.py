from requests import get
from bs4 import BeautifulSoup as bs


def parser():
    URL = "https://www.anekdot.ru/last/good/"
    response = get(URL)
    soup = bs(response.text, 'html.parser')
    anekdots_list = [i.text for i in soup.find_all('div', class_='text')]
    return anekdots_list



