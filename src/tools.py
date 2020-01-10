import os
import sys 
from PyQt5.QtCore import * 
# from PyQt5.QtGui import * 
from PyQt5.QtWidgets import *

import subprocess


class Terminal(QWidget):
    def __init__(self, parent=None, os: str = "windows"):
        QWidget.__init__(self) 
        self.parent = parent   
        self.os = os



    def setup_command_box(self):
        self.label = QLabel(self.tr("Enter command and press Return"))
        self.le = QLineEdit()
        self.te = QTextEdit()

        # layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.le)
        layout.addWidget(self.te)
        self.setLayout(layout)

        self.connect(self.le, SIGNAL("returnPressed(void)"), self.run_command)

    def run_command(self):
        cmd = str(self.le.text())
        stdouterr = os.popen4(cmd)[1].read()
        self.te.setText(stdouterr)
