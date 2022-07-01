from PyQt5 import QtWidgets
from fn import APICall
from gui import gui, searchGui, details, config
from os import system
import json

def playEpisode(number:int, anime):
    source = "uservideo"
    player = "mpv"
    links = APICall.getMirror(anime.eplist[number])
    system(player+" "+links[source])

def showDetail(container,anime):
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
    container.Search.show()

def updateList(container, animes, MainWindow=None):
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
