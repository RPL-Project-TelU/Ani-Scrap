from PyQt5 import QtWidgets
from fn import APICall
from gui import gui, searchGui, details, config
from os import system
from pypresence import Presence

import json, time

def playEpisode(number:int, anime):
    if RPC:
        RPC.update(state=anime.title, details="Watching anime", start=time.time(),large_image=anime.thumb_link,large_text="Episode "+str(number)+" of "+anime.eps)
    source = configFile["mirror"]
    player = configFile["player"]
    links = APICall.getMirror(anime.eplist[number])
    system(player+" "+links[source])

def showDetail(container,anime):
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

global configFile, RPC

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