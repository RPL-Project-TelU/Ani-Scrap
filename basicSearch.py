import requests
from bs4 import BeautifulSoup

page = requests.get('https://anoboy.live/anime/kimetsu-no-yaiba-season-2/')

after_bs = BeautifulSoup(page.content, 'html.parser')

find_data = after_bs.find_all(id='episodebox')

for x in find_data:
    print(x.text)
    
pilih = input("Silakan pilih episode yang anda inginkan : ")

print("Berikut ini adalah link yang anda inginkan : https://anoboy.live/kimetsu-no-yaiba-season-2-episode-"+pilih+"-sub-indo/")
