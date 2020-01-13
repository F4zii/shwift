from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon


from utils import DIR_OPENED_ICON_PATH, DIR_CLOSED_ICON_PATH, FILE_ICON_PATH



class TreeFileWidget(QTreeWidget):
    def __init__(self, windowUi ,parent = None):
        QTreeWidget.__init__(self, parent)
        self.parent = parent
        self.window_ui = windowUi
        self.itemExpanded.connect(self.on_item_expanded)
        self.itemCollapsed.connect(self.on_item_expanded)
        self.itemClicked.connect(self.on_item_clicked)
        self.itemEntered.connect(self.on_item_entered)
        self.clicks = 0

    def on_item_entered(it, col):
        print(it, col)

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
            self.window_ui.open_file(self.currentItem().file_path)

        else:
            self.toggle_folder_icon(it)


    def on_item_expanded(self, it):
        if it.item_type == "dir":
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
        QTreeWidgetItem.__init__(self, tree, text)
        # self.file_path = file_path
        # self.type = type
