from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon

import sys
import os
 
import time

from utils import DIR_OPENED_ICON_PATH, DIR_CLOSED_ICON_PATH,  FILE_ICON_PATH

class Popup(QWidget):
    def __init__(self):
        QWidget.__init__(self)





class TreeFileWidget(QTreeWidget):
    def __init__(self, windowUi ,parent = None):
        QTreeWidget.__init__(self, parent)
        self.parent = parent
        self.window_ui = windowUi
        self.itemExpanded.connect(self.on_item_expanded)
        self.itemCollapsed.connect(self.on_item_expanded)
        self.itemClicked.connect(self.on_item_clicked)
        self.clicks = 0

    def on_item_clicked(self, it, col):
        # if the folder was changed, no need to update file also 
        # since the type was "dir"

        if it.item_type == "file":
            self.window_ui.open_file(self.currentItem().file_path)

        else:
            self.toggle_folder_icon(it)


    def on_item_expanded(self, it):
        if it.item_type == "dir":
            self.toggle_folder_icon(it)
            
            

    def toggle_folder_icon(self, item):
        # loop = QEventLoop()
        # QTimer.singleShot(10, loop.quit)
        # loop.exec_()
        expanded = item.isExpanded()
        if expanded:
            item.setIcon(0, QIcon(DIR_OPENED_ICON_PATH))
        else:
            item.setIcon(0, QIcon(DIR_CLOSED_ICON_PATH))

          



class TreeFileWidgetItem(QTreeWidgetItem):
    def __init__(self, tree, text, file_path: str, type: str):
        QTreeWidgetItem.__init__(self, tree, text)
        # self.file_path = file_path
        # self.type = type


class TabWidget(QTabWidget):
    def __init__(self, parent=None):
        super(QTabWidget, self).__init__(parent)
        self.parent = parent
        # self.textEdit = QTextEdit(self.parent)
        # self.textEdit.setGeometry(QRect(180, 40, 1650, 850))
        self.translate = QCoreApplication.translate
        self.new_file_count = 0


        
    def create_tab(self,  textEdit, name: str = "tab", closable: bool = True):
        tab = Tab(textEdit=textEdit)
        tab.setObjectName(name)
        # tab.padding
        self.addTab(tab, "")
        self.setTabText(self.indexOf(tab), self.translate("MainWindow", name))

    def create_untitled_tab(self):
        self.new_file_count += 1
        return self.create_tab(Editor(), f'Untitled-{self.new_file_count-1}')

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


