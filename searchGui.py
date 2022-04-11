# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchGui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import details

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 800)
        Form.setMinimumSize(QtCore.QSize(1000, 800))
        Form.setMaximumSize(QtCore.QSize(1000, 800))
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-10, 0, 1011, 801))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridAnimeList = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridAnimeList.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridAnimeList.setContentsMargins(25, 25, 25, 25)
        self.gridAnimeList.setObjectName("gridAnimeList")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def addAnimeBox(self,anime):
        frameAnime = QtWidgets.QFrame(self.gridLayoutWidget)
        frameAnime.setMaximumSize(QtCore.QSize(450, 150))
        frameAnime.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        frameAnime.setFrameShape(QtWidgets.QFrame.Box)
        frameAnime.setFrameShadow(QtWidgets.QFrame.Raised)
        frameAnime.setLineWidth(5)
        frameAnime.setObjectName(anime.objName)
        gridLayoutWidget_2 = QtWidgets.QWidget(frameAnime)
        gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 451, 151))
        gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        gridAnime = QtWidgets.QGridLayout(gridLayoutWidget_2)
        gridAnime.setContentsMargins(10, 10, 10, 10)
        gridAnime.setHorizontalSpacing(15)
        gridAnime.setObjectName("gridAnime")
        lblstatus = QtWidgets.QLabel(gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(lblstatus.sizePolicy().hasHeightForWidth())
        lblstatus.setSizePolicy(sizePolicy)
        lblstatus.setMaximumSize(QtCore.QSize(225, 30))
        lblstatus.setObjectName("lblstatus")
        gridAnime.addWidget(lblstatus, 1, 1, 1, 1)
        lbl_eps = QtWidgets.QLabel(gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(lbl_eps.sizePolicy().hasHeightForWidth())
        lbl_eps.setSizePolicy(sizePolicy)
        lbl_eps.setMaximumSize(QtCore.QSize(225, 30))
        lbl_eps.setObjectName("lbl_eps")
        gridAnime.addWidget(lbl_eps, 2, 1, 1, 1)
        lbl_title = QtWidgets.QLabel(gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(lbl_title.sizePolicy().hasHeightForWidth())
        lbl_title.setSizePolicy(sizePolicy)
        lbl_title.setMaximumSize(QtCore.QSize(225, 30))
        lbl_title.setObjectName("lbl_title")
        gridAnime.addWidget(lbl_title, 0, 1, 1, 1)
        lbl_img = QtWidgets.QLabel(gridLayoutWidget_2)
        lbl_img.setMaximumSize(QtCore.QSize(90, 125))
        lbl_img.setScaledContents(True)
        lbl_img.setText("")
        lbl_img.setPixmap(QtGui.QPixmap(anime.thumb))
        lbl_img.setObjectName("lbl_img")
        gridAnime.addWidget(lbl_img, 0, 0, 3, 1)
        btn_play = QtWidgets.QPushButton(gridLayoutWidget_2, clicked = lambda: self.frameClick(anime))
        btn_play.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btn_play.setMaximumSize(QtCore.QSize(50, 180))
        btn_play.setObjectName("btn_play")
        gridAnime.addWidget(btn_play, 0, 2, 3, 1)
        btn_play.setText("PLAY")
        lbl_eps.setText("Episode : "+anime.eps)
        lbl_title.setText(anime.title)
        lblstatus.setText("Status : "+anime.status)
        return frameAnime


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Search"))

    def frameClick(self,anime):
        print(anime.title)
        self.Details = QtWidgets.QWidget()
        ui = details.Ui_Form()
        ui.setupUi(self.Details)
        self.Details.show()

    def updateList(self, animes):
        x, y = 0, 0
        for i in range(8):
            try:
                anime = animes[i]
                print(anime.title)
                animeBox = self.addAnimeBox(anime)
                self.gridAnimeList.addWidget(animeBox,x,y,1,1)
                if y == 1:
                    y = 0
                    x += 1
                else:
                    y+=1
            except:
                continue

