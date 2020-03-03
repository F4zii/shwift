from interface import Ui_MainWindow

from PyQt5.QtCore import QFile, QTextStream
from PyQt5 import QtWidgets

import stylesheets

import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # ['Breeze', 'Oxygen', 'QtCurve', 'Windows', 'Fusion']
    app.setStyle('Windows')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    theme_file = QFile(":/dark.qss")
    theme_file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(theme_file)
    app.setStyleSheet(stream.readAll())
    MainWindow.showMaximized()
    sys.exit(app.exec_())
