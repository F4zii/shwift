from PyQt5.QtCore import QThread, pyqtSignal

import time

from utils import get_file_list

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