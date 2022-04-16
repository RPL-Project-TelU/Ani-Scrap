def btnSearchClick(self):
    try:
        query = self.textEdit.toPlainText()
        self.Search = QtWidgets.QWidget()
        ui = searchGui.Ui_Form()
        ui.setupUi(self.Search)
    except NameError:
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec_())
        retranslateUi(self, Dialog)
        Dialog.show()
    else:
        ui.updateList(webScrapper.querySearch(query))
        self.Search.show()
        