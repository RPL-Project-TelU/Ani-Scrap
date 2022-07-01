from fn.Scrapper import api_get
from fn.Scrapper import encode_base64
from fn.objectClass import Anime
flassger_url = "http://127.0.0.1:5000"


# searchAnime adalah fungsi untuk menampilkan list daftar anime yang dicari
# Masukkan berupa string yang berisikan judul anime yang dicari 
# Menggunakan json 
# Keluaran berupa list anime yang dicari
def searchAnime(query:str)->list():
    animes = []
    r = api_get(flassger_url+"/search-anime/"+query)
    json = r.json()
    for k in json:
        animes.append(Anime(k, json[k]['status'], json[k]['episode'], json[k]['link'], json[k]['thumb'], json[k]['thumb_link']))
    return animes

# getMirror adalah fungsi implementasi API dari selectMirror 
# Masukkan berupa link anime yang ingin ditonton
# Keluaran berupa json
def getMirror(epUrl:str)->dict():
    encodedUrl = encode_base64(epUrl)
    r = api_get(flassger_url+"/get-video/"+encodedUrl)
    return r.json()

# getDetails adalah  untuk implementasi dari API
# Masukkan berupa link anime 
# Keluaran berupa json yang berisikan deskripsi anime dan
# episode list anime 
def getDetails(anime:Anime):
    encodedUrl = encode_base64(anime.link)
    r = api_get(flassger_url+"/get-anime/"+encodedUrl)
    json = r.json()
    anime.desc = json['sinopsis']
    anime.eplist = json['episode']
