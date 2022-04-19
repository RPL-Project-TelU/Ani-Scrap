import re, json
from sys import prefix
from html import unescape
from function.objectClass import Anime
from function import Scrapper
base_url = "https://anoboy.live/"


def querySearch(query:str) -> str:
    r = Scrapper.parse_web(base_url+"search/"+query)
    c = r.findAll("article")
    animes = []
    for i in range(len(c)):
        status = re.findall(r"<span>.* Status : (.*).*?<",str(c[i]))[0]
        try:
            episode = re.findall(r"<span>.* Episode (\d*)",str(c[i]))[0]
        except:
            episode = re.findall(r"<span>.* Episode.*: (.*).*?<",str(c[i]))[0]         
        tag = c[i].find('a')
        img = Scrapper.downloadFile(tag.find('img')['src'], r"tmp/")
        animes.append(Anime(tag['title'], status, episode, tag["href"], r"tmp/"+img))
    return animes

def selectEpisode(animeUrl:str)->str:
    r = Scrapper.parse_web(animeUrl)
    epList = r.find('div',class_="eplister")
    episodes = epList.findAll('li')
    x = int(input("Pilih episode [1-{}] : ".format(len(episodes))))
    return episodes[x-1].find('a')['href']

def selectMirror(epUrl:str)->str:
    r = Scrapper.parse_web(epUrl)
    # print(r)
    videoServer = r.find('select', class_="mirror").findAll('option')
    # for i in range(1,len(videoServer)):
    #     print("[{}] ".format(i)+videoServer[i].text)
    # x = int(input("Pilih source : "))
    link = re.findall(r'src="(.*?)"', Scrapper.decode_base64(videoServer[2]['value']))[0]
    page = Scrapper.parse_web(link)
    return page.find('iframe')['src']

def recent()->Anime:
    r = Scrapper.parse_web(base_url)
    c = r.findAll("article")
    animes = []
    for i in range(len(c)):
        status = re.findall(r"<span>.* Status : (.*).*?<",str(c[i]))[0]
        try:
            episode = re.findall(r"<span>.* Episode (\d*)",str(c[i]))[0]
        except:
            episode = re.findall(r"<span>.* Episode.*: (.*).*?<",str(c[i]))[0]        
        tag = c[i].find('a')
        img = Scrapper.downloadFile(tag.find('img')['src'], r"tmp/")
        animes.append(Anime(tag['title'],status, episode, tag["href"], r"tmp/"+img))
    return animes

def getDetails(anime:Anime)->Anime:
    r = Scrapper.parse_web(anime.link)
    anime.desc = r.find('div',class_="entry-content").text
    for i in reversed(r.find("div",class_="eplister").findAll("a")):
        anime.eplist.append(i['href'])
    return anime



