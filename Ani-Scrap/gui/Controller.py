from PyQt5 import QtWidgets
from function import webScrapper
from gui import gui, searchGui, details
from os import system

def playEpisode(number:int, anime):
    link = webScrapper.selectMirror(anime.eplist[number])
    system("mpv "+link)

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
    ui.updateList(webScrapper.querySearch(query))
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
