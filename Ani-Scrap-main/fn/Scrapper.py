import urllib.parse, os
import cloudscraper, re, base64, requests, random
from bs4 import BeautifulSoup
from typing import TypeVar
# decode_Base64 adalah fungsi untuk mendecode atau mentranslate dari base 64 ke ascii
# Masukan berupa string berbasis base64 dan sebuah bool untuk memastikan metode yg digunakan
# Keluaran berupa string berbasis ascii
def decode_base64(text:str,lossless:bool=False)->str:
    base64_bytes = text.encode('ascii')
    if lossless:
        base64_bytes += b'=='
    message_bytes = base64.b64decode(base64_bytes)
    return message_bytes.decode('ascii')

T = TypeVar("T")
def encode_base64(text:T)->T:
    message_bytes = text.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message.replace("=", "")

def parse_web(url:str,headers:str=None,raw:bool=False):
    try:
        scraper = cloudscraper.create_scraper()
        page = scraper.get(url,headers=headers).content
    except:
        page = requests.get(url,headers=headers).content
    if raw:
        return page
    return BeautifulSoup(page, "html.parser")

def api_get(url:str,json:str=None,headers:str=None,data:str=None,post:bool=False)->requests.Response:
    try:
        scraper = cloudscraper.create_scraper()
        if post:
            page = scraper.post(url,headers=headers,json=json,data=data)
        else:
            page = scraper.get(url,headers=headers,json=json,data=data)
    except:
        if post:
            page = requests.post(url,headers=headers,json=json,data=data)    
        else:
            page = requests.get(url,headers=headers,json=json,data=data)
    return page

def urlEncode(url:str, data:dict)->str:
    param = urllib.parse.urlencode(data)
    return url+"?"+param

def downloadFile(url,path):
    try:
        fn = re.findall(r".*\/(.*.jpg|.*.png)", url)[0]
    except:
        print(url)
        return ""
    if os.path.isfile(path+fn):
        return fn
    r = requests.get(url).content
    with open(f"{path}{fn}", "wb+") as f:
        f.write(r)
    return fn

