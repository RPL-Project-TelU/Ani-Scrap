from PyQt5 import QtWidgets
import sys
from GUI import gui
from function import webScrapper

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
    ui.updateList(MainWindow,webScrapper.recent())
    MainWindow.show()
    sys.exit(app.exec_())