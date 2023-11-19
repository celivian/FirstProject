import sys
from check_is_root import *
from grahps import *
from quadratic_equation import *
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
from dialog_window import *

"""Это класс окна. Он запускает интерфейс программы"""

class Organizer(QMainWindow):
    def __init__(self):
        super().__init__()
        dlg = CustomDialog()
        if dlg.exec():
            pass
        else:
            quit()
        uic.loadUi('BaseData/uiFiles/main.ui', self)
        self.setupUi(self)

    """Метод setupUI запускает основной интерфейс программы:
    создает объекты виджета в соответствующих контейнерах и 
    присваивает им правильные имена объектов."""

    def setupUi(self, MainWindow):
        self.setFixedSize(715, 548)
        self.input = InputQE(self, Quadratic_Equation(self))
        self.pushButton_2.clicked.connect(self.checkisroot)
        self.pushButton.clicked.connect(self.input.calculation)
        self.comboBox.activated.connect(self.input.choice_equation)

    """Метод retranslateUi воссоздает весь текст"""

    """Метод checkisroot открывает новое окно с проверкой корней"""

    def checkisroot(self):
        self.check = Check_Is_Root(self)
        self.form()
        self.check.show()
        text = self.label_13.text()
        self.check.label_2.setText(text)

    """Метод form формирует уравнение в текстовом виде, понятном для человека"""

    def form(self):
        coefa = self.coefa.text()
        coefb = self.coefb.text()
        coefc = self.coefc.text()
        if not coefa:
            coefa = '1'
        if coefa == '-':
            coefa = '-1'
        try:
            testcoefa = float(coefa)
            type_of_equation = self.comboBox.currentText()
            if type_of_equation == 'ax² + bx + c = 0':
                if float(coefb) < 0:
                    type_of_equation = type_of_equation[:4] + '-' + type_of_equation[5:]
                    coefb = coefb[1:]
                if float(coefc) < 0:
                    type_of_equation = type_of_equation[:9] + '-' + type_of_equation[10:]
                    coefc = coefc[1:]
                type_of_equation = type_of_equation.replace('a', coefa)
                type_of_equation = type_of_equation.replace('b', coefb)
                type_of_equation = type_of_equation.replace('c', coefc)
            if type_of_equation == 'ax² + bx = 0':
                if float(coefb) < 0:
                    type_of_equation = type_of_equation[:4] + '-' + type_of_equation[5:]
                    coefb = coefb[1:]
                type_of_equation = type_of_equation.replace('a', coefa)
                type_of_equation = type_of_equation.replace('b', coefb)
            if type_of_equation == 'ax² + c = 0':
                if float(coefc) < 0:
                    type_of_equation = type_of_equation[:4] + '-' + type_of_equation[5:]
                    coefc = coefc[1:]
                type_of_equation = type_of_equation.replace('a', coefa)
                type_of_equation = type_of_equation.replace('c', coefc)
            if type_of_equation == 'ax² = 0':
                type_of_equation = type_of_equation.replace('a', coefa)
            self.label_13.setText(type_of_equation)
        except Exception:
            self.check.label_7.setText('Коэффициенты не введены или введены неправильно!')
            self.check.label_7.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Organizer()
    ex.show()
    sys.exit(app.exec_())
