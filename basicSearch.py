import requests
from bs4 import BeautifulSoup

page = requests.get('https://anoboy.live/anime/kimetsu-no-yaiba-season-2/')

after_bs = BeautifulSoup(page.content, 'html.parser')

find_data = after_bs.find_all(id='episodebox')

for x in find_data:
    print(x.text)