from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *



class Popup(QWidget):
    def __init__(self, title: str, text: str, icon):
        QWidget.__init__(self)
        self.title = title
        self.text = text
        self.icon = icon

    def show_popup(self):
        self.msg = QMessageBox()

        self.msg.setWindowTitle(self.title)

        self.msg.setText(self.text)

        self.msg.setIcon(self.icon)

        e = msg.exec_()


class Editor(QTextEdit):
    def __init__(self, parent=None):
        QTextEdit.__init__(self, parent)
        self.setGeometry(QRect(180, 40, 1650, 850)) 


    def clear_text():
        self.textEdit.setText('')