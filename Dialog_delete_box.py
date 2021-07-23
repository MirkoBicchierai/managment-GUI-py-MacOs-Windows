from datetime import date
from PyQt5 import QtCore, QtWidgets


class Ui_Dialog_delete_box(QtWidgets.QDialog):

    def __init__(self, window):
        super(Ui_Dialog_delete_box, self).__init__(window)
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Eliminazione di massa")
        self.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(40, 40, 321, 141))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.widget)
        self.dateEdit.setDisplayFormat("d/MM/yyyy")
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDate(QtCore.QDate.fromString(date.today().strftime("%d/%m/%Y"), 'd/MM/yyyy'))
        self.gridLayout.addWidget(self.dateEdit, 1, 0, 1, 1)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.widget)
        self.dateEdit_2.setDisplayFormat("d/MM/yyyy")
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.dateEdit_2.setDate(QtCore.QDate.fromString(date.today().strftime("%d/%m/%Y"), 'd/MM/yyyy'))
        self.gridLayout.addWidget(self.dateEdit_2, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.label_3.setText("Impostare un range date di SCADENZA")
        self.label.setText("Data di inizio:")
        self.label_2.setText("Data di fine:")

    def accept(self):
        QtWidgets.QDialog.accept(self)
