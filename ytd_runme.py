import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QFileSystemModel, QTreeView
import numpy as np
from pytube import YouTube

from frontend_ytd import Ui_MainWindow

class MainClassStart(Ui_MainWindow):
     
    def __init__(self, Form):
        print("\n --------Start Program--------")
        
        Ui_MainWindow.__init__(self)
        self.setupUi(Form)
        self.pushButton.clicked.connect(self.download_360p_mp4_videos)
        print("\n --------End Program--------") 

    def download_360p_mp4_videos(self):
        url = self.textEdit.toPlainText()
        yt = YouTube(url)
        outpath = "./"
        yt.streams.filter(file_extension="mp4").get_by_resolution("360p").download(outpath)
    
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    mainObject = MainClassStart(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

#
# End Of Program
