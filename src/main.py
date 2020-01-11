
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QGridLayout
from PyQt5.QtCore import QDir, QFile, QTextStream, QRect
from PyQt5.QtGui import *

import sys

import qdarkstyle

# from pygments.lexers import get_lexer_for_filename
# from pygments import highlight
# from pygments.formatters import BBCodeFormatter

from utils import load_filesystem_view

from widgets import Popup, TabWidget, Editor


import sys
import os

import utils
from utils import DIR_ICON_PATH, FILE_ICON_PATH

from tools import Terminal

class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.translate = QtCore.QCoreApplication.translate

    def open_file(self):
        filename = utils.openFileNameDialog()
        if not filename:
            return
        with open(str(filename), 'r') as f:
            e = Editor()
            e.setText(self.translate("MainWindow", f.read()))
            tab = self.tabs.create_tab(e, name=os.path.basename(filename))
            self.tabs.setCurrentWidget(tab)
            

    def save_file(self):
        f = utils.saveFileDialog()
        if not f:
            return

    def on_tab_change(self, i):
        if not self.tabs.currentWidget():
            self.textEdit.setText("")
            return  
        self.textEdit.setText(self.tabs.currentWidget().textEdit.toPlainText())  

 
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setWindowIcon(QtGui.QIcon('src\assets\file.ico'))
        self.mainLayout = QGridLayout()
        self.mainLayout.setContentsMargins(0,0,0,0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(190, 40, 1650, 850))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.textEdit.setFont(font)
        self.tabs = TabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(190, 15, 280, 100))
        self.tabs.tabCloseRequested.connect(self.tabs.remove_tab)
        self.tabs.setObjectName("Tabs")
        self.tabs.setTabsClosable(True)
        self.tabs.lower()
        self.tabs.currentChanged.connect(self.on_tab_change)
        # self.tabs.tabBar().setTabButton(0, QtGui.QTabBar.RightSide,None)
        # self.tabs = dict()   # filename: Tab

        self.treeView = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeView.setHeaderLabel('File System')
        self.treeView.setGeometry(QtCore.QRect(50, 40, 140, 850))
        # self.mainLayout.addWidget(self.treeView)
        # self.mainLayout.addWidget(self.tabs)
        # self.mainLayout.addWidget(self.textEdit)
        # self.terminal = Terminal()
        # self.terminal = Terminal(self.centralwidget)
        # self.terminal.setup_command_box()
        # utils.find_or_create_item(self, os.path.dirname(os.path.abspath(__file__)), self.centralwidget)
        load_filesystem_view(os.path.dirname(os.path.realpath(__file__)), self.treeView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1900, 20))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuPreferences = QtWidgets.QMenu(self.menuFile)
        self.menuPreferences.setObjectName("menuPreferences")

        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")

        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")

        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.triggered.connect(self.save_file)

        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")

        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")

        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")

        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")

        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")

        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")

        self.actionFind = QtWidgets.QAction(MainWindow)
        self.actionFind.setObjectName("actionFind")

        self.actionReplace = QtWidgets.QAction(MainWindow)
        self.actionReplace.setObjectName("actionReplace")

        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        
        self.actionKeyboard_Shortcuts = QtWidgets.QAction(MainWindow)
        self.actionKeyboard_Shortcuts.setObjectName("actionKeyboard_Shortcuts")

        self.actionColor_Theme = QtWidgets.QAction(MainWindow)
        self.actionColor_Theme.setObjectName("actionColor_Theme")

        self.actionToggle_Line_Numbers = QtWidgets.QAction(MainWindow)
        self.actionToggle_Line_Numbers.setObjectName("actionToggle_Line_Numbers")

        self.menuPreferences.addAction(self.actionSettings)
        self.menuPreferences.addAction(self.actionKeyboard_Shortcuts)
        self.menuPreferences.addAction(self.actionColor_Theme)

        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.menuPreferences.menuAction())
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addAction(self.actionReplace)
        self.menuView.addAction(self.actionToggle_Line_Numbers)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(self.translate("MainWindow", "Shwift"))
        # self.tabs.setTabText(self.tabs.indexOf(self.tab), self.translate("MainWindow", "Tab 1"))
        # self.tabs.setTabText(self.tabs.indexOf(self.tab_2), self.translate("MainWindow", "Tab 2"))
        self.menuFile.setTitle(self.translate("MainWindow", "File"))
        self.menuPreferences.setTitle(self.translate("MainWindow", "Preferences"))
        self.menuEdit.setTitle(self.translate("MainWindow", "Edit"))
        self.menuView.setTitle(self.translate("MainWindow", "View"))
        self.actionNew.setText(self.translate("MainWindow", "New"))
        self.actionNew.setStatusTip(self.translate("MainWindow", "Create a new file"))
        self.actionNew.setShortcut(self.translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(self.translate("MainWindow", "Open"))
        self.actionOpen.setStatusTip(self.translate("MainWindow", "Open a file from your system"))
        self.actionOpen.setShortcut(self.translate("MainWindow", "Ctrl+O"))
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.setText(self.translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(self.translate("MainWindow", "Save the current working file"))
        self.actionSave.setShortcut(self.translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(self.translate("MainWindow", "Save-As"))
        self.actionSave_As.setStatusTip(self.translate("MainWindow", "Save the current working file as a new file in your system"))
        self.actionSave_As.setShortcut(self.translate("MainWindow", "Ctrl+Shift+S"))
        self.actionUndo.setText(self.translate("MainWindow", "Undo"))
        self.actionUndo.setStatusTip(self.translate("MainWindow", "Undo previous actions"))
        self.actionUndo.setShortcut(self.translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(self.translate("MainWindow", "Redo"))
        self.actionRedo.setStatusTip(self.translate("MainWindow", "Redo previous actions"))
        self.actionRedo.setShortcut(self.translate("MainWindow", "Ctrl+Y"))
        self.actionCopy.setText(self.translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(self.translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(self.translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(self.translate("MainWindow", "Ctrl+V"))
        self.actionCut.setText(self.translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(self.translate("MainWindow", "Ctrl+X"))
        self.actionFind.setText(self.translate("MainWindow", "Find"))
        self.actionFind.setShortcut(self.translate("MainWindow", "Ctrl+F"))
        self.actionReplace.setText(self.translate("MainWindow", "Replace"))
        self.actionReplace.setShortcut(self.translate("MainWindow", "Ctrl+R"))
        self.actionSettings.setText(self.translate("MainWindow", "Settings"))
        self.actionKeyboard_Shortcuts.setText(self.translate("MainWindow", "Keyboard-Shortcuts"))
        self.actionColor_Theme.setText(self.translate("MainWindow", "Color-Theme"))
        self.actionToggle_Line_Numbers.setText(self.translate("MainWindow", "Toggle Line Numbers"))
        self.actionToggle_Line_Numbers.setShortcut(self.translate("MainWindow", "Ctrl+L, N"))

        def initUI(self):      
            # formatting
            self.resize(550, 400)
            self.setWindowTitle("Toychest")

            # widgets
            self.toollist = QtGui.QTreeView()

            # QTreeView use QStandardItemModel as data source
            self.source_model = QtGui.QStandardItemModel()

            # Tabs

            # signals

            # main layout
            mainLayout = QtGui.QGridLayout()
            mainLayout.setContentsMargins(0,0,0,0)
            mainLayout.addWidget(self.toollist)
            self.setLayout(mainLayout)
            # set model for toollist
            self.toollist.setModel(self.source_model)

        def initDirectory(self, path):
            new_item = newItem(path)
            self.readDirectory(path, new_item)
            self.source_model.appendRow(new_item)

        def readDirectory(self, path, parent_item):
            directory = os.listdir(path)
            for file_name in directory:
                file_path = path + '/' + file_name
                new_item = newItem(file_path)
                parent_item.appendRow(new_item)
                if os.path.isdir(file_path):
                    self.readDirectory(file_path, new_item)

        def newItem(self, path):
            title = os.path.basename(path)
            item = QtGui.QStandardItem()
            icon_path = FILE_ICON_PATH
            if os.path.isdir(file_path):
                icon_path = DIR_ICON_PATH
            icon = QtGui.QIcon(icon_path)
            item.setText(title)
            item.setIcon(icon)
            return item
            
        # utils.openFileNameDialog()
        # utils.openFileNamesDialog()
        # utils.saveFileDialog()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    # MainWindow.setContentsMargins(10, 10, 10, 10)
    MainWindow.show()
    sys.exit(app.exec_())
