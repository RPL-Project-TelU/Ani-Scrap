import sys,json

from PyQt5 import QtWidgets
from gui import gui, Controller
from fn import webScrapper, APICall
from pypresence import Presence

def firstSetup():
    try:
        with open('./config.json','r',encoding='utf-8') as config:
            return json.load(config)
    except:
        with open('./config.json','w',encoding='utf-8') as config:
            setup = dict()
            setup["player"] = "mpv"
            setup["discordRPC"] = True
            setup["mirror"] = "uservideo"
            config.write(json.dumps(setup))
            return setup

def init():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    return app, ui, MainWindow
    
if __name__ == "__main__":
    configFile = firstSetup()
    app, ui, MainWindow = init()
    print("Waiting for anoboy.online")
    # Controller.updateList(ui, APICall.searchAnime(" "),MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())