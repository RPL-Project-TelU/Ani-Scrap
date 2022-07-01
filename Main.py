from PyQt5 import QtWidgets
import sys
from gui import gui, Controller
from fn import webScrapper

def init():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    return app, ui, MainWindow
    
if __name__ == "__main__":
    # Setup
    app, ui, MainWindow = init()
    print("Waiting for anoboy.online")
    Controller.updateList(ui, webScrapper.recent(),MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())