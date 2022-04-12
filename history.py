# 'with' is exception handling
import re,json
from kaasi_cli import kaa, scraper, anilist
def updateWatchHistory(epsData,anilist=None):
    epsLink = str(kaa.Base_Url+epsData['anime']['slug']+"/"+epsData['episode']['slug']+'-'+epsData['episode']['slug_id']).replace("\\","")
    try :
        watch_history['anime'][epsData['anime']['name']] = {'label' : epsData['episode']['name'], 'next-link' : kaa.Base_Url+epsData['episode']['next']['slug'], 'episodeLink' : epsLink, 'status': epsData['anime']['status']}
        watch_history['last'] = {'name' : epsData['anime']['name'] ,'episode-label' : epsData['episode']['name'], 'next-link' : kaa.Base_Url+epsData['episode']['next']['slug'], 'episodeLink' : epsLink, 'status' : epsData['anime']['status']}
    except :
        watch_history['anime'][epsData['anime']['name']] = {'label' : epsData['episode']['name'], 'next-link' : '', 'episodeLink' : epsLink, 'status' : epsData['anime']['status']}
        watch_history['last'] = {'name' : epsData['anime']['name'] ,'episode-label' : epsData['episode']['name'], 'next-link' : '', 'episodeLink' : epsLink, 'status' : epsData['anime']['status']}
    if anilist != None:
        watch_history['anime'][epsData['anime']['name']]['mediaId'] = anilist['media']['id']
        watch_history['last']['mediaId'] = anilist['media']['id']
        if epsData['anime']['status'] == "Currently Airing" and anilist['media']['status'] in ('RELEASING','NOT_YET_RELEASED'):
            watch_history['airing'][epsData['anime']['name']] = watch_history['anime'][epsData['anime']['name']]
            watch_history['airing'][epsData['anime']['name']]['airingAt'] = anilist['media']['nextAiringEpisode']['airingAt']
    elif epsData['anime']['status'] == "Currently Airing":
        watch_history['airing'][epsData['anime']['name']] = watch_history['anime'][epsData['anime']['name']]
    with open('history.txt','w',encoding='utf-8') as histo:
        histo.write(str(watch_history))


watch_history = {'anime' : {}, 'last' : {}, 'airing' : {}}
try:
    with open('./history.txt','r',encoding='utf-8') as histo:
        watch_history = eval(histo.read())
except:
    with open('./history.txt','w',encoding='utf-8') as histo:
        histo.write(str(watch_history))