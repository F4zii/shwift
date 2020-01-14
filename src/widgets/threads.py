from PyQt5.QtCore import QThread, pyqtSignal

import time


class TreeViewUpdateThread(QThread):

    tree_view_modified = pyqtSignal()

    def _run_thread(self):
        while True:
            self.tree_view_modified.emit()
            time.sleep(3)