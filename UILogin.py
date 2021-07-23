from PyQt5.QtWidgets import QWidget, QLineEdit
from PyQt5 import QtWidgets


class UILogin(object):
    def setupUI(self, main):
        main.setGeometry(50, 50, 400, 450)
        main.setFixedSize(400, 450)
        main.setWindowTitle("Management")
        self.widget = QWidget(main)
        main.setCentralWidget(self.widget)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEchoMode(QLineEdit.Password)
        self.horizontalLayout.addWidget(self.lineEdit)
        self.btn = QtWidgets.QPushButton(self.widget)
        self.btn.setObjectName("pushButton")
        self.btn.setText("Login")
        self.horizontalLayout.addWidget(self.btn)

        self.btn.setAutoDefault(True)
        self.lineEdit.returnPressed.connect(self.btn.click)
