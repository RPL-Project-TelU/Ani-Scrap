import requests 
import pandas as pd 
from bs4 import BeautifulSoup 
 

def getdata(url): 
 r = requests.get(url) 
 return r.text 
 
htmldata = getdata("https://anoboy.online/series/boruto-naruto-next-generations#/") 
soup = BeautifulSoup(htmldata, 'html.parser') 
 

for movie_containers in soup.find_all('div', class_ = 'bixbox synp'): 
 print(movie_containers.get_text()) 
 
for link in soup.find_all('a', href=True):  
 print(link['href'])
