import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import Format_rc
import Anoboy_rc

class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("UI_Aniscrap_New.ui", self)
        self.SubmitButton.clicked.connect(self.gotomediaplayer)

    def gotomediaplayer(self):
        UserName=self.UserName.text()
        Token=self.Token.text()
        print("Successfully logged in with UserName:", UserName, "and Token:", Token)
        mediaplayer=MediaPlayer()
        widget.addWidget(mediaplayer)
        widget.setCurrentIndex(widget.currentIndex()+1)

class MediaPlayer(QDialog):
    def __init__(self):
        super(MediaPlayer, self).__init__()
        loadUi("MediaPlayer.ui", self)
        self.Submit2Button.clicked.connect(self.MediaPlayerFunction)

    def MediaPlayerFunction(self):
        if self.radioMPV.isChecked() == True:
            print("Preparing link with MPV format.......")
        else:
            print("Preparing link with VLC fromat.......")

app=QApplication(sys.argv)
mainwindow=MediaPlayer()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(440)
widget.setFixedHeight(500)
widget.show()
app.exec_()