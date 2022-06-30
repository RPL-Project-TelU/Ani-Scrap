from pypresence import Presence
import time, re, os
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import Format_rc
import Anoboy_rc
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QPushButton, QVBoxLayout

app = QtWidgets.QApplication([])
dlg = uic.loadUi("MediaPlayer.ui")

def firstSetup():
    with open('./config.json','w',encoding='utf-8') as config:
            setup = {}
            print("First time setup")
            if dlg.radioMPV.isChecked() == True:
                setup['player'] = "mpv"
            else:
                setup['player'] = "vlc"
            dlg.Submit2Button.clicked.connect(firstSetup)
            dlg.show()
            app.exec()
            setup['anilist'] = loginAnilist()
            config.write(str(setup))
            return setup
            #config.write(str(setup))
            #LoginAnilist=loginAnilist()
            #widget.addWidget(LoginAnilist)
            #widget.setCurrentIndex(widget.currentIndex()+1)

def loginAnilist():
    #with open('./config.json','w',encoding='utf-8') as config:
            dlg = uic.loadUi("Login_Anilist.ui")
            setup = {}
            if dlg.Button_yesAnilist.isChecked() == True:
                setup['anilist'] = "yes"
            else:
                setup['anilist'] = "no"
            dlg.SubmitButton.clicked.connect(loginAnilist)
            #setup['termux'] = input("Are you using Termux ? [y/n] : ") in ('Y','y')
            #setup['anilist'] = input("Login with anilist ? [y/n] : ") in ('y','Y')
            #if setup['anilist']:
            #setup['token'] = anilist.__init__()
                #setup['auto'] = input("Auto update anilist after watching anime ? [y/n] : ") in ('y','Y')
                #setup['username'] = eval(anilist.getUserId(setup['token']).content)['data']['Viewer']['name']
            dlg.show()
            app.exec()
            #config.write(str(setup))
            #sys.exit(app.exec_())
            return setup

def getconfig():
        with open('./config.json','r',encoding='utf-8') as config:
            return config.read()

widget=QtWidgets.QStackedWidget()
firstSetup()
loginAnilist()
getconfig()
