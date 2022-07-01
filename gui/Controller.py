from PyQt5 import QtWidgets, QtGui
from fn import APICall
from gui import gui, searchGui, details, config, history, anilistSetting
from os import system
from pypresence import Presence
from datetime import date
from fn.objectClass import Anime

import json, time

def jsontoAnime(js:json)->list():
    animes = []
    for k in js:
        anime = Anime(k, js[k]['status'], js[k]['episode'], js[k]['link'], js[k]['thumb'], js[k]['thumb_link'])
        anime.desc = js[k]['desc']
        anime.eplist = js[k]['eplist']
        anime.eps = js[k]['eps']
        anime.lastwatch = js[k]['lastwatch']
        animes.append(anime)
    return animes

def animeToDict(anime:Anime)->dict():
    aniJs = dict()
    aniJs[anime.objName] = {"title" : anime.title, "link": anime.link, "thumb": anime.thumb, "thumb_link": anime.thumb_link, "status": anime.status, "desc": anime.desc, "eplist": anime.eplist, "eps": anime.eps, "lastwatch": anime.lastwatch}
    return aniJs

def addToHistory(anime:Anime):
    try:
        with open('./history.json','r',encoding='utf-8') as histoReader:
            history = json.load(histoReader)
            history.update(animeToDict(anime))
            with open('./history.json','w',encoding='utf-8') as histoWriter:
                histoWriter.write(json.dumps(history))
    except:
        with open('./history.json','w',encoding='utf-8') as histoWriter:
            histoWriter.write(json.dumps(animeToDict(anime)))

def playEpisode(number:int, anime:Anime):
    if RPC:
        RPC.update(state=anime.title, details="Watching anime", start=time.time(),large_image=anime.thumb_link,large_text="Episode "+str(number)+" of "+anime.eps)
    source = configFile["mirror"]
    player = configFile["player"]
    try:
        print("Getting mirror")
        links = APICall.getMirror(anime.eplist[number])
    except:
        print("failed to fetch mirror")
        return
    anime.lastwatch = str(date.today())
    anime.eps = number
    addToHistory(anime)
    print("Playing...")
    system(player+" "+links[source])


def showDetail(container,anime:Anime):
    if RPC:
        RPC.update(state=anime.title, details="Checking anime", large_image=anime.thumb_link)
    print(anime.title)
    container.Details = QtWidgets.QWidget()
    ui = details.Ui_Form()
    ui.setupUi(container.Details, anime)
    container.Details.show()

def btnSearchClick(container):
    query = container.textEdit.toPlainText()
    container.Search = QtWidgets.QWidget()
    ui = searchGui.Ui_Form()
    ui.setupUi(container.Search)
    ui.updateList(APICall.searchAnime(query))
    if RPC:
        RPC.update(state="Searching "+query, details="Browsing anime")
    container.Search.show()

def updateList(container, animes, MainWindow=None):
    if RPC:
        RPC.update(state="In Main Menu", details="Browsing anime")
    x, y = 0, 0
    for i in range(8):
        try:
            anime = animes[i]
            print(anime.title)
            if MainWindow:
                animeBox = container.addAnimeBox(MainWindow,anime)
            else:
                animeBox = container.addAnimeBox(container,anime)
            container.gridAnimeList.addWidget(animeBox,x,y,1,1)
            if y == 1:
                y = 0
                x += 1
            else:
                y+=1
        except:
            continue
def openConfig(container):
    if RPC:
        RPC.update(state="In Setting", details="Configuring some Configuration")
    container.config = QtWidgets.QWidget()
    ui = config.Ui_Config()
    ui.setupUi(container.config)
    container.config.show()

def saveConfig(container):
    config = dict()
    config["player"] = container.combo_player.currentText()
    config["discordRPC"] = container.cbox_discord.isChecked()
    config["mirror"] = container.combo_mirror.currentText()
    with open('./config.json','w',encoding='utf-8') as fileConfig:
        fileConfig.write(json.dumps(config))
    container.btn_save.setEnabled(False)

def openHistory(container):
    if RPC:
        RPC.update(state="Checking History", details="Looking back at the past")
    container.history = QtWidgets.QWidget()
    ui = history.Ui_Form()
    ui.setupUi(container.history)
    container.history.show()    

def loadItem(container):
    global listofAnime
    with open('./history.json','r',encoding='utf-8') as histoReader:
        history = json.load(histoReader)
    listofAnime = jsontoAnime(history)
    for i in listofAnime:
        item = QtWidgets.QListWidgetItem()
        item.setText(i.title)
        container.list_history.addItem(item)

def jsontoAnime(js:json)->list():
    animes = []
    for k in js:
        anime = Anime(js[k]['title'], js[k]['status'], js[k]['eps'], js[k]['link'], js[k]['thumb'], js[k]['thumb_link'])
        anime.desc = js[k]['desc']
        anime.eplist = js[k]['eplist']
        anime.lastwatch = js[k]['lastwatch']
        animes.append(anime)
    return animes

def itemChanged(container,idx):
    global listofAnime
    container.lbl_outTitle.setText(listofAnime[idx].title)
    container.lbl_outEps.setText(str(listofAnime[idx].eps))
    container.lbl_outTotalEps.setText(str(len(listofAnime[idx].eplist)))
    container.lbl_outStatus.setText(listofAnime[idx].status)
    container.lbl_img.setPixmap(QtGui.QPixmap(listofAnime[idx].thumb))
    container.txt_sinopsis.setPlainText(listofAnime[idx].desc)

def openAnilistSetting(container):
    if RPC:
        RPC.update(state="Setting up anilist", details="Connecting...")
    container.anilistSetting = QtWidgets.QWidget()
    ui = anilistSetting.Ui_Form()
    ui.setupUi(container.anilistSetting)
    container.anilistSetting.show()      

def getAnimeIndex(container):
    return listofAnime[container.list_history.currentRow()]

def saveAniConfig(container):
    aniCfg = dict()
    aniCfg['token'] = container.textEdit_2.toPlainText()
    aniCfg['username'] = container.txt_username.toPlainText()
    aniCfg['autoUpdate'] = container.cAutoUpdate.isChecked()
    with open('./anilist.json','w',encoding='utf-8') as aniWriter:
        aniWriter.write(json.dumps(aniCfg))
    container.btn_save.setEnabled(False)

global configFile, RPC, listofAnime

with open('./config.json','r',encoding='utf-8') as configReader:
    configFile = json.load(configReader)
        
if configFile["discordRPC"]:
    try:
        client_id = "992433245197176874"  
        RPC = Presence(client_id=client_id)
        RPC.connect()
    except:
        RPC = False
        print("Can't Connect to discord")
else:
    RPC = False