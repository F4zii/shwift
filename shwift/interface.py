import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QFileSystemWatcher
from PyQt5.QtWidgets import QVBoxLayout, QMainWindow, QFileDialog

from tools.tools import Terminal
from utils import utils
from utils.utils import load_filesystem_view
from widgets.tab import TabWidget
from widgets.tree import TreeFileWidget
from widgets.ui_widgets import Editor

import stylesheets


# from pygments.lexers import get_lexer_for_filename
# from pygments import highlight
# from pygments.formatters import BBCodeFormatter
# sys.path.insert(0, 'src\widgets')
# from .core.utils import DIR_CLOSED_ICON_PATH, DIR_OPENED_ICON_PATH, FILE_ICON_PATH

# from .core.threads import TreeViewUpdateThread


# TODO Max OOP if possible
# https://doc.qt.io/qt-5/qfilesystemwatcher.html

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.translate = QtCore.QCoreApplication.translate

    def open_file(self, filepath: str = None):
        if not filepath:
            filepath = utils.openFileNameDialog()
        if not os.path.isfile(filepath):
            return

        with open(str(filepath), "r", encoding="utf8") as f:
            content = f.read()
        if not self.textEdit:
            e = Editor(self.centralwidget)
            e.setPlainText(self.translate("MainWindow", f.read()))
            self.textEdit = e
            self.mainLayout.addWidget(self.textEdit)
        self.tabs.create_tab(content, filepath=filepath)

    def save_file_as(self):
        curr_tab = self.tabs.currentWidget()
        if not curr_tab:
            curr_tab = self.tabs.create_untitled_tab()
        f = utils.saveFileDialog()
        if not f:
            return
        with open(str(f), "w") as save_file:
            save_file.write(curr_tab.text)
        self.tabs.text_modified = False

    def open_folder(self, dirpath: str = None):
        if not dirpath:
            folder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if not os.path.isdir(folder):
            return

        load_filesystem_view(folder, self.treeView)
        self.treeView.dirname = folder
        self.tabs.update_tabs_by_folder(folder)

    # def save_file(self):
    #     curr_tab = self.tabs.currentWidget()
    #     if (not curr_tab.filename.startswith("Untitled")):
    #         file = QFile(curr_tab.filename)
    #         print(self.filename)
    #         if not file.open( QFile.WriteOnly | QFile.Text):
    #             QMessageBox.warning(self, "Error",
    #                     "Cannot write file %s:\n%s." % (curr_tab.filename, file.errorString()))
    #             return

    #         outstr = QTextStream(file)
    #         QApplication.setOverrideCursor(Qt.WaitCursor)
    #         outstr << self.textEdit.toPlainText()
    #         QApplication.restoreOverrideCursor()
    #         self.setModified(False)
    #         curr_tab.filename = QFileInfo(curr_tab.filename).fileName()
    #         self.setWindowTitle(self.fname + "[*]")
    #         self.setCurrentFile(self.filename)

    #     else:
    #         self.fileSaveAs()

    # def save_modified_file(self):
    #     if not self.tabs.text_modified:
    #         return True

    #     curr_tab = self.tabs.currentWidget()

    #     ret = QMessageBox.question(self, "Message",
    #             "<h4><p>The document was modified.</p>\n" \
    #             "<p>Do you want to save changes?</p></h4>",
    #             QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)

    #     if ret == QMessageBox.Yes:
    #         if self.filename.startswith("Untitled"):
    #             self.save_file_as()
    #             return False
    #         else:
    #             self.save_file()
    #             return True

    #     if ret == QMessageBox.Cancel:
    #         return False

    #     return True

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        MainWindow.setWindowIcon(QtGui.QIcon("src/assets/file.ico"))
        self.mainLayout = QVBoxLayout()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = Editor(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(190, 55, 1720, 850))
        self.font = QtGui.QFont()
        self.font.setPointSize(16)
        self.textEdit.setFont(self.font)
        self.tabs = TabWidget(self, self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(190, 30, 1720, 100))
        self.tabs.setObjectName("Tabs")
        self.tabs.setTabsClosable(True)
        self.tabs.lower()
        self.watcher = QFileSystemWatcher(['.'])
        # self.tabs.create_untitled_tab()
        # self.tabs.tabBar().setTabButton(0, QtGui.QTabBar.RightSide,None)
        # self.tabs = dict()   # filename: Tab
        self.terminal = Terminal()
        self.terminal.setGeometry(QtCore.QRect(190, 900, 1720, 1200))
        # self.mainLayout.addChildWidget(self.terminal)
        self.treeView = TreeFileWidget(self, self.centralwidget)
        self.treeView.setHeaderLabel("File System")
        self.treeView.setGeometry(QtCore.QRect(10, 30, 170, 875))
        load_filesystem_view(self.treeView.dirname, self.treeView)
        # self.splitter1 = QtWidgets.QSplitter(self.centralwidget)
        # self.splitter1.addWidget(self.treeView)
        # self.splitter1.addWidget(self.textEdit)
        # # self.splitter.addWidget(self.textEdit)
        # # self.splitter.setStretchFactor(1, 1)
        # self.mainLayout.addWidget(self.splitter1)
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

        self.actionGotoEnd = QtWidgets.QAction(MainWindow)
        self.actionGotoEnd.setObjectName("actionGotoEnd")

        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")

        self.actionOpenFolder = QtWidgets.QAction(MainWindow)
        self.actionOpenFolder.setObjectName("actionOpenFolder")

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.triggered.connect(self.save_file_as)

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
        self.menuFile.addAction(self.actionOpenFolder)
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
        self.menuView.addAction(self.actionGotoEnd)
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
        self.actionNew.triggered.connect(self.tabs.create_untitled_tab)
        self.actionOpen.setText(self.translate("MainWindow", "Open"))
        self.actionOpen.setStatusTip(
            self.translate("MainWindow", "Open a file from your system")
        )
        self.actionOpen.setShortcut(self.translate("MainWindow", "Ctrl+O"))
        self.actionOpen.triggered.connect(self.open_file)

        self.actionOpenFolder.setText(self.translate("MainWindow", "Open Folder"))
        self.actionOpenFolder.setStatusTip(
            self.translate("MainWindow", "Open a folder from your system")
        )
        self.actionOpenFolder.setShortcut(self.translate("MainWindow", "Ctrl+Shift+O"))
        self.actionOpenFolder.triggered.connect(self.open_folder)

        self.actionSave.setText(self.translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(
            self.translate("MainWindow", "Save the current working file")
        )
        self.actionSave.setShortcut(self.translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(self.translate("MainWindow", "Save-As"))
        self.actionSave_As.setStatusTip(
            self.translate(
                "MainWindow",
                "Save the current working file as a new file in your system",
            )
        )
        self.actionSave_As.setShortcut(self.translate("MainWindow", "Ctrl+Shift+S"))
        self.actionUndo.setText(self.translate("MainWindow", "Undo"))
        self.actionUndo.setStatusTip(
            self.translate("MainWindow", "Undo previous actions")
        )
        self.actionUndo.setShortcut(self.translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(self.translate("MainWindow", "Redo"))
        self.actionRedo.setStatusTip(
            self.translate("MainWindow", "Redo previous actions")
        )
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
        self.actionKeyboard_Shortcuts.setText(
            self.translate("MainWindow", "Keyboard-Shortcuts")
        )
        self.actionColor_Theme.setText(self.translate("MainWindow", "Color-Theme"))
        self.actionToggle_Line_Numbers.setText(
            self.translate("MainWindow", "Toggle Line Numbers")
        )
        self.actionToggle_Line_Numbers.setShortcut(
            self.translate("MainWindow", "Ctrl+L, N")
        )
        self.actionGotoEnd.setText(self.translate("MainWindow", "Goto end of file"))
        self.actionGotoEnd.setStatusTip(
            self.translate("MainWindow", "Goto the end of the current file")
        )
        self.actionGotoEnd.setShortcut(self.translate("MainWindow", "Ctrl+E"))
        self.actionGotoEnd.triggered.connect(self.textEdit.goto_buffer_end)

        def initUI(self):
            # formatting
            self.resize(550, 400)
            self.setWindowTitle("Toychest")

            # widgets
            # self.toollist = QtGui.QTreeView()

            # QTreeView use QStandardItemModel as data source
            # self.source_model = QtGui.QStandardItemModel()

            # Tabs

            # signals

            # main layout
            self.mainLayout.setContentsMargins(0, 0, 0, 0)
            self.mainLayout.addWidget(self.toollist)
            self.mainLayout.addWidget(self.tabs)
            self.mainLayout.addWidget(self.treeView)
            self.mainLayout.addWidget(self.terminal)
            # checking, maybe will change that to happen when opening
            self.mainLayout.addWidget(self.textEdit)
            # set model for toollist
            # self.toollist.setModel(self.source_model)