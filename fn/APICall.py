from fn.Scrapper import api_get
from fn.Scrapper import encode_base64
from fn.objectClass import Anime
flassger_url = "http://127.0.0.1:5000"

def searchAnime(query:str)->list():
    animes = []
    r = api_get(flassger_url+"/search-anime/"+query)
    json = r.json()
    for k in json:
        animes.append(Anime(k, json[k]['status'], json[k]['episode'], json[k]['link'], json[k]['thumb'], json[k]['thumb_link']))
    return animes

def getMirror(epUrl:str)->dict():
    encodedUrl = encode_base64(epUrl)
    r = api_get(flassger_url+"/get-video/"+encodedUrl)
    return r.json()
    
def getDetails(anime:Anime):
    encodedUrl = encode_base64(anime.link)
    r = api_get(flassger_url+"/get-anime/"+encodedUrl)
    json = r.json()
    anime.desc = json['sinopsis']
    anime.eplist = json['episode']
