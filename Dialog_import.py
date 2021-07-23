from datetime import date
from PyQt5 import QtCore, QtWidgets


class Ui_Dialog_import_box(QtWidgets.QDialog):

    def __init__(self, window, data):
        super(Ui_Dialog_import_box, self).__init__(window)
        self._data = data
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(400, 275)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 20, 261, 21))
        self.label.setObjectName("label")
        self.label.setText("Imposta un range di date di SCADENZA")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 210, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.calculate)
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(40, 40, 321, 151))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
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
        self.gridLayout.addWidget(self.dateEdit, 1, 0, 1, 1)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.widget)
        self.dateEdit_2.setDisplayFormat("d/MM/yyyy")
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.gridLayout.addWidget(self.dateEdit_2, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 1, 1, 1)

        self.labelN = QtWidgets.QLabel(self.widget)
        self.labelN.setText("Netto")
        self.gridLayout_2.addWidget(self.labelN, 2, 0, 1, 1)
        self.importN = QtWidgets.QLabel(self.widget)
        self.importN.setText("")
        self.gridLayout_2.addWidget(self.importN, 2, 1, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.label_4.setStyleSheet("color:green")
        self.label_6.setStyleSheet("Color:#ff4d4d")
        self.dateEdit.setDate(QtCore.QDate.fromString(date.today().strftime("%d/%m/%Y"), 'd/MM/yyyy'))
        self.dateEdit_2.setDate(QtCore.QDate.fromString(date.today().strftime("%d/%m/%Y"), 'd/MM/yyyy'))
        QtCore.QMetaObject.connectSlotsByName(self)

        self.setWindowTitle("Calcola Entrate/Uscite")
        self.pushButton_2.setText("Calcola")
        self.label.setText("Data di inizio")
        self.label_2.setText("Data di fine")
        self.label_3.setText("Entrate:")
        self.label_5.setText("Uscite:")

    def calculate(self):
        positive = 0
        negative = 0
        new_date = self.dateEdit.text().split("/")
        new_date_2 = self.dateEdit_2.text().split("/")
        date_start = new_date[2] + "-" + new_date[1] + "-" + new_date[0]
        date_end = new_date_2[2] + "-" + new_date_2[1] + "-" + new_date_2[0]
        tmp = self._data.loc[self._data["finish_date"] <= date_end].loc[self._data["finish_date"] >= date_start]
        for i in range(len(tmp["import"].values)):
            if tmp["import"].values[i] <= 0:
                negative += tmp["import"].values[i]
            else:
                positive += tmp["import"].values[i]

        self.importN.setText(" " + str(positive - (negative * -1)) + "€")
        self.label_4.setText("+" + str(positive) + "€")
        self.label_6.setText("-" + str(abs(negative)) + "€")

