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
        self.comboBox.activated.connect(self.choice_equation)

    def calculation(self):
        self.type_of_equation = self.comboBox.currentText()
        coefa = self.coefa.text()
        coefb = self.coefb.text()
        coefc = self.coefc.text()
        equation = Quadratic_Equation(self.type_of_equation, coefa, coefb, coefc)
        equation.solution()

    def choice_equation(self):
        self.type_of_equation = self.comboBox.currentText()
        if self.type_of_equation == 'ax² + bx + c = 0':
            self.label_3.show()
            self.coefb.show()
            self.label_2.show()
            self.coefc.show()
        if self.type_of_equation == 'ax² + bx = 0':
            self.label_3.show()
            self.coefb.show()
            self.label_2.hide()
            self.coefc.hide()
        if self.type_of_equation == 'ax² + c = 0':
            self.label_2.show()
            self.coefc.show()
            self.label_3.hide()
            self.coefb.hide()
        if self.type_of_equation == 'ax² = 0':
            self.label_2.hide()
            self.coefc.hide()
            self.label_3.hide()
            self.coefb.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Organizer()
    ex.show()
    sys.exit(app.exec_())
