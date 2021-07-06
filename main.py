from PyQt5.QtWidgets import QApplication
import sys
from MainWindow import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    sshFile = 'theme.stylesheet'
    with open(sshFile, 'r') as fh:
        w.setStyleSheet(fh.read())
    sys.exit(app.exec_())
