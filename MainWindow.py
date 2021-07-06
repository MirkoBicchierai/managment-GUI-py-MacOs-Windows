import os
import pandas as pd
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from UILogin import UILogin
from UIPrimary import UIPrimary
from cryptography.fernet import Fernet


def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)


def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.uiWindow = UILogin()
        self.uiToolTab = UIPrimary()
        self.startLoginWindow()
        self.center()
        self.status = 0
        self.count = 0
        self.statusBar().showMessage("Login")

    def center(self):
        rectangle = self.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        rectangle.moveCenter(center)
        self.move(rectangle.topLeft())
        rectangle = self.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        rectangle.moveCenter(center)
        self.move(rectangle.topLeft())

    def startPrimaryToolTab(self):
        self.statusBar()
        self.uiToolTab.setupUI(self, (pd.read_csv("data.csv")).sort_values(by=["start_date"], ascending=[False]))
        self.show()
        self.setFixedWidth(1024)
        self.setFixedHeight(640)

    def startLoginWindow(self):
        self.uiWindow.setupUI(self)
        self.uiWindow.btn.clicked.connect(self.check_password)
        self.show()
        self.setFixedWidth(300)
        self.setFixedHeight(150)

    def check_password(self):
        if "Nexal123" == self.uiWindow.lineEdit.text():
            decrypt("data.csv", "cZP5YldvWyV8HOFDevOM0_K9l7T-90d-RyWHAvL89KY=")
            self.startPrimaryToolTab()
            self.status = 1
            self.statusBar().showMessage("data loaded")
        else:
            self.count = self.count + 1
            self.statusBar().showMessage("Login : " + str(self.count))
            if self.count == 3:
                if os.path.exists('data.csv'):
                    os.remove('data.csv')
                self.close()

    def closeEvent(self, event):
        if self.status == 1:
            self.uiToolTab.save_application()
            encrypt("data.csv", "cZP5YldvWyV8HOFDevOM0_K9l7T-90d-RyWHAvL89KY=")
        event.accept()
