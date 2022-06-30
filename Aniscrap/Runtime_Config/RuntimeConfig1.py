import Anoboy_rc
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import sys

app = QtWidgets.QApplication([])
dlg = uic.loadUi("Login_Anilist.ui")

def firstSetup():
    with open('./config.json','w',encoding='utf-8') as config:
            setup = {}
            print("Open this url in the browser to get Token:\nhttps://anilist.co/api/v2/oauth/authorize?client_id=7201&response_type=token")
            MediaPlayer=dlg.lineEdit.text()
            setup['player'] = MediaPlayer
            Termux=dlg.lineEdit_2.text()
            setup['termux'] = Termux
            Token=dlg.lineEdit_3.text()
            setup['token'] = Token
            config.write(str(setup))
            dlg.ButtonSubmit.clicked.connect(firstSetup)
            dlg.show()
            app.exec()
            sys.exit(app.exec_())
            return setup

def getconfig():
        with open('./config.json','r',encoding='utf-8') as config:
            return config.read()

firstSetup()
getconfig()