from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

from . import ui_widgets

import os

from utils import is_file_in, get_relative_path

Editor = ui_widgets.Editor

class TabWidget(QTabWidget):
    def __init__(self, window, parent=None):
        super(QTabWidget, self).__init__(parent)
        self.window = window
        self.parent = parent
        # self.textEdit = QTextEdit(self.parent)
        # self.textEdit.setGeometry(QRect(180, 40, 1650, 850))
        self.translate = QCoreApplication.translate
        self.new_file_count = 0
        self.currentChanged.connect(self.on_tab_change)
        self.tabCloseRequested.connect(self.remove_tab)


        
    def create_tab(self,  textEdit, filepath: str, closable: bool = True):
        tab = Tab(textEdit=textEdit, filepath=filepath, parent=self)
        tab.setObjectName(filepath)
        # tab.padding
        self.addTab(tab, "")
        self.setTabText(self.indexOf(tab), self.translate("MainWindow", tab.file_name))


    def create_untitled_tab(self):
        self.new_file_count += 1
        return self.create_tab(Editor(), f'Untitled-{self.new_file_count-1}')


    def remove_tab(self, index):
        widget = self.widget(index)
        if widget is not None:
            widget.deleteLater()
        self.removeTab(index)
        widget.textEdit.deleteLater()
        widget.textEdit = None
        widget = None


    def on_tab_change(self, i):
        curr_tab = self.currentWidget()
        if not curr_tab:
            self.window.mainLayout.removeWidget(self.window.textEdit)  
            self.window.textEdit.deleteLater()
            self.window.textEdit = None
            return

        if not hasattr(curr_tab, "textEdit"):
            curr_tab = self.create_untitled_tab()  
        self.window.textEdit.setText(curr_tab.textEdit.toPlainText())  


class Tab(QWidget):
    def __init__(self, textEdit, filepath: str, parent=None):
        super(QWidget, self).__init__(parent)
        self.parent = parent 
        self.textEdit = textEdit
        self.filepath = filepath
        self.file_name = ""
        self.external_init()

    def external_init(self):
        if self.filepath.startswith('Untitled'):
            self.file_name = f'Untitled-{self.parent.new_file_count-1}'
            return
        basename = os.path.basename(self.filepath)
        print(basename)
        if is_file_in(filepath=basename):
            print("In!" + basename)
            self.file_name = basename
        else:
            self.file_name = get_relative_path(os.path.dirname(__file__), self.filepath)
