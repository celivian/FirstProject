import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from quadratic_equation import *
from input_qe import *

"""Это класс окна. Он запускает интерфейс программы"""

class Organizer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setFixedSize(800, 600)
        self.setWindowIcon(QIcon("icon.ico"))
        self.input = InputQE(self, Quadratic_Equation(self))
        self.initUI(self)
