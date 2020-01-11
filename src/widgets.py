from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem

import sys
import os

from utils import DIR_ICON_PATH, FILE_ICON_PATH


class Popup(QWidget):
    def __init__(self):
        QWidget.__init__(self)





class TreeFileWidget(QTreeWidget):
    def __init__(self, parent = None):
        QTreeWidget.__init__(self, parent)
        self.clicked.connect(self.on_double_clicked)
        self.clicks = 0


    def on_double_clicked(self, index):
        if self.clicks >= 2:
            
        QtGui.QTreeWidget.mousePressEvent(self, event)




class TabWidget(QTabWidget):
    def __init__(self, parent=None):
        super(QTabWidget, self).__init__(parent)
        self.parent = parent
        # self.textEdit = QTextEdit(self.parent)
        # self.textEdit.setGeometry(QRect(180, 40, 1650, 850))
        self.translate = QCoreApplication.translate

        
    def create_tab(self,  textEdit, name: str = "tab", closable: bool = True):
        tab = Tab(textEdit=textEdit)
        tab.setObjectName(name)
        # tab.padding
        self.addTab(tab, "")
        self.setTabText(self.indexOf(tab), self.translate("MainWindow", name))


    def remove_tab(self, index):
        widget = self.widget(index)
        if widget is not None:
            widget.deleteLater()
        self.removeTab(index)


class Tab(QWidget):
    def __init__(self, textEdit, parent=None):
        super(QWidget, self).__init__(parent)
        self.parent = parent 
        self.textEdit = textEdit


class Editor(QTextEdit):

    def __init__(self, parent=None):
        super(Editor, self).__init__(parent)
        self.setGeometry(QRect(180, 40, 1650, 850)) 


