import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from quadratic_equation import *
from input_qe import *
from check_is_root import *
from grahps import *

"""Это класс окна. Он запускает интерфейс программы"""


class Organizer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowIcon(QIcon("icon.ico"))
        self.setFixedSize(800, 600)
        self.input = InputQE(self, Quadratic_Equation(self))
        self.setupUi()

    """Метод initUI запускает основной интерфейс программы:
    создает объекты виджета в соответствующих контейнерах и 
    присваивает им правильные имена объектов."""

    def setupUi(self):
        self.pushButton_2.clicked.connect(self.window2)
        self.pushButton.clicked.connect(self.input.calculation)
        self.comboBox.activated.connect(self.input.choice_equation)

    def window2(self):
        self.win = Check_Is_Root(self)
        self.win.show()

    def form(self):
        fl1 = False
        fl2 = False
        coefa = self.coefa.text()
        coefb = self.coefb.text()
        coefc = self.coefc.text()
        type_of_equation = self.comboBox.currentText()
        try:
            if (coefb and coefc and type_of_equation == "ax² + bx + c = 0") or (
                    coefb and type_of_equation == 'ax² + bx = 0') or (
                    coefc and type_of_equation == 'ax² + c = 0') or type_of_equation == "ax² = 0":
                if not coefa:
                    coefa = '1'
                if not coefb:
                    coefb = '1'
                    fl1 = True
                if not coefc:
                    coefc = '1'
                    fl2 = True
                coefficients = [coefa, coefb, coefc]
                if coefficients[0][0] == '0' or '-0' in coefficients[0] or '+0' in coefficients[0] or \
                        coefficients[1][0] == '0' or '-0' in coefficients[1] or '+0' in coefficients[1] \
                        or coefficients[2][0] == '0' or '-0' in coefficients[2] or \
                        '+0' in coefficients[2]:
                    raise ValueError
                else:
                    if fl1:
                        coefb = ''
                        fl1 = False
                    if fl2:
                        coefc = ''
                        fl2 = False
                    formed = type_of_equation.replace('a', coefa)
                    test = float(coefa)
                    if coefb:
                        if float(coefb) < 0:
                            i = formed.index('+')
                            formed = formed[:i] + '-' + formed[i + 1:]
                            coefb = coefb[1:]
                        formed = formed.replace('b', coefb)
                    if coefc:
                        if float(coefc) < 0:
                            i = formed.index('+')
                            i2 = formed.index('+', i, len(formed))
                            formed = formed[:i2] + '-' + formed[i2 + 1:]
                            coefc = coefc[1:]
                        formed = formed.replace('c', coefc)
                    self.label_13.setText(formed)
            else:
                self.label_13.setText('[Уравнение]')
        except ValueError:
            self.label_13.setText('[Уравнение]')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Organizer()
    ex.show()
    sys.exit(app.exec_())
