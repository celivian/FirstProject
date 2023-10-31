import io
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from quadratic_equation import *


class Organizer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setFixedSize(800, 600)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.calculation)

    def calculation(self):
        type_of_equation = self.comboBox.currentText()
        equation = Quadratic_Equation(type_of_equation, 1, 3, 5)
        equation.solution()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Organizer()
    ex.show()
    sys.exit(app.exec_())
