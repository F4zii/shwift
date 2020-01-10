# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtCore import QDir
from PyQt5.QtGui import *

# from pygments.lexers import get_lexer_for_filename
# from pygments import highlight
# from pygments.formatters import BBCodeFormatter



from utils import load_project_structure

from widgets import Popup, TabWidget
import sys
import os

import utils

class Ui_MainWindow(object):


    def open_file(self):
        filename = utils.openFileNameDialog()
        if not filename:
            return
        with open(str(filename), 'r') as f:
            self.textEdit.setText(f.read())
        self.tabs[filename] = QtWidgets.QWidget()
        self.tabs[filename].setObjectName(filename)

    def save_file(self):
        f = utils.saveFileDialog()
        if not f:
            self.popup = Popup()
            self.popup.setGeometry(QRect(100, 100, 400, 200))
            self.popup.show()


    

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 960)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(180, 40, 1650, 850))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.textEdit.setFont(font)
        self.tabs = TabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(180, 0, 270, 20))
        self.tabs.tabCloseRequested.connect(self.tabs.removeTab)
        self.tabs.setObjectName("Tabs")
        self.tabs.setTabsClosable(True)
        self.tabs.raise_()
        # self.tabs.tabBar().setTabButton(0, QtGui.QTabBar.RightSide,None)
        # self.tabs = dict()   # filename: Tab
        self.tab = self.tabs.create_tab("tab")
        self.tabs.addTab(self.tab, "")
        print(self.tab)
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabs.addTab(self.tab_2, "")
        self.treeView = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeView.setHeaderLabel('File System')
        self.treeView.setGeometry(QtCore.QRect(20, 40, 140, 850))
        load_project_structure(os.path.dirname(os.path.realpath(__file__)), self.treeView)
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
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Shwift"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuPreferences.setTitle(_translate("MainWindow", "Preferences"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Create a new file"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Open a file from your system"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save the current working file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save-As"))
        self.actionSave_As.setStatusTip(_translate("MainWindow", "Save the current working file as a new file in your system"))
        self.actionSave_As.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setStatusTip(_translate("MainWindow", "Undo previous actions"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setStatusTip(_translate("MainWindow", "Redo previous actions"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionFind.setText(_translate("MainWindow", "Find"))
        self.actionFind.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionReplace.setText(_translate("MainWindow", "Replace"))
        self.actionReplace.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionKeyboard_Shortcuts.setText(_translate("MainWindow", "Keyboard-Shortcuts"))
        self.actionColor_Theme.setText(_translate("MainWindow", "Color-Theme"))
        self.actionToggle_Line_Numbers.setText(_translate("MainWindow", "Toggle Line Numbers"))
        self.actionToggle_Line_Numbers.setShortcut(_translate("MainWindow", "Ctrl+L, N"))

        
        # utils.openFileNameDialog()
        # utils.openFileNamesDialog()
        # utils.saveFileDialog()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
