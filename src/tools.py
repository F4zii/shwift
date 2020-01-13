from PyQt5.QtCore import * 
# from PyQt5.QtGui import * 
from PyQt5.QtWidgets import *

import subprocess

import os


import sys
from PyQt5 import QtCore, QtWidgets


class EmbTerminal(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(EmbTerminal, self).__init__(parent)
        self.process = QtCore.QProcess(self)

        self.terminal = QtWidgets.QWidget(self)

        layout = QtWidgets.QVBoxLayout(self)

        layout.addWidget(self.terminal)

        self.process.start('urxvt',['-embed', str(int(self.winId()))])
        self.setFixedSize(640, 480)
