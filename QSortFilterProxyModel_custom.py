from PyQt5.QtCore import QSortFilterProxyModel, Qt


class QSortFilterProxyModel_custom(QSortFilterProxyModel):

    def __init__(self):
        super(QSortFilterProxyModel_custom, self).__init__()

    def sort(self, column, order=Qt.AscendingOrder):
        self.sourceModel().sort(column, order)

    def filter(self):
        print("xd")