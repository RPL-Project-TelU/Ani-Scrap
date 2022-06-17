# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI Media PlayerSMmHuL.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MediaPlayer(object):
    def setupUi(self, MediaPlayer):
        if MediaPlayer.objectName():
            MediaPlayer.setObjectName(u"MediaPlayer")
        self.centralwidget = QWidget(MediaPlayer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.MVP = QRadioButton(self.centralwidget)
        self.MVP.setObjectName(u"MVP")
        self.MVP.setGeometry(QRect(20, 20, 82, 17))
        self.VLC = QRadioButton(self.centralwidget)
        self.VLC.setObjectName(u"VLC")
        self.VLC.setGeometry(QRect(20, 50, 82, 17))
        MediaPlayer.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MediaPlayer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 295, 21))
        MediaPlayer.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MediaPlayer)
        self.statusbar.setObjectName(u"statusbar")
        MediaPlayer.setStatusBar(self.statusbar)

        self.retranslateUi(MediaPlayer)

        QMetaObject.connectSlotsByName(MediaPlayer)
    # setupUi

    def retranslateUi(self, MediaPlayer):
        MediaPlayer.setWindowTitle(QCoreApplication.translate("MediaPlayer", u"MainWindow", None))
        self.MVP.setText(QCoreApplication.translate("MediaPlayer", u"MVP", None))
        self.VLC.setText(QCoreApplication.translate("MediaPlayer", u"VLC", None))
    # retranslateUi
