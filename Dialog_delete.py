from PyQt5 import QtCore, QtWidgets


class Ui_Dialog_delete(object):
    def setupUi(self, dialog):
        dialog.setWindowTitle("Conferma eliminazione")
        dialog.resize(300, 150)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 100, 250, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 261, 21))
        self.label.setObjectName("label")
        self.label.setText("Sei sicuro di voler eliminare la transazione?")

        self.buttonBox.accepted.connect(dialog.accept)
        self.buttonBox.rejected.connect(dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog)
