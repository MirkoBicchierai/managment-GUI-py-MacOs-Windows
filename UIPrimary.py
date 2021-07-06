from PyQt5.QtWidgets import QWidget, QHeaderView
from PyQt5 import QtWidgets, Qt, QtCore
from PyQt5.QtCore import Qt
from Dialog_add import Ui_Dialog_add
from Dialog_delete import Ui_Dialog_delete
from Dialog_delete_box import Ui_Dialog_delete_box
from Dialog_import import Ui_Dialog_import_box
from Model_Table import TableModel
from QSortFilterProxyModel_custom import QSortFilterProxyModel_custom


class UIPrimary(object):

    def setupUI(self, main_window, data):

        self.data = data
        self.main = main_window
        main_window.setGeometry(50, 50, 400, 450)
        main_window.setFixedSize(400, 450)
        main_window.setWindowTitle("Management")
        self.central_widget = QWidget(main_window)
        main_window.setCentralWidget(self.central_widget)
        self.central_widget.setObjectName("Form")
        self.central_widget.resize(1024, 640)

        self.table = QtWidgets.QTableView(self.central_widget)
        self.table.horizontal_header = self.table.horizontalHeader()
        self.table.vertical_header = self.table.verticalHeader()
        self.table.horizontal_header.setSectionResizeMode(QHeaderView.ResizeToContents)

        self.table.setGeometry(QtCore.QRect(10, 45, 1024 - 20, 640 - 70))
        self.model = TableModel(self.data, self)

        self.proxy_model = QSortFilterProxyModel_custom()
        self.proxy_model.setSourceModel(self.model)
        self.proxy_model.setFilterKeyColumn(-1)
        self.proxy_model.sort(0, Qt.AscendingOrder)
        self.table.setModel(self.proxy_model)
        self.proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.table.setColumnHidden(1, True)
        self.table.setSortingEnabled(True)

        self.table.horizontal_header.setSectionResizeMode(7, QHeaderView.Stretch)
        self.table.horizontal_header.setSectionResizeMode(3, QHeaderView.Stretch)

        self.table.clicked.connect(self.deleteI)

        self.addB = QtWidgets.QPushButton(self.central_widget)
        self.addB.setGeometry(QtCore.QRect(865 + 20, 8, 40, 30))
        self.addB.setObjectName("addB")
        self.addB.clicked.connect(self.addI)

        self.deleteB = QtWidgets.QPushButton(self.central_widget)
        self.deleteB.setGeometry(QtCore.QRect(910 + 20, 8, 40, 30))
        self.deleteB.setObjectName("deleteB")
        self.deleteB.clicked.connect(self.deleteBox)

        self.importB_range = QtWidgets.QPushButton(self.central_widget)
        self.importB_range.setGeometry(QtCore.QRect(955 + 20, 8, 40, 30))
        self.importB_range.setObjectName("importB_range")
        self.importB_range.clicked.connect(self.range_import)

        self.search_bar = QtWidgets.QLineEdit(self.central_widget)
        self.search_bar.setGeometry(QtCore.QRect(65, 12, 341, 26))
        self.search_bar.setObjectName("lineEdit")

        self.search_bar.textChanged.connect(self.proxy_model.setFilterFixedString)

        self.search = QtWidgets.QLabel(self.central_widget)
        self.search.setGeometry(QtCore.QRect(10, 12, 45, 20))
        self.search.setObjectName("searchB")
        self.search.setText("Cerca:")

        self.labelE = QtWidgets.QLabel(self.central_widget)
        self.labelE.setGeometry(QtCore.QRect(440, 15, 47, 15))
        self.labelE.setObjectName("label")

        self.importE = QtWidgets.QLabel(self.central_widget)
        self.importE.setGeometry(QtCore.QRect(480, 15, 100, 15))
        self.importE.setObjectName("label_3")

        self.labelU = QtWidgets.QLabel(self.central_widget)
        self.labelU.setGeometry(QtCore.QRect(560, 15, 47, 15))
        self.labelU.setObjectName("label_2")

        self.importU = QtWidgets.QLabel(self.central_widget)
        self.importU.setGeometry(QtCore.QRect(600, 15, 100, 15))
        self.importU.setObjectName("label_4")

        self.labelN = QtWidgets.QLabel(self.central_widget)
        self.labelN.setGeometry(QtCore.QRect(680, 15, 47, 15))
        self.labelN.setObjectName("label_5")

        self.importN = QtWidgets.QLabel(self.central_widget)
        self.importN.setGeometry(QtCore.QRect(720, 15, 100, 15))
        self.importN.setObjectName("label_6")

        _translate = QtCore.QCoreApplication.translate
        self.central_widget.setWindowTitle(_translate("Form", "Form"))
        self.addB.setText(_translate("Form", "+"))
        self.deleteB.setText(_translate("Form", "X"))

        self.labelE.setText(_translate("Form", "Entate:"))
        self.labelU.setText(_translate("Form", "Uscite:"))
        self.labelN.setText(_translate("Form", "Netto:"))

        self.labelE.setStyleSheet('color: green')
        self.importE.setStyleSheet('color: green')
        self.labelU.setStyleSheet('color: #ff4d4d')
        self.importU.setStyleSheet('color: #ff4d4d')

        self.importB_range.setText(_translate("Form", "€"))
        QtCore.QMetaObject.connectSlotsByName(self.central_widget)
        self.setLabelValue()

    def addI(self):
        ui = Ui_Dialog_add(self.main)
        ui.show()
        if ui.exec_() == QtWidgets.QDialog.Accepted:
            new_date = ui.dateEdit.text().split("/")
            self.model.insertRows(0, 1, [ui.lineEdit.text(), ui.doubleSpinBox.text(),
                                         new_date[2] + "-" + new_date[1] + "-" + new_date[0],
                                         ui.plainTextEdit.toPlainText()])
            self.model.sort(0, Qt.DescendingOrder)

    def deleteI(self, item):
        if item.column() == 8:
            dialog = QtWidgets.QDialog(self.main)
            ui = Ui_Dialog_delete()
            ui.setupUi(dialog)
            dialog.show()

            data = self.model.getDataFrame()
            k = -1
            for i in range(len(data["id"].values)):
                if str(self.table.model().data(self.table.model().index(item.row(), 1))) == str(data["id"].values[i]):
                    k = i

            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                if k != -1:
                    self.model.removeRow(k)

    def range_import(self):
        ui = Ui_Dialog_import_box(self.main, self.model.getDataFrame())
        ui.show()

    def deleteBox(self):
        ui = Ui_Dialog_delete_box(self.main)
        ui.show()
        if ui.exec_() == QtWidgets.QDialog.Accepted:
            new_date = ui.dateEdit.text().split("/")
            new_date_2 = ui.dateEdit_2.text().split("/")
            self.model.deleteBox(new_date[2] + "-" + new_date[1] + "-" + new_date[0],
                                 new_date_2[2] + "-" + new_date_2[1] + "-" + new_date_2[0])

    def setLabelValue(self):
        self.data = self.model.getDataFrame()
        positive = 0
        negative = 0
        for i in range(len(self.data["import"].values)):
            if self.data["import"].values[i] <= 0:
                negative += self.data["import"].values[i]
            else:
                positive += self.data["import"].values[i]
        self.importN.setText(str(positive-(negative*-1)) + "€")
        self.importE.setText("+" + str(positive) + "€")
        self.importU.setText("-" + str(abs(negative)) + "€")

    def save_application(self):
        self.model.getDataFrame().to_csv("data.csv", index=False, mode='w+')
