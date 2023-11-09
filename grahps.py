import sys
from PyQt5.QtWidgets import QApplication, QWidget
from main import *
from PyQt5 import uic



class Graph(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('grahps.ui', self)
        self.setupUi()

    def setupUi(self):
        self.pushButton.clicked.connect(self.run)

    def run(self):
        if self.radioButton.isChecked():
            self.widget.clear()
            self.widget.plot([i for i in range(10)], [i for i in range(10)], pen='r')
        elif self.radioButton_2.isChecked():
            self.widget.clear()
            self.widget.plot([i for i in range(10)], [i ** 2 for i in range(10)], pen='g')
        elif self.radioButton_3.isChecked():
            self.widget.clear()
            self.widget.plot([i for i in range(10)], [i ** 3 for i in range(10)], pen='b')
