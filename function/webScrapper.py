import re, json
from sys import prefix
from html import unescape
from function.objectClass import Anime
from function import Scrapper
base_url = "https://anoboy.live/"


def query(keyword:str,Ongoing:bool=True,query:str="",page:int=1,limit=8)->Anime:
    """
    Keyword = load_movie_last_update
    Keyword = load_movie_trending
    Keyword = load_search_movie
    """
    data = {
        "page": page,
        "limit": limit,
        "action": keyword,
    }
    if keyword == "load_search_movie":
        data["keyword"] = query
    if Ongoing:
        data["status"] = "Ongoing"
    enc_url = Scrapper.urlEncode(base_url+'my-ajax',data)
    jsData = Scrapper.api_get(enc_url).json()
    animes = []
    for i in jsData['data']:
        img = Scrapper.downloadFile("https://upload.anoboy.live/"+i['image'], r"tmp/")
        anime = Anime(i["post_name"], i['post_title'], i['status'], base_url+"movie/"+i['post_name'], r"tmp/"+img, i['post_content'],i['total_episode'])
        for j in range(1,int(i['total_episode'])+1):
            anime.eplist.append(base_url+anime.objName+"-episode-"+str(j)+"-sub-indo")
        anime.genres = eval(str(i["categories"]))
        animes.append(anime)
    return animes

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



