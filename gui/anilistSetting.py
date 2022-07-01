# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anilistSetting.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Controller

import json

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(616, 350)
        Form.setMinimumSize(QtCore.QSize(616, 350))
        Form.setMaximumSize(QtCore.QSize(616, 350))
        self.lbl_username = QtWidgets.QLabel(Form)
        self.lbl_username.setGeometry(QtCore.QRect(60, 40, 111, 17))
        self.lbl_username.setObjectName("lbl_username")
        self.txt_username = QtWidgets.QTextEdit(Form)
        self.txt_username.setGeometry(QtCore.QRect(190, 40, 141, 21))
        self.txt_username.setObjectName("txt_username")
        self.lbl_token = QtWidgets.QLabel(Form)
        self.lbl_token.setGeometry(QtCore.QRect(60, 80, 111, 17))
        self.lbl_token.setObjectName("lbl_token")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(190, 80, 351, 91))
        self.textEdit_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit_2.setObjectName("textEdit_2")
        self.lbl_autoUpdate = QtWidgets.QLabel(Form)
        self.lbl_autoUpdate.setGeometry(QtCore.QRect(60, 200, 101, 17))
        self.lbl_autoUpdate.setObjectName("lbl_autoUpdate")
        self.cAutoUpdate = QtWidgets.QCheckBox(Form)
        self.cAutoUpdate.setGeometry(QtCore.QRect(190, 200, 82, 16))
        self.cAutoUpdate.setObjectName("cAutoUpdate")
        self.btn_save = QtWidgets.QPushButton(Form,clicked=lambda: self.saveAniConfig())
        self.btn_save.setGeometry(QtCore.QRect(60, 290, 80, 30))
        self.btn_save.setObjectName("btn_save")
        self.btn_delete = QtWidgets.QPushButton(Form)
        self.btn_delete.setGeometry(QtCore.QRect(379, 290, 161, 30))
        self.btn_delete.setObjectName("btn_delete")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        try:
            with open('./anilist.json','r',encoding='utf-8') as aniConfig:
                aniSetting = json.load(aniConfig)
                token = aniSetting['token']
                username = aniSetting['username']
                autoUpdate = aniSetting['autoUpdate']
        except:
            token = """
            <!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Fira Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:19px; background-color:#282a36;\"><span style=\" font-family:\'Droid Sans Mono\',\'monospace\',\'monospace\'; font-size:14px; color:#f6f6f4; background-color:#282a36;\">get token from here : </span><a href=\"https://anilist.co/api/v2/oauth/authorize?client_id=7201&amp;response_type=token\"><span style=\" font-family:\'FantasqueSansMono Nerd Font Mono\'; text-decoration: underline; color:#646464;\">Anilist Token</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:19px; background-color:#282a36;\"><a href=\"https://anilist.co/api/v2/oauth/authorize?client_id=7201&amp;response_type=token\"><span style=\" font-family:\'FantasqueSansMono Nerd Font Mono\'; text-decoration: underline; color:#646464;\">https://anilist.co/api/v2/oauth/authorize?client_id=7201&amp;response_type=token</span></a></p></body></html>
            """
            username = ""
            autoUpdate = False
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Anilist Setting"))
        self.txt_username.setText(username)
        self.cAutoUpdate.setChecked(autoUpdate)
        self.lbl_username.setText(_translate("Form", "Anilist Username"))
        self.lbl_token.setText(_translate("Form", "Token"))
        self.textEdit_2.setHtml(_translate("Form", token))
        self.lbl_autoUpdate.setText(_translate("Form", "Auto Update"))
        self.cAutoUpdate.setText(_translate("Form", "CheckBox"))
        self.btn_save.setText(_translate("Form", "Save"))
        self.btn_delete.setText(_translate("Form", "Delete Configuration"))

    def saveAniConfig(self):
        Controller.saveAniConfig(self)


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())
