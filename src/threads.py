from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
import os

from utils import FOLDER, DIR_CLOSED_ICON_PATH, get_icon_for_extention


class PathWalkThread(QThread):
    new_item = qt.pyqtSignal(str)

    def __init__(self, tree: QTreeWidget):
        super().__init__()
        tree.moveToThread(QApplication.instance().thread())
        self.tree = tree
        self.tree.clear()
        self.base_path = self.tree.dirname

    def run(self):
        self.load_filesystem_view()


    def load_filesystem_view(self):
        """
        Load Project structure tree
        @param self.base_path
        @param tree
        @return
        """


        for element in os.listdir(self.base_path):
            path_info = self.base_path + "/" + element
            parent_itm = QTreeWidgetItem(self.tree, [os.path.basename(element)])
            parent_itm.file_path = path_info
            if os.path.isdir(path_info):
                parent_itm.setIcon(0, QIcon(DIR_CLOSED_ICON_PATH))
                parent_itm.item_type = "dir"
                parent_itm.was_expanded = False
                parent_itm.setChildIndicatorPolicy(QTreeWidgetItem.ShowIndicator)
            else:
                parent_itm.setIcon(0, QIcon(get_icon_for_extention(element.split(".")[-1])))
                parent_itm.item_type = "file"



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