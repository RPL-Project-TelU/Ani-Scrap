def btnSearchClick(self):
    query = self.textEdit.toPlainText()
    if query == "":
        self.warnDialog = QtWidgets.QDialog()
        uiDialog = warnDialog.Ui_form()
        uiDialog.setupUI(self.warnDialog)
        self.warnDialog.show()
        return 
    self.Search = QtWidgets.QWidget()
    ui = searchGui.Ui_Form()
    ui.setupUi(self.Search)
    ui.updateList(webScrapper.querySearch(query))
    self.Search.show()
        

