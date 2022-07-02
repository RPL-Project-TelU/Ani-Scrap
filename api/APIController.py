import re, json
from sys import prefix
from html import unescape
from fn.objectClass import Anime
from fn import Scrapper
base_url = "https://anoboy.online/"

# Implementasi API swagger untuk scraping website anime yang hasilnya akan di return menjadi list of json
def querySearch(query:str) -> dict():
    r = Scrapper.parse_web(base_url+"search/"+query)
    c = r.findAll("article")
    animes = dict()
    for i in range(len(c)):
        status = re.findall(r"<span>.* Status : (.*).*?<",str(c[i]))[0]
        try:
            episode = re.findall(r"<span>.* Episode (\d*)",str(c[i]))[0]
        except:
            episode = re.findall(r"<span>.* Episode.*: (.*).*?<",str(c[i]))[0]         
        tag = c[i].find('a')
        img = Scrapper.downloadFile(tag.find('img')['src'], r"tmp/")
        # animes.append(Anime(tag['title'], status, episode, tag["href"], r"tmp/"+img))
        animes[tag['title']] = {"status": status, "episode": episode, "link": tag["href"], "thumb": r"tmp/"+img, "thumb_link": tag.find('img')['src']}
    return animes

# Implementasi API untuk scraping server video atau mirror nya, akan di scraping semua server lalu di return dalam bentuk json link video streaming nya
# Untuk saat ini hanya mirror uservideo yang sudah di scrap
def selectMirror(epUrl:str)->dict():
    url = Scrapper.decode_base64(epUrl,True)
    r = Scrapper.parse_web(url)
    # print(r)
    videoServer = r.find('select', class_="mirror").findAll('option')
    # for i in range(1,len(videoServer)):
    #     print("[{}] ".format(i)+videoServer[i].text)
    # x = int(input("Pilih source : "))
    link = re.findall(r'src="(.*?)"', Scrapper.decode_base64(videoServer[2]['value']))[0]
    page = Scrapper.parse_web(link)
    return {"uservideo": page.find('iframe')['src']}

# Implementasi API untuk mengambil sinopsis dan daftar episode Anime
# Yang nantinya akan direturn menjadi JSON
def getDetails(animeLink:str())->dict():
    url = Scrapper.decode_base64(animeLink,True)
    anime = dict()
    eplist = []
    r = Scrapper.parse_web(url)
    anime['sinopsis'] = r.find('div',class_="entry-content").text
    for i in reversed(r.find("div",class_="eplister").findAll("a")):
        eplist.append(i['href'])
    anime['episode'] = eplist
    return anime



