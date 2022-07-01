from PyQt5 import QtWidgets
import sys,json
from gui import gui, Controller
from fn import webScrapper

def firstSetup():
    try:
        with open('./config.json','r',encoding='utf-8') as config:
            return json.load(config)
    except:
        with open('./config.json','w',encoding='utf-8') as config:
            setup = dict()
            setup["player"] = "MPV"
            setup["discordRPC"] = False
            setup["mirror"] = "uservideo"
            config.write(json.dumps(setup))
            return setup

def init():
    configFile = firstSetup()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    return app, ui, MainWindow
    
if __name__ == "__main__":
    # Setup
    app, ui, MainWindow = init()
    print("Waiting for anoboy.online")
    Controller.updateList(ui, webScrapper.recent(),MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())