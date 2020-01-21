from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QThread, pyqtSignal

import sys
import os

import pathlib

class PathWalkThread(QThread):
    new_item = pyqtSignal(str)

    def __init__(self, base_path = QDir.currentPath()):
        super().__init__()
        self.base_path = base_path

    def run(self):
        for path in pathlib.Path(self.base_path).iterdir():
            self.new_item.emit(str(path))

# then later on in your code:





if __name__ == "__main__":
    app = QApplication(sys.argv)
    # ['Breeze', 'Oxygen', 'QtCurve', 'Windows', 'Fusion']
    app.setStyle('Breeze')
    MainWindow = QMainWindow()
    MainWindow.showMaximized()
    walk_thread = PathWalkThread()
    walk_thread.new_item.connect(lambda path: newch(path))

    def newch(path):
        print(f"new child - {path}")


    walk_thread.start()

    sys.exit(app.exec_())
