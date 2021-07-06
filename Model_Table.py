import numpy
from PyQt5.QtCore import (Qt, QAbstractTableModel, QVariant, QModelIndex)
from PyQt5 import QtCore
from PyQt5.QtGui import QColor
from datetime import date


class TableModel(QAbstractTableModel):

    def __init__(self, data, window):
        super(TableModel, self).__init__()
        self._data = data
        self.checked = data["checked"].values
        self.column_count = 9
        self.row_count = len(self._data["id"].values)
        self.window = window

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return ("Data", "id", "Data Scadenza", "Attività", "Prezzo", "", "Data Pagamento", "Descrizione"
                    , "")[
                section]
        else:
            return "{}".format(section)

    def rowCount(self, QModelIndex):
        return self.row_count

    def columnCount(self, QModelIndex):
        return self.column_count

    def data(self, index, role):
        row = index.row()
        col = index.column()

        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter

        if role == Qt.BackgroundRole:
            if col == 8:
                return QColor(255, 71, 26)
        if role == Qt.DisplayRole or role == Qt.EditRole:
            if col == 0:
                return QtCore.QDate.fromString(self._data["start_date"].values[row], 'yyyy-M-d')
            if col == 1:
                return "{}".format(self._data["id"].values[row])
            if col == 2:
                return QtCore.QDate.fromString(self._data["finish_date"].values[row], 'yyyy-M-d')
            if col == 3:
                return self._data["Name"].values[row]

            if col == 5:
                return

            if col == 6:
                if self._data["checked_date"].values[row] != "-":
                    return QtCore.QDate.fromString(self._data["checked_date"].values[row], 'd/M/yyyy')
                else:
                    return QtCore.QDate.fromString("", 'd/M/yyyy')

            if col == 4:
                return int(format(self._data["import"].values[row]))

            if col == 7:
                return self._data["Description"].values[row]
            if col == 8:
                return "X"

        elif role == Qt.CheckStateRole:
            if col == 5:
                return Qt.Checked if self._data["checked"].values[row] == 2 else Qt.Unchecked
        elif role == Qt.ToolTipRole:
            if col == 5:
                return self.checked[row]
        return QVariant()

    def setData(self, index, value, role):
        check = None
        row = index.row()
        col = index.column()

        if role == Qt.CheckStateRole and col == 5:
            if value == Qt.Checked:
                check = 2
                self.checked[row] = 2
            else:
                check = 0
                self.checked[row] = 0

        if check is not None:
            for i in range(len(self._data["id"].values)):
                if str(self._data["id"].values[i]) == str(self.data(self.index(row, 1), Qt.DisplayRole)):
                    self._data["checked"].values[i] = check
                    if check == 2:
                        self.setData(self.index(row, 6), -1, Qt.EditRole)
                    else:
                        self.setData(self.index(row, 6), -2, Qt.EditRole)
            self.dataChanged.emit(self.index(row,col+1), index, [Qt.EditRole])

        if role == Qt.EditRole:
            row = index.row()
            column = index.column()
            if row > len(self._data["id"].values) or column > self.column_count:
                return False
            else:
                if column == 3:
                    for j in range(len(self._data["id"].values)):
                        if str(self._data["id"].values[j]) == str(self.data(self.index(row, 1), Qt.DisplayRole)):
                            if value != "":
                                self._data["Name"].values[j] = value
                if column == 4:
                    for j in range(len(self._data["id"].values)):
                        if str(self._data["id"].values[j]) == str(self.data(self.index(row, 1), Qt.DisplayRole)):
                            if value != "":
                                self._data["import"].values[j] = int(value)
                    self.window.setLabelValue()

                if column == 6:
                    for j in range(len(self._data["id"].values)):
                        if str(self._data["id"].values[j]) == str(self.data(self.index(row, 1), Qt.DisplayRole)):
                            if value != "" and value != -1 and value != -2:
                                self._data["checked_date"].values[j] = value.toString('d/M/yyyy')
                            else:
                                if value == - 1:
                                    self._data["checked_date"].values[j] = date.today().strftime("%d/%m/%Y")
                                if value == - 2:
                                    self._data["checked_date"].values[j] = "-"

                if column == 2:
                    for j in range(len(self._data["id"].values)):
                        if str(self._data["id"].values[j]) == str(self.data(self.index(row, 1), Qt.DisplayRole)):
                            if value != "":
                                self._data["finish_date"].values[j] = value.toString('yyyy-M-d')

                if column == 7:
                    for j in range(len(self._data["id"].values)):
                        if str(self._data["id"].values[j]) == str(self.data(self.index(row, 1), Qt.DisplayRole)):
                            if value != "":
                                self._data["Description"].values[j] = value
                return True

        return True

    def sort(self, column, order=Qt.AscendingOrder):
        self._data.reset_index(inplace=True, drop=True)
        self.layoutAboutToBeChanged.emit()
        if column == 0:
            self._data.sort_values('start_date', ascending=order == Qt.AscendingOrder, inplace=True)
            self._data.reset_index(inplace=True, drop=True)  # <-- this is the change
        if column == 1:
            self._data.sort_values('id', ascending=order == Qt.AscendingOrder, inplace=True)
            self._data.reset_index(inplace=True, drop=True)  # <-- this is the change
        if column == 2:
            self._data.sort_values('Name', ascending=order == Qt.AscendingOrder, inplace=True)
            self._data.reset_index(inplace=True, drop=True)  # <-- this is the change
        if column == 3:
            self._data.sort_values('import', ascending=order == Qt.AscendingOrder, inplace=True)
            self._data.reset_index(inplace=True, drop=True)  # <-- this is the change
        if column == 4:
            self._data.sort_values('checked_date', ascending=order == Qt.AscendingOrder, inplace=True)
            self._data.reset_index(inplace=True, drop=True)  # <-- this is the change
        if column == 5:
            self._data.sort_values('checked_date', ascending=order == Qt.AscendingOrder, inplace=True)
            self._data.reset_index(inplace=True, drop=True)  # <-- this is the change
        if column == 6:
            self._data.sort_values('finish_date', ascending=order == Qt.AscendingOrder, inplace=True)
            self._data.reset_index(inplace=True, drop=True)  # <-- this is the change
        if column == 7:
            self._data.sort_values('Description', ascending=order == Qt.AscendingOrder, inplace=True)
            self._data.reset_index(inplace=True, drop=True)  # <-- this is the change
        self.layoutChanged.emit()

    def flags(self, index):
        if index.column() == 5:
            return Qt.ItemIsEnabled | Qt.ItemIsUserCheckable
        if index.column() == 2:
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable
        if index.column() == 3:
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable
        if index.column() == 4:
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable
        if index.column() == 6:
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable
        if index.column() == 7:
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable
        if index.column() == 8:
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable
        else:
            return Qt.ItemFlags(QAbstractTableModel.flags(self, index) | Qt.ItemIsEnabled | Qt.ItemIsSelectable)

    def getDataFrame(self):
        return self._data

    def setDataFrame(self, data):
        self._data = data

    def removeRows(self, position, rows=1, index=QModelIndex(), reset=True):
        self.beginRemoveRows(QModelIndex(), position, position + rows - 1)
        self._data.drop(position, inplace=True)
        if reset:
            self._data.reset_index(inplace=True, drop=True)
        self.endRemoveRows()
        self.row_count = self.row_count - 1
        self.window.setLabelValue()
        return True

    def deleteBox(self, date_start, date_end):
        for i in self._data.loc[self._data["finish_date"] <= date_end].loc[
            self._data["finish_date"] >= date_start].index:
            self.removeRows(i, reset=False)
        self._data.reset_index(inplace=True, drop=True)
        self.sort(0)  # HOT FIX
        self.window.setLabelValue()
        return

    def insertRows(self, position, rows=1, text=None, index=QModelIndex()):
        self.beginInsertRows(QModelIndex(), 0, 0)
        new_row = {'start_date': date.today().strftime("%Y-%m-%d"), 'id': numpy.max(self._data["id"].values) + 1,
                   'Name': text[0], 'import': float(text[1].replace(",", ".")), 'Description': text[3],
                   'checked': int(0),
                   'checked_date': '-', 'finish_date': text[2]}
        self._data = self._data.append(new_row, ignore_index=True)
        self.row_count = self.row_count + 1
        self.endInsertRows()
        self.window.setLabelValue()
        return True
