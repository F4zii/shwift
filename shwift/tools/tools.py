import os
import subprocess

from PyQt5 import QtWidgets, uic

UI_FILE = os.path.join(os.path.dirname(__file__), 'gui.ui')


class Terminal(QtWidgets.QMainWindow):
    def __init__(self):
        super(Terminal, self).__init__()
        uic.loadUi(UI_FILE, self)
        self.lineEdit.returnPressed.connect(self.doCMD)
        # self.pushButtonInstall.clicked.connect(self.onClick)
        self.working_dir = "."

    def doCMD(self):
        cmd = self.lineEdit.text()
        self.lineEdit.setText("")

        if "cd " in cmd:
            vals = cmd.split(" ")
            if vals[1][0] == "/":
                self.working_dir = vals[1]
            else:
                self.working_dir = self.working_dir + "/" + vals[1]

            print(self.working_dir)
            subprocess.call(cmd, shell=True, cwd=self.working_dir)

            self.textBrowser.setText(self.textBrowser.toPlainText() + "\n$ " + cmd)
        else:
            try:
                result = subprocess.check_output(cmd, shell=True, cwd=self.working_dir)
            except Exception:
                self.textBrowser.setText(f"$ An error has occurred, `{cmd}` is a wrong or unknown command")
            else:
                self.textBrowser.setText(self.textBrowser.toPlainText() + "\n$ " + cmd + result.decode("utf-8"))

        self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())

    # def onClick(self):
    #    if len(self.lineEditName.text()) < 1:
    #        QMessageBox.critical(self, "Install", "Install")
    #    else:
    #        os.system("sudo apt-get install " + self.lineEditName.text())
