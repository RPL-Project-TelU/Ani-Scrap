import requests 
import pandas as pd 
from bs4 import BeautifulSoup 

import re, json
from kaasi_cli import scraper, anilist

Base_Url = "https://www2.kickassanime.ro/"
 
# link for extract html data 
def getdata(url): 
 r = requests.get(url) 
 return r.text 

def parse_appData(url):
    soup = scraper.parse_web(url)
    json_data = soup.find('script', text=re.compile("appData") )
    data = str(json_data)[str(json_data).find('{"clip'):str(json_data).find('} ||')+1]
    return json.loads(data)

def search_anime(query):
    Search_Url = "search?q="
    js = parse_appData(Base_Url+Search_Url+query)
    if ((not ("animes" in js)) or (len(js['animes']) == 0)):
        return None
    return js['animes']

def outputAnime(animeList):
    for i in range(len(animeList)):
        if i%2==0:
            print("\033[96m[",i,"] ",animeList[i]['name'],"\033[0m")
        else:
            print("\033[92m[",i,"] ",animeList[i]['name'],"\033[0m")

def selectAnime(animeList):
    outputAnime(animeList)
    x = int(input("\033[4m\033[92mInput\033[0m : "))
    return Base_Url+animeList[x]['slug'] 
 
def select_episode(link,direct=False,eps=None):
    episodes = parse_appData(link)['anime']['episodes']
    if direct:
        x = eps # NOT RELIABLE BECAUSE SOME ANIME HAVE 0 EPISODE IN THE LIST!
    else:
        x = int(input("Select episode [1-{episode}] : ".format(episode=len(episodes))))
    return parse_appData(Base_Url+episodes[len(episodes)-x]['slug'])

def check_link(js):
    if js['episode']['link1'] != '':
        return js['episode']['link1'] # RETURN EMBED VIDEO LINK
    
    elif js['ext_servers'] != None:
        for i in range(len(js['ext_servers'])):
            if js['ext_servers'][i]['name'] == 'Vidstreaming':
                return js['ext_servers'][i]['link'] # RETURN EMBED VIDEO LINK
    else:
        raise Exception("ONLY DIRECT DOWNLOAD AVAILABLE!!")

htmldata = getdata("https://anoboy.online/series/boruto-naruto-next-generations#/") 
soup = BeautifulSoup(htmldata, 'html.parser') 
 
movie_containers = '' 
link = '' 
 
for movie_containers in soup.find_all('div', class_ = 'bixbox synp'): 
 print(movie_containers.get_text()) 
 
animes = search_anime("naruto") #hasil search
outputAnime(animes)
# select eps
# animeLink = selectAnime(animes)
# episodeData = select_episode(animeLink)
# embedVideoLink = check_link(episodeData)

# for link in soup.find_all('a', href=True): 
#  print(link['href'])