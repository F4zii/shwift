from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QThread, pyqtSignal

import pathlib


class PathWalkThread(QThread):
    new_item = pyqtSignal(str)

    def __init__(self, base_path = QDir.currentPath()):
        super().__init__()
        self.base_path = base_path

    def run(self):
        for path in pathlib.Path(self.base_path).iterdir():
            self.new_item.emit(str(path))

# then later on in your code:


class TreeViewUpdateThread(QThread):

    def __init__(self, dirname):
        self._dirname = dirname
        self.tree_view_modified = pyqtSignal()
        self.file_list = get_file_list(self._dirname)

    def run(self):
        while True:
            updated_file_list = get_file_list(self._dirname)
            if file_list != updated_file_list:
                self.tree_view_modified.emit()
                self.file_list = updated_file_list
            time.sleep(1.5)