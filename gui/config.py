from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Controller
import sys,json

class Ui_Config(object):
    def setupUi(self, Config):
        Config.setObjectName("Config")
        Config.resize(440, 210)
        Config.setMinimumSize(QtCore.QSize(440, 210))
        Config.setMaximumSize(QtCore.QSize(440, 210))
        self.lbl_mediaplayer = QtWidgets.QLabel(Config)
        self.lbl_mediaplayer.setGeometry(QtCore.QRect(40, 40, 91, 16))
        self.lbl_mediaplayer.setObjectName("lbl_mediaplayer")
        self.combo_player = QtWidgets.QComboBox(Config)
        self.combo_player.setGeometry(QtCore.QRect(220, 40, 121, 21))
        self.combo_player.setObjectName("combo_player")
        self.combo_player.addItem("")
        self.combo_player.addItem("")
        self.lbl_discord = QtWidgets.QLabel(Config)
        self.lbl_discord.setGeometry(QtCore.QRect(40, 80, 141, 17))
        self.lbl_discord.setObjectName("lbl_discord")
        self.cbox_discord = QtWidgets.QCheckBox(Config)
        self.cbox_discord.setGeometry(QtCore.QRect(220, 80, 82, 20))
        self.cbox_discord.setChecked(True)
        self.cbox_discord.setObjectName("cbox_discord")
        self.btn_reset = QtWidgets.QPushButton(Config)
        self.btn_reset.setGeometry(QtCore.QRect(170, 160, 141, 30))
        self.btn_reset.setObjectName("btn_reset")
        self.btn_deleteHistory = QtWidgets.QPushButton(Config)
        self.btn_deleteHistory.setGeometry(QtCore.QRect(330, 160, 101, 30))
        self.btn_deleteHistory.setObjectName("btn_deleteHistory")
        self.lbl_mirror = QtWidgets.QLabel(Config)
        self.lbl_mirror.setGeometry(QtCore.QRect(40, 120, 56, 17))
        self.lbl_mirror.setObjectName("lbl_mirror")
        self.combo_mirror = QtWidgets.QComboBox(Config)
        self.combo_mirror.setGeometry(QtCore.QRect(220, 120, 121, 21))
        self.combo_mirror.setObjectName("combo_mirror")
        self.combo_mirror.addItem("")
        self.btn_save = QtWidgets.QPushButton(Config, clicked= lambda: self.saveConfig())
        self.btn_save.setGeometry(QtCore.QRect(20, 160, 131, 30))
        self.btn_save.setObjectName("btn_save")
        self.retranslateUi(Config)
        QtCore.QMetaObject.connectSlotsByName(Config)

    def retranslateUi(self, Config):
        with open('./config.json','r',encoding='utf-8') as config:
            configFile = json.load(config)
    
        _translate = QtCore.QCoreApplication.translate
        Config.setWindowTitle(_translate("Config", "Configuration"))
        self.lbl_mediaplayer.setText(_translate("Config", "Media Player"))
        self.combo_player.setItemText(0, _translate("Config", "MPV"))
        self.combo_player.setItemText(1, _translate("Config", "VLC"))
        # insert enum here
        # self.combo_player.setCurrentIndex()
        self.cbox_discord.setChecked(configFile["discordRPC"])

        self.lbl_discord.setText(_translate("Config", "Share status to Discord"))
        self.cbox_discord.setText(_translate("Config", "Yes"))
        self.btn_reset.setText(_translate("Config", "Reset Configuration"))
        self.btn_deleteHistory.setText(_translate("Config", "Delete History"))
        self.lbl_mirror.setText(_translate("Config", "Mirror"))
        self.combo_mirror.setItemText(0, _translate("Config", "uservideo"))
        self.btn_save.setText(_translate("Config", "Save"))

    def saveConfig(self):
        Controller.saveConfig(self)
        
        

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Config = QtWidgets.QWidget()
#     ui = Ui_Config()
#     ui.setupUi(Config)
#     Config.show()
#     sys.exit(app.exec_())
