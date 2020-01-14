import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class ToggleButton(QWidget):
    def __init__(self):
        super(ToggleButton, self).__init__()

        self._init_ui()

    def _init_ui(self):
        self.col = QColor(0, 0, 0)

        redb = QPushButton("Red", self)
        redb.setCheckable(True)
        redb.move(10, 10)

        redb.clicked[bool].connect(self.setColor)

        redb = QPushButton("Green", self)
        redb.setCheckable(True)
        redb.move(10, 60)

        redb.clicked[bool].connect(self.setColor)

        blueb = QPushButton("Blue", self)
        blueb.setCheckable(True)
        blueb.move(10, 100)

        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget {background-color: %s}" % self.col.name())

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle("Toggle button")
        self.show()

    def setColor(self, pressed):

        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)
