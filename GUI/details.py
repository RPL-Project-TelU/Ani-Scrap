# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'details.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from function import webScrapper

class Ui_Form(object):
    def setupUi(self, Form, anime):
        anime = webScrapper.getDetails(anime)
        Form.setObjectName("Form")
        Form.resize(1000, 800)
        Form.setMinimumSize(QtCore.QSize(1000, 800))
        Form.setMaximumSize(QtCore.QSize(1000, 800))
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1001, 802))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.detailsLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.detailsLayout.setContentsMargins(10, 10, 10, 10)
        self.detailsLayout.setObjectName("detailsLayout")
        self.lbl_title = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_title.setMinimumSize(QtCore.QSize(650, 30))
        self.lbl_title.setMaximumSize(QtCore.QSize(650, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setScaledContents(True)
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setWordWrap(True)
        self.lbl_title.setObjectName("lbl_title")
        self.detailsLayout.addWidget(self.lbl_title, 0, 1, 1, 1)
        self.lbl_synopsis = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_synopsis.setMinimumSize(QtCore.QSize(650, 30))
        self.lbl_synopsis.setMaximumSize(QtCore.QSize(650, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbl_synopsis.setFont(font)
        self.lbl_synopsis.setObjectName("lbl_synopsis")
        self.detailsLayout.addWidget(self.lbl_synopsis, 1, 1, 1, 1)
        self.epsLayout = QtWidgets.QHBoxLayout()
        self.epsLayout.setObjectName("epsLayout")
        self.sbox_eps = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.sbox_eps.setMinimumSize(QtCore.QSize(200, 30))
        self.sbox_eps.setMaximumSize(QtCore.QSize(200, 30))
        self.sbox_eps.setMinimum(1)
        self.sbox_eps.setMaximum(len(anime.eplist))
        self.sbox_eps.setObjectName("sbox_eps")
        self.sbox_eps.setValue(len(anime.eplist))
        self.epsLayout.addWidget(self.sbox_eps)
        self.btn_epsSel = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.selectEpisode(int(self.sbox_eps.text())-1, anime))
        self.btn_epsSel.setMinimumSize(QtCore.QSize(200, 30))
        self.btn_epsSel.setMaximumSize(QtCore.QSize(200, 30))
        self.btn_epsSel.setObjectName("btn_epsSel")
        self.epsLayout.addWidget(self.btn_epsSel)
        self.detailsLayout.addLayout(self.epsLayout, 3, 1, 1, 1)
        self.lbl_episode = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_episode.setMinimumSize(QtCore.QSize(300, 50))
        self.lbl_episode.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbl_episode.setFont(font)
        self.lbl_episode.setObjectName("lbl_episode")
        self.detailsLayout.addWidget(self.lbl_episode, 3, 0, 1, 1)
        self.episodeListLayout = QtWidgets.QGridLayout()
        self.episodeListLayout.setObjectName("episodeListLayout")
        self.frameEps = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frameEps.setMinimumSize(QtCore.QSize(150, 30))
        self.frameEps.setMaximumSize(QtCore.QSize(150, 30))
        self.frameEps.setFrameShape(QtWidgets.QFrame.Box)
        self.frameEps.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameEps.setLineWidth(1)
        self.frameEps.setObjectName("frameEps")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frameEps)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 151, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.frameEpsLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.frameEpsLayout.setContentsMargins(0, 0, 0, 0)
        self.frameEpsLayout.setObjectName("frameEpsLayout")
        self.lbl_eps = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.lbl_eps.setMaximumSize(QtCore.QSize(100, 25))
        self.lbl_eps.setObjectName("lbl_eps")
        self.frameEpsLayout.addWidget(self.lbl_eps)
        self.btn_play = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_play.setMaximumSize(QtCore.QSize(50, 25))
        self.btn_play.setObjectName("btn_play")
        self.frameEpsLayout.addWidget(self.btn_play)
        self.episodeListLayout.addWidget(self.frameEps, 0, 0, 1, 1)
        self.detailsLayout.addLayout(self.episodeListLayout, 4, 0, 1, 2)
        self.lbl_img = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_img.setMinimumSize(QtCore.QSize(300, 400))
        self.lbl_img.setMaximumSize(QtCore.QSize(300, 400))
        self.lbl_img.setText("")
        self.lbl_img.setPixmap(QtGui.QPixmap(anime.thumb))
        self.lbl_img.setScaledContents(True)
        self.lbl_img.setObjectName("lbl_img")
        self.detailsLayout.addWidget(self.lbl_img, 0, 0, 3, 1)
        self.txt_synopsis = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.txt_synopsis.setMinimumSize(QtCore.QSize(650, 100))
        self.txt_synopsis.setMaximumSize(QtCore.QSize(50, 400))
        font = QtGui.QFont()
        font.setFamily("Fira Sans Book")
        font.setPointSize(14)
        self.txt_synopsis.setFont(font)
        self.txt_synopsis.setInputMethodHints(QtCore.Qt.ImhNone)
        self.txt_synopsis.setPlainText(anime.desc)
        self.txt_synopsis.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.txt_synopsis.setPlaceholderText("")
        self.txt_synopsis.setObjectName("txt_synopsis")
        self.detailsLayout.addWidget(self.txt_synopsis, 2, 1, 1, 1)

        self.lbl_title.setText(anime.title)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Details"))
        self.lbl_synopsis.setText(_translate("Form", "Synopsis :"))
        self.btn_epsSel.setText(_translate("Form", "Play Episode"))
        self.lbl_episode.setText(_translate("Form", "EPISODE : "))
        self.lbl_eps.setText(_translate("Form", "Episode xxxxx"))
        self.btn_play.setText(_translate("Form", "Play"))

    def selectEpisode(self, number:int, anime):
        print(anime.eplist[number])

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())
