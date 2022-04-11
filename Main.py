from PyQt5 import QtWidgets
import sys, gui, objectClass, webScrapper

def init():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    return app, ui, MainWindow
    
if __name__ == "__main__":
    # Setup
    app, ui, MainWindow = init()
    print("Loading..")
    ui.updateList(MainWindow,webScrapper.recent())
    MainWindow.show()
    sys.exit(app.exec_())