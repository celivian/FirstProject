import io
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from quadratic_equation import *
from input_error import *


class Organizer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setFixedSize(800, 600)
        self.qequation = Quadratic_Equation(self)
        self.changedtab()
        self.initUI()

    def initUI(self):
        self.tabWidget.currentChanged.connect(self.changedtab)


    def changedtab(self):
        self.tabindex = self.tabWidget.currentIndex()
        if self.tabindex == 0:
            self.pushButton.clicked.connect(self.qequation.calculation)
            self.comboBox.activated.connect(self.qequation.choice_equation)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Organizer()
    ex.show()
    sys.exit(app.exec_())
