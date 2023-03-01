import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon


def window():
    app = QtWidgets.QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle("First Application")
    win.setGeometry(200, 200, 600, 600)  # pyqt5 tutorial diye google da aratırız
    win.setWindowIcon(QIcon("icon.png"))
    win.setToolTip("my tooltip")

    win.show()
    sys.exit(app.exec_())


window()
