from PyQt5 import QtWidgets, QtGui
from fn import APICall
from gui import gui, searchGui, details, config, history, anilistSetting
from os import system
from pypresence import Presence
from datetime import date
from fn.objectClass import Anime

import json, time


# Fungsi untuk menkonversi atau parsing json menjadi objek anime
# Kebalikan dari fungsi jsontoAnime
# Fungsi ini akan memparsing objek anime menjadi dictionary
def animeToDict(anime:Anime)->dict():
    aniJs = dict()
    aniJs[anime.objName] = {"title" : anime.title, "link": anime.link, "thumb": anime.thumb, "thumb_link": anime.thumb_link, "status": anime.status, "desc": anime.desc, "eplist": anime.eplist, "eps": anime.eps, "lastwatch": anime.lastwatch}
    return aniJs

# Fungsi untuk menambahkan objek anime kedalam history
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

# Fungsi untuk memutar suatu episode anime
# Setelah diputar maka akan dimasukkan ke dalam history
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

# Fungsi untuk membuka widget pencarian anime
def showDetail(container,anime:Anime):
    if RPC:
        RPC.update(state=anime.title, details="Checking anime", large_image=anime.thumb_link)
    print(anime.title)
    container.Details = QtWidgets.QWidget()
    ui = details.Ui_Form()
    ui.setupUi(container.Details, anime)
    container.Details.show()

# Fungsi yang aktif jika tombol search di klik di gui
def btnSearchClick(container):
    query = container.textEdit.toPlainText()
    container.Search = QtWidgets.QWidget()
    ui = searchGui.Ui_Form()
    ui.setupUi(container.Search)
    ui.updateList(APICall.searchAnime(query))
    if RPC:
        RPC.update(state="Searching "+query, details="Browsing anime")
    container.Search.show()

# Fungsi yang berguna untuk menambah objek anime kedalam UI atau frame box yang maximal berjumlah 8
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

# Fungsi untuk membuka widget config
def openConfig(container):
    if RPC:
        RPC.update(state="In Setting", details="Configuring some Configuration")
    container.config = QtWidgets.QWidget()
    ui = config.Ui_Config()
    ui.setupUi(container.config)
    container.config.show()

# Fungsi untuk menyimpan cofigurasi yang sudah diatur di widget config
def saveConfig(container):
    config = dict()
    config["player"] = container.combo_player.currentText()
    config["discordRPC"] = container.cbox_discord.isChecked()
    config["mirror"] = container.combo_mirror.currentText()
    with open('./config.json','w',encoding='utf-8') as fileConfig:
        fileConfig.write(json.dumps(config))
    container.btn_save.setEnabled(False)

# Fungsi untuk membuka widget history
def openHistory(container):
    if RPC:
        RPC.update(state="Checking History", details="Looking back at the past")
    container.history = QtWidgets.QWidget()
    ui = history.Ui_Form()
    ui.setupUi(container.history)
    container.history.show()    

# Fungsi untuk membaca history.json dan menampilkan nya kedalam widget history
def loadItem(container):
    global listofAnime
    with open('./history.json','r',encoding='utf-8') as histoReader:
        history = json.load(histoReader)
    listofAnime = jsontoAnime(history)
    for i in listofAnime:
        item = QtWidgets.QListWidgetItem()
        item.setText(i.title)
        container.list_history.addItem(item)

# Fungsi untuk menkonversi atau parsing json menjadi objek anime
def jsontoAnime(js:json)->list():
    animes = []
    for k in js:
        anime = Anime(js[k]['title'], js[k]['status'], js[k]['eps'], js[k]['link'], js[k]['thumb'], js[k]['thumb_link'])
        anime.desc = js[k]['desc']
        anime.eplist = js[k]['eplist']
        anime.lastwatch = js[k]['lastwatch']
        animes.append(anime)
    return animes

# Fungsi untuk mendektsi perubahan item pada widget history, jika selected item berubah maka akan mengubah juga label yang ada di gui tersebut
def itemChanged(container,idx):
    global listofAnime
    container.lbl_outTitle.setText(listofAnime[idx].title)
    container.lbl_outEps.setText(str(listofAnime[idx].eps))
    container.lbl_outTotalEps.setText(str(len(listofAnime[idx].eplist)))
    container.lbl_outStatus.setText(listofAnime[idx].status)
    container.lbl_img.setPixmap(QtGui.QPixmap(listofAnime[idx].thumb))
    container.txt_sinopsis.setPlainText(listofAnime[idx].desc)
    container.lbl_outDate.setText(listofAnime[idx].lastwatch)

# Fungsi untuk menampilkan widget konfigurasi anilist
def openAnilistSetting(container):
    if RPC:
        RPC.update(state="Setting up anilist", details="Connecting...")
    container.anilistSetting = QtWidgets.QWidget()
    ui = anilistSetting.Ui_Form()
    ui.setupUi(container.anilistSetting)
    container.anilistSetting.show()      

# Fungsi untuk mengembalikan objek anime dari index pada widget history
def getAnimeIndex(container):
    return listofAnime[container.list_history.currentRow()]

# Fungsi untuk menyimpan konfigurasi anilist
def saveAniConfig(container):
    aniCfg = dict()
    aniCfg['token'] = container.textEdit_2.toPlainText()
    aniCfg['username'] = container.txt_username.toPlainText()
    aniCfg['autoUpdate'] = container.cAutoUpdate.isChecked()
    with open('./anilist.json','w',encoding='utf-8') as aniWriter:
        aniWriter.write(json.dumps(aniCfg))
    container.btn_save.setEnabled(False)

# Fungsi untuk melanjutkan anime yang terakhir kali di tonton
def continueWatching(container):
    with open('./history.json','r',encoding='utf-8') as histoReader:
        history = json.load(histoReader)
    animes = jsontoAnime(history)
    showDetail(container, animes[-1])

# INIT kode dibawah akan selalu dijalankan ketika module Controller.py dipanggil
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