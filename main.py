from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic
import sys
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Coffee")

        data = sqlite3.connect("coffee.sqlite")
        cur = data.cursor()


        data.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
