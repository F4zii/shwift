from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QInputDialog, QLineEdit, QFileDialog, QTreeWidgetItem
from PyQt5.QtGui import QIcon

import os
import sys



def create_label(window, name: str):
    return QtWidgets.QLabel(window).setText(name)


def label_set_text(label, text: str):
    label.setText(text)
    label.adjustSize()



def load_project_structure(startpath, tree):
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
            load_project_structure(path_info, parent_itm)
            parent_itm.setIcon(0, QIcon('assets/folder.ico'))
        else:
            parent_itm.setIcon(0, QIcon('assets/file.ico'))



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