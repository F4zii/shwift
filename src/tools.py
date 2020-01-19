import sys
import os
import getpass
import socket
from pathlib import Path
from PyQt5.QtWidgets import QWidget, QApplication, QPlainTextEdit, QMainWindow
from PyQt5.QtGui import QFont, QTextCursor
from PyQt5.QtCore import (
    Qt,
    pyqtSignal,
    QProcess,
    QCoreApplication,
    QSettings,
    QEvent,
    QPoint,
    QSize,
)
from PyQt5 import QtCore
from PyQt5 import QtWidgets


class OpenFolderDialog(object):
    def _open_file_dialog(self):
        directory = str(QtWidgets.QFileDialog.getExistingDirectory())
        self.lineEdit.setText('{}'.format(directory))

    def _set_text(self, text):
        return text

    def setupUi(self, TestQFileDialog):
        TestQFileDialog.setObjectName("TestQFileDialog")
        TestQFileDialog.resize(240, 320)

        self.toolButtonOpenDialog = QtWidgets.QToolButton(TestQFileDialog)
        self.toolButtonOpenDialog.setGeometry(QtCore.QRect(210, 10, 25, 19))
        self.toolButtonOpenDialog.setObjectName("toolButtonOpenDialog")
        self.toolButtonOpenDialog.clicked.connect(self._open_file_dialog)

        self.lineEdit = QtWidgets.QLineEdit(TestQFileDialog)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 191, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(TestQFileDialog)
        QtCore.QMetaObject.connectSlotsByName(TestQFileDialog)

    def retranslateUi(self, TestQFileDialog):
        _translate = QtCore.QCoreApplication.translate
        TestQFileDialog.setWindowTitle(_translate("TestQFileDialog", "Dialog"))
        self.toolButtonOpenDialog.setText(_translate("TestQFileDialog", "..."))


class Terminal(QPlainTextEdit):
    commandSignal = pyqtSignal(str)
    commandZPressed = pyqtSignal(str)

    def __init__(self, parent=None, movable=False):
        super(Terminal, self).__init__()

        self.installEventFilter(self)
        self.setAcceptDrops(True)
        QApplication.setCursorFlashTime(1000)
        self.process = QProcess()
        self.process.readyReadStandardError.connect(self.onReadyReadStandardError)
        self.process.readyReadStandardOutput.connect(self.onReadyReadStandardOutput)

        self.name = (
            str(getpass.getuser())
            + "@"
            + str(socket.gethostname())
            + ":"
            + str(os.getcwd())
            + "$ "
        )
        self.appendPlainText(self.name)
        self.commands = (
            []
        )  # This is a list to track what commands the user has used so we could display them when
        # up arrow key is pressed
        self.tracker = 0
        self.setStyleSheet(
            "QPlainTextEdit{background-color: #212121; color: #f3f3f3; padding: 8;}"
        )
        self.verticalScrollBar().setStyleSheet("background-color: #212121;")
        self.text = None
        self.setFont(QFont("Noto Sans Mono", 8))
        self.previousCommandLength = 0

    def eventFilter(self, source, event):
        if event.type() == QEvent.DragEnter:
            event.accept()
            print("DragEnter")
            return True
        elif event.type() == QEvent.Drop:
            print("Drop")
            self.setDropEvent(event)
            return True
        else:
            return False  ### super(QPlainTextEdit).eventFilter(event)

    def setDropEvent(self, event):
        if event.mimeData().hasUrls():
            f = str(event.mimeData().urls()[0].toLocalFile())
            self.insertPlainText(f)
            event.accept()
        elif event.mimeData().hasText():
            ft = event.mimeData().text()
            print("text:", ft)
            self.insertPlainText(ft)
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):
        cursor = self.textCursor()

        if e.modifiers() == Qt.ControlModifier and e.key() == Qt.Key_A:
            return

        if e.modifiers() == Qt.ControlModifier and e.key() == Qt.Key_Z:
            self.commandZPressed.emit("True")
            return

        if e.modifiers() == Qt.ControlModifier and e.key() == Qt.Key_C:
            self.process.kill()
            self.name = (
                str(getpass.getuser())
                + "@"
                + str(socket.gethostname())
                + ":"
                + str(os.getcwd())
                + "$ "
            )
            self.appendPlainText("process cancelled")
            self.appendPlainText(self.name)
            self.textCursor().movePosition(QTextCursor.End)
            return

        if e.key() == Qt.Key_Return:  ### 16777220:  # This is the ENTER key
            text = self.textCursor().block().text()

            if (
                text == self.name + text.replace(self.name, "")
                and text.replace(self.name, "") != ""
            ):  # This is to prevent adding in commands that were not meant to be added in
                self.commands.append(text.replace(self.name, ""))
            #                print(self.commands)
            self.handle(text)
            self.commandSignal.emit(text)
            self.appendPlainText(self.name)

            return

        if e.key() == Qt.Key_Up:
            try:
                if self.tracker != 0:
                    cursor.select(QTextCursor.BlockUnderCursor)
                    cursor.removeSelectedText()
                    self.appendPlainText(self.name)

                self.insertPlainText(self.commands[self.tracker])
                self.tracker -= 1

            except IndexError:
                self.tracker = 0

            return

        if e.key() == Qt.Key_Down:
            try:
                cursor.select(QTextCursor.BlockUnderCursor)
                cursor.removeSelectedText()
                self.appendPlainText(self.name)

                self.insertPlainText(self.commands[self.tracker])
                self.tracker += 1

            except IndexError:
                self.tracker = 0

        if e.key() == Qt.Key_Backspace:  ### 16777219:
            if cursor.positionInBlock() <= len(self.name):
                return

            else:
                cursor.deleteChar()

        super().keyPressEvent(e)
        cursor = self.textCursor()
        e.accept()

    def ispressed(self):
        return self.pressed

    def onReadyReadStandardError(self):
        self.error = self.process.readAllStandardError().data().decode()
        self.appendPlainText(self.error.strip("\n"))

    def onReadyReadStandardOutput(self):
        self.result = self.process.readAllStandardOutput().data().decode()
        self.appendPlainText(self.result.strip("\n"))
        self.state = self.process.state()

    #        print(self.result)

    def run(self, command):
        """Executes a system command."""
        if self.process.state() != 2:
            self.process.start(command)
            self.process.waitForFinished()
            self.textCursor().movePosition(QTextCursor.End)

    def handle(self, command):
        #        print("begin handle")
        """Split a command into list so command echo hi would appear as ['echo', 'hi']"""
        real_command = command.replace(self.name, "")

        if command == "True":
            if self.process.state() == 2:
                self.process.kill()
                self.appendPlainText("Program execution killed, press enter")

        if real_command.startswith("python"):
            pass

        if real_command != "":
            command_list = real_command.split()
        else:
            command_list = None
        """Now we start implementing some commands"""
        if real_command == "clear":
            self.clear()

        elif command_list is not None and command_list[0] == "echo":
            self.appendPlainText(" ".join(command_list[1:]))

        elif real_command == "exit":
            quit()

        elif (
            command_list is not None
            and command_list[0] == "cd"
            and len(command_list) > 1
        ):
            try:
                os.chdir(" ".join(command_list[1:]))
                self.name = (
                    str(getpass.getuser())
                    + "@"
                    + str(socket.gethostname())
                    + ":"
                    + str(os.getcwd())
                    + "$ "
                )
                self.textCursor().movePosition(QTextCursor.End)

            except FileNotFoundError as E:
                self.appendPlainText(str(E))

        elif (
            command_list is not None
            and len(command_list) == 1
            and command_list[0] == "cd"
        ):
            os.chdir(str(Path.home()))
            self.name = (
                str(getpass.getuser())
                + "@"
                + str(socket.gethostname())
                + ":"
                + str(os.getcwd())
                + "$ "
            )
            self.textCursor().movePosition(QTextCursor.End)

        elif self.process.state() == 2:
            self.process.write(real_command.encode())
            self.process.closeWriteChannel()

        elif command == self.name + real_command:
            self.run(real_command)
        else:
            pass
