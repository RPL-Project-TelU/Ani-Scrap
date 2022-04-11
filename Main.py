from PyQt5 import QtWidgets
import sys, gui

if __name__ == "__main__":
    # Setup
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    anime = ui.addAnimeBox(MainWindow, "anime1", "Spy x Familiy", "Ongoing", str(1), "resource/121382.th.jpg")
    anime2 = ui.addAnimeBox(MainWindow, "anime2", "Spy x Familiy", "Ongoing", str(1), "resource/121382.th.jpg")
    ui.gridAnimeList.addWidget(anime, 0, 0, 1, 1)
    ui.gridAnimeList.addWidget(anime2, 0, 1, 1, 1)
    MainWindow.show()
    sys.exit(app.exec_())