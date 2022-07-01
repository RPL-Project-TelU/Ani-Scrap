import re, json
from sys import prefix
from html import unescape
from fn.objectClass import Anime
from fn import Scrapper
base_url = "https://anoboy.online/"

# querySearch adalah fungsi untuk mencari anime
# Masukan berupa string judul anime yang diinginkan
# Keluaran berupa list objek dari anime
def querySearch(query:str) -> list():
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

# selectEpisode adalah fungsi untuk mereturn link episode anime yang dipilih
# Masukan berupa episode anime yang ingin dipilih
# Keluaran berupa link episode yang dipilih
# For cli only
# def selectEpisode(animeUrl:str)->str:
#     r = Scrapper.parse_web(animeUrl)
#     epList = r.find('div',class_="eplister")
#     episodes = epList.findAll('li')
#     x = int(input("Pilih episode [1-{}] : ".format(len(episodes))))
#     return episodes[x-1].find('a')['href']

# CLI only

# selectMirror adalah fungsi untuk mereturn link mirror yang dipilih
# Masukan berupa link episode anime yang ingin ditonton
# Keluaran berupa link untuk menuju ke video anime
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

# recent berfungsi untuk mengambil anime yang baru diupload
# Keluaran berupa list dari objek anime
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

# getDetails adalah fungsi untuk menambahkan list episode dan
# sinopsis ke dalam objek anime
# Masukan berupa string berisikan judul anime yang dicari
# Keluaran berupa list episode dan sinopsis
def getDetails(anime:Anime):
    r = Scrapper.parse_web(anime.link)
    anime.desc = r.find('div',class_="entry-content").text
    for i in reversed(r.find("div",class_="eplister").findAll("a")):
        anime.eplist.append(i['href'])



