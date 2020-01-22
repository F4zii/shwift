from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon


from threads import PathWalkThread

from utils import DIR_CLOSED_ICON_PATH, DIR_OPENED_ICON_PATH, load_filesystem_view


class TreeFileWidget(QTreeWidget):
    def __init__(self, windowUi, parent=None):
        QTreeWidget.__init__(self, parent)
        self._parent = parent
        self._window = windowUi
        self._dirname = ''
        self.itemExpanded.connect(self.on_item_expanded)
        self.itemCollapsed.connect(self.on_item_expanded)
        self.itemClicked.connect(self.on_item_clicked)
        self.itemEntered.connect(self.on_item_entered)
        self.path_walk_thread = PathWalkThread(self)

    @property
    def parent(self):
        return self._parent

    @property
    def window(self):
        return self._window

    @property
    def dirname(self):
        return self._dirname


    @dirname.setter
    def dirname(self, name):
        self._dirname = name

    @property
    def window(self):
        return self._window

    def on_item_entered(it, col):
        pass

    def on_item_clicked(self, it, col):
        """
        An event handler being called by QTreeWidget.itemClicked

        function uses:
            Toggling folder icons
            Opening Files on click (From tree view)

        @param it - The TreeWidgetItem that was clicked
        @param col - The column of the TreeWidgetItem that was clicked
        """

        if it.item_type == "file":
            tabs = self._window.tabs
            for i in range(tabs.count()):
                item = tabs.widget(i)
                if item.filepath == it.file_path:
                    return tabs.setCurrentWidget(item)
            self._window.open_file(self.currentItem().file_path)

        if it.item_type == "dir":
            if not it.was_expanded:
                load_filesystem_view(it.file_path, it)
                it.was_expanded = True
            it.setExpanded(not it.isExpanded())
            # self.toggle_folder_icon(it)

            
    def on_item_expanded(self, it):
        if it.item_type == "dir":
            if not it.was_expanded:
                load_filesystem_view(it.file_path, it)
                it.was_expanded = True
            self.toggle_folder_icon(it)

    def toggle_folder_icon(self, item):
        # loop = QEventLoop()
        # QTimer.singleShot(10, loop.quit)
        # loop.exec_()
        expanded = item.isExpanded()
        if expanded:
            item.setIcon(0, QIcon(DIR_OPENED_ICON_PATH))

        else:
            item.setIcon(0, QIcon(DIR_CLOSED_ICON_PATH))




class TreeFileWidgetItem(QTreeWidgetItem):
    def __init__(self, tree, text, file_path: str, type: str):
        super().__init__()
        self.path = file_path
        # self.file_path = file_path
        # self.type = type
