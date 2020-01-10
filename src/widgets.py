from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys



class Popup(QWidget):
    def __init__(self):
        QWidget.__init__(self)

    def paintEvent(self, e):
        dc = QPainter(self)
        dc.drawLine(0, 0, 100, 100)
        dc.drawLine(100, 0, 0, 100)




# class TreeFileWidget(QWidget):
#     def __init__(self, *args, **kwargs):
#         QWidget.__init__(self, *args, **kwargs)
#         hlay = QHBoxLayout(self)
#         self.treeview = QTreeView()
#         self.listview = QListView()
#         hlay.addWidget(self.treeview)
#         hlay.addWidget(self.listview)

#         path = QDir.rootPath()

#         self.dirModel = QFileSystemModel()
#         self.dirModel.setRootPath(QDir.rootPath())
#         self.dirModel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs)

#         self.fileModel = QFileSystemModel()
#         self.fileModel.setFilter(QDir.NoDotAndDotDot |  QDir.Files)

#         self.treeview.setModel(self.dirModel)
#         self.listview.setModel(self.fileModel)

#         self.treeview.setRootIndex(self.dirModel.index(path))
#         self.listview.setRootIndex(self.fileModel.index(path))

#         self.treeview.clicked.connect(self.on_clicked)

#     app = QApplication(sys.argv)
#     # Splitter to show 2 views in same widget easily.
#     splitter = QSplitter()
#     # The model.
#     model = QFileSystemModel()
#     # You can setRootPath to any path.
#     model.setRootPath(QDir.rootPath())
#     # List of views.
#     views = []
#     for ViewType in (QColumnView, QTreeView):
#         # Create the view in the splitter.
#         view = ViewType(splitter)
#         # Set the model of the view.
#         view.setModel(model)
#         # Set the root index of the view as the user's home directory.
#         view.setRootIndex(model.index(QDir.homePath()))
#     # Show the splitter.
#     splitter.show()
#     # Maximize the splitter.
#     splitter.setWindowState(Qt.WindowMaximized)


#     def on_clicked(self, index):
#         path = self.dirModel.fileInfo(index).absoluteFilePath()
#         self.listview.setRootIndex(self.fileModel.setRootPath(path))



class TabWidget(QTabWidget):
    def __init__(self, parent=None):
        super(QTabWidget, self).__init__(parent)
        self.parent = parent
        # self.textEdit = QTextEdit(self.parent)
        # self.textEdit.setGeometry(QRect(180, 40, 1650, 850))
        self.translate = QCoreApplication.translate

        
    def create_tab(self, name: str = "tab", closable: bool = True):
        tab = Tab()
        tab.setObjectName(name)
        # tab.padding
        self.addTab(tab, "")
        self.setTabText(self.indexOf(tab), self.translate("MainWindow", name))


    def remove_tab(self, index):
        widget = self.widget(index)
        if widget is not None:
            widget.deleteLater()
        self.removeTab(index)


class Tab(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.parent = parent
        self.textEdit = QTextEdit(self.parent)
        self.textEdit.setGeometry(QRect(180, 40, 1650, 850))    
    
    def __str__(self):
        return self.textEdit.toPlainText()
        


class Editor(QTextEdit):

    def __init__(self, parent=None):
        super(Editor, self).__init__(parent)


    def new_(self):
        tab = QtGui.QTextEdit(self.tab)
        self.tab.addTab(tab, 'Untitled')