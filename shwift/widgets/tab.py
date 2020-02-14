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

        self._window.textEdit.textChanged.connect(self.save_current_text)

    def create_tab(self, text, filepath: str, closable: bool = True):
        tab = Tab(text=text, filepath=filepath, parent=self)
        tab.setObjectName(tab.filename)
        # tab.padding
        self.addTab(tab, "")
        self.setTabText(self.indexOf(tab), self._translate("MainWindow", tab.filename))
        self.setCurrentWidget(tab)
        return tab

    def create_untitled_tab(self):
        self._untitled_file_count += 1
        return self.create_tab("", f"Untitled-{self._untitled_file_count-1}")

    def remove_tab(self, index):
        widget = self.widget(index)
        if widget is not None:
            widget_name = widget.filename.split('-')
            if len(widget_name) == 2 and \
                    widget_name[0] == 'Untitled' and \
                    int(widget_name[1]) + 1 == self._untitled_file_count:
                self._untitled_file_count -= 1

            widget.deleteLater()
            self.removeTab(index)
            widget = None

        if self.count() == 0:
            self._window.textEdit.setPlainText('')
            self._untitled_file_count = 0

    def _on_tab_change(self, i):
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

    def save_current_text(self):
        self.text_modified = True
        widget = self.get_last_widget()
        if not widget:
            return
        content = self._window.textEdit.toPlainText()
        if content:
            widget.text = content

    def get_last_widget(self):
        widget = self.last_widget
        if not widget:
            widget = self.currentWidget()
        return widget


class Tab(QWidget):
    def __init__(self, text, filepath: str, parent=None):
        super(QWidget, self).__init__(parent)
        self._parent = parent
        self.text = text
        self._filepath = filepath
        self._filename = ""
        self.external_init()

    def external_init(self):
        if str(self._filepath).startswith("Untitled"):
            self._filename = f"Untitled-{self._parent._untitled_file_count-1}"
            return
        basename = os.path.basename(self._filepath)
        treeView = self._parent._window.treeView
        if is_file_in(filepath=basename, directory=treeView.dirname):
            self._filename = basename
        else:
            self._filename = get_relative_path(os.path.dirname(__file__), self._filepath)

    @property
    def filepath(self):
        return self._filepath

    @property
    def filename(self):
        return self._filename