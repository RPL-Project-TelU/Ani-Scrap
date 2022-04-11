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

    animes = webScrapper.recent()
    x, y = 0, 0
    for i in range(8):
        anime = animes[i]
        animeBox = ui.addAnimeBox(MainWindow, anime.objName, anime.title, anime.status, "1", anime.thumb)
        ui.gridAnimeList.addWidget(animeBox,x,y,1,1)
        if y == 1:
            y = 0
            x += 1
        else:
            y+=1

    MainWindow.show()

    sys.exit(app.exec_())