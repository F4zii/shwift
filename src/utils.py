from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QInputDialog, QLineEdit, QFileDialog, QTreeWidgetItem
from PyQt5.QtGui import QIcon

import os
import sys

DIR_ICON_PATH = r'C:\Users\iddos.DESKTOP-JTOR36M\Documents\GitHub\Shwift-Text-Editor\src\assets\folder.ico'
FILE_ICON_PATH = r'C:\Users\iddos.DESKTOP-JTOR36M\Documents\GitHub\Shwift-Text-Editor\src\assets\file.ico'

def create_label(window, name: str):
    return QtWidgets.QLabel(window).setText(name)


def label_set_text(label, text: str):
    label.setText(text)
    label.adjustSize()




def load_filesystem_view(startpath, tree):
    """
    Load Project structure tree
    @param startpath
    @param tree
    @return
    """
    for element in os.listdir(startpath):
        path_info = startpath + "/" + element
        parent_itm = QTreeWidgetItem(tree, [os.path.basename(element)])
        if os.path.isdir(path_info):
            load_filesystem_view(path_info, parent_itm)
            parent_itm.setIcon(0, QIcon(DIR_ICON_PATH))
            # parent_itm.setExpanded( True ) if we want to show the whole tree expanded

        else:
            parent_itm.setIcon(0, QIcon(FILE_ICON_PATH))
            # parent_itm.setExpanded( True ) if we want to show the whole tree expanded



def openFileNameDialog():
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
    return fileName




def openFileNamesDialog():
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    files, _ = QFileDialog.getOpenFileNames(None, "QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
    if files:
        print(files)

def saveFileDialog():
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getSaveFileName(None, "QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
    return fileName



def get_file_name(curr_file):
    here = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(here, str(curr_file))

    
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