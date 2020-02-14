from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

from . import ui_widgets

import os

from shwift.utils.utils import is_file_in, get_relative_path


class TabWidget(QTabWidget):
    def __init__(self, window, parent=None):
        super(QTabWidget, self).__init__(parent)
        self._window = window
        self._parent = parent
        # self.textEdit = QTextEdit(self._parent)
        # self.textEdit.setGeometry(QRect(180, 40, 1650, 850))
        self._translate = QCoreApplication.translate
        self._untitled_file_count = 0
        self.currentChanged.connect(self._on_tab_change)
        self.tabCloseRequested.connect(self.remove_tab)
        self.last_widget = None
        self.text_modified = False
        self.setUpdatesEnabled(True)
        self._window.textEdit.textChanged.connect(self.save_current_text)

    def create_tab(self, text, filepath: str, untitled=False, closable: bool = True):
        tab = Tab(text=text, filepath=filepath, parent=self, untitled=untitled)
        tab.setObjectName(tab.visible_name)
        # tab.padding
        self.addTab(tab, "")
        self.setTabText(self.indexOf(tab), self._translate("MainWindow", tab.visible_name))
        self.setCurrentWidget(tab)
        return tab

    def create_untitled_tab(self) -> QWidget:
        self._untitled_file_count += 1
        return self.create_tab("", f"Untitled-{self._untitled_file_count - 1}", untitled=True)

    def remove_tab(self, index) -> None:
        widget = self.widget(index)
        if widget is not None:
            widget_name = widget.visible_name.split('-')
            if widget.untitled and int((widget_name[1])) + 1 == self._untitled_file_count:
                self._untitled_file_count -= 1

            widget.deleteLater()
            self.removeTab(index)
            widget = None

        if self.count() == 0:
            self._window.textEdit.setPlainText('')
            self._untitled_file_count = 0

    def _on_tab_change(self, i) -> None:
        curr_tab = self.currentWidget()
        self.save_current_text()
        self.last_widget = curr_tab
        if curr_tab is None:
            # self._window.mainLayout.removeWidget(self._window.textEdit)
            self._window.text = ""
            return

        if curr_tab is None:
            curr_tab = self.create_untitled_tab()

        if self._window.textEdit:
            self._window.textEdit.setPlainText(curr_tab.text)

    def save_current_text(self) -> None:
        self.text_modified = True
        widget = self.get_last_widget()
        if not widget:
            return
        content = self._window.textEdit.toPlainText()
        if content:
            widget.text = content

    def get_last_widget(self) -> QWidget:
        widget = self.last_widget
        if not widget:
            widget = self.currentWidget()
        return widget

    def update_tabs_by_folder(self, folder: str):
        for i in range(self.count()):
            tab = self.widget(i)
            path = os.path.join(folder, tab.filepath)
            if os.path.isfile(path):
                print(path)
                filename = os.path.basename(path)
                print(filename)
                tab.setObjectName(filename)
                tab.refresh()


# TODO display images - https://stackoverflow.com/questions/28884213/displaying-an-image-on-pyqt
class Tab(QWidget):
    def __init__(self, text, filepath: str, parent=None, untitled=False):
        super(QWidget, self).__init__(parent)
        self._parent = parent
        self.text = text
        self._filepath = filepath
        self._visible_name = ""
        self.untitled = untitled
        self.external_init()

    def external_init(self):
        if self.untitled:
            self._visible_name = f"Untitled-{self._parent._untitled_file_count - 1}"
            return
        basename = os.path.basename(self._filepath)
        treeView = self._parent._window.treeView
        if is_file_in(filepath=basename, directory=treeView.dirname):
            self._visible_name = basename
        else:
            self._visible_name = get_relative_path(os.path.dirname(__file__), self._filepath)

    @property
    def filepath(self):
        """
        The abs path of the file the tab ownes
        """
        return self._filepath

    @property
    def visible_name(self):
        """
        The file name of the file the tab ownes
        *
        """
        return self._visible_name

    @visible_name.setter
    def visible_name_setter(self, name: str):
        self._filename = name
        self.setObjectName(name)

    def refresh(self):
        self.repaint()
        self.update()
        self.show()
