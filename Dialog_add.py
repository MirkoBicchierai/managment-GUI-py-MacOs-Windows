from datetime import date
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIntValidator


class Ui_Dialog_add(QtWidgets.QDialog):

    def __init__(self, window):
        super(Ui_Dialog_add, self).__init__(window)
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Aggiungi muovimento")
        self.resize(410, 367)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(30, 320, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(40, 20, 321, 101))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.doubleSpinBox = QtWidgets.QLineEdit(self.widget)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 1, 1, 1, 1)

        self.onlyInt = QIntValidator()
        self.doubleSpinBox.setValidator(self.onlyInt)

        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Importo*")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.label_3.setText("Nome*")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.label.setText("Data di scadenza*")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.widget)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDate(QtCore.QDate.fromString(date.today().strftime("%d/%m/%Y"), 'd/M/yyyy'))
        self.gridLayout.addWidget(self.dateEdit, 2, 1, 1, 1)

        self.widget1 = QtWidgets.QWidget(self)
        self.widget1.setGeometry(QtCore.QRect(40, 130, 321, 161))
        self.widget1.setObjectName("widget1")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setObjectName("label_4")
        self.label_4.setText("Descrizione:")
        self.verticalLayout.addWidget(self.label_4)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget1)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def accept(self):
        if self.lineEdit.text() == "" or self.lineEdit.text() == " ":
            return
        QtWidgets.QDialog.accept(self)
