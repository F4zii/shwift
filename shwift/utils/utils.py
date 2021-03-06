from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QInputDialog,
    QLineEdit,
    QFileDialog,
    QTreeWidgetItem,
    QTreeWidget,
)
from PyQt5.QtGui import QIcon

import os

from os import walk

import pathlib

FOLDER = pathlib.Path.cwd()

ROOT_FOLDER = FOLDER.parent.joinpath("shwift")
DIR_CLOSED_ICON_PATH = f"{ROOT_FOLDER}/assets/folder_closed.ico"
DIR_OPENED_ICON_PATH = f"{ROOT_FOLDER}/assets/folder_opened.ico"
FILE_ICON_PATH = f"{ROOT_FOLDER}/assets/file.ico"


def create_label(window, name: str):
    return QtWidgets.QLabel(window).setText(name)


def label_set_text(label, text: str):
    label.setText(text)
    label.adjustSize()


ICONS = {
    "py": "python.ico",
    "js": "javascript.ico",
    "c": "c.ico",
    "cpp": "cpp.ico",
    "cs": "csharp.ico",
    "java": "java.ico",
    "css": "css.ico",
    "html": "html.ico",
    "pl": "perl.ico",
    "php": "php.ico"
}


def load_filesystem_view(startpath, tree):
    """
    Load Project structure tree
    @param startpath
    @param tree
    @return
    """

    if not startpath:
        return

    if isinstance(tree, QTreeWidget):
        tree.clear()
    curr_dir = pathlib.Path(startpath)
    for element in curr_dir.glob('**/*'):
        path_info = curr_dir.joinpath(element)
        parent_itm = QTreeWidgetItem(tree, [os.path.basename(element)])
        parent_itm.filepath = path_info
        if path_info.is_dir():
            parent_itm.setIcon(0, QIcon(DIR_CLOSED_ICON_PATH))
            parent_itm.item_type = "dir"
            parent_itm.was_expanded = False
            parent_itm.setChildIndicatorPolicy(QTreeWidgetItem.ShowIndicator)
        else:
            parent_itm.setIcon(0, QIcon(get_icon_for_extension(path_info.suffix)))
            parent_itm.item_type = "file"


def get_icon_for_extension(ext: str):
    ext = ext.replace('.', '')
    assets = f"{ROOT_FOLDER}/assets"
    if not os.path.isdir(f"{assets}/langs/{ext}"):
        return f"{assets}/file.ico"
    return f"{assets}/langs/{ext}/{ext}.ico"


def openFileNameDialog():
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(
        None,
        "Open a File",
        "",
        "All Files (*);;Python Files (*.py)",
        options=options,
    )
    return fileName


def openFileNamesDialog():
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    files, _ = QFileDialog.getOpenFileNames(
        None,
        "Open Files",
        "",
        "All Files (*);;Python Files (*.py)",
        options=options,
    )
    if files:
        print(files)


def saveFileDialog():
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getSaveFileName(
        None,
        "Save file",
        "",
        "All Files (*);;Text Files (*.txt)",
        options=options,
    )
    return fileName


def get_file_name(curr_file):
    here = pathlib.Path(__file__).parent

    return here.joinpath(str(curr_file))

def toggle_stylesheet(path):
    """
    Toggle the stylesheet to use the desired path in the Qt resource
    system (prefixed by `:/`) or generically (a path to a file on
    system).

    :path:      A full path to a resource or file on system
    """

    # get the QApplication instance,  or crash if not set
    app = QApplication.instance()
    if app is None:
        raise RuntimeError("No Qt Application found.")

    file = QFile(path)
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())


def find_tab_by_filepath(treeWidget, filepath: str):
    pass


def is_file_in(filepath: str, directory: str = "src"):
    f = []
    for (dirpath, dirnames, filenames) in walk(directory):
        f.extend(filenames)
    return filepath in f


def get_relative_path(dirname: str, filepath: str):
    return os.path.join(dirname, filepath)


def safe_file_read(filepath: str):
    try:
        with open(str(filepath), "r", encoding="utf8") as f:
            return f.read()
    except UnicodeDecodeError:
        pass


def get_file_list(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    curr_file_list = os.listdir(dirName)
    all_files = list()
    # Iterate over all the entries
    for entry in curr_file_list:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            all_files = all_files + get_file_list(fullPath)
        else:
            all_files.append(fullPath)

    return all_files
