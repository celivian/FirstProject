from main import *
from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from errors import *


class Check_Is_Root(QWidget):
    def __init__(self, main):
        super(Check_Is_Root, self).__init__()
        uic.loadUi('wincheckisroot.ui', self)
        self.main = main
        self.main.form()
        self.setupUi()

    def setupUi(self):
        self.label_7.hide()
        text = self.main.label_13.text()
        try:
            if text == '[Уравнение]':
                raise Input_Error()
            else:
                self.pushButton.clicked.connect(self.check)
                self.label_2.setText(text)
        except Input_Error:
            self.label_7.setText('Введены неверные данные!')
            self.label_7.show()

    def check(self):
        self.type_of_equation = self.main.comboBox.currentText()
        x1 = self.lineEdit_2.text()
        x2 = self.lineEdit.text()
        try:
            if float(x1) < 0:
                x1 = f'({x1})'
            if float(x2) < 0:
                x2 = f'({x2})'
        except ValueError:
            self.label_7.setText('Введите конкретные числа!')
            self.label_7.show()
        self.equation = self.label_2.text().replace('²', '**2')
        i1 = self.equation.index('x')
        self.equation = self.equation[:-4]
        if self.type_of_equation == 'ax² + bx = 0':
            self.equation = self.equation[:-1] + '*' + self.equation[-1]
        if self.type_of_equation == 'ax² + c = 0':
            self.equation = self.equation
        if self.type_of_equation == 'ax² + bx + c = 0':
            sp = self.equation.split('x')
            self.equation = '*x'.join(sp)
        if self.type_of_equation == 'ax² = 0':
            self.equation = self.equation
        if x1 and x2:
            print(self.equation)
            evalum1 = eval(self.equation.replace('x', x1))
            evalum2 = eval(self.equation.replace('x', x2))
            if evalum1 == 0:
                ox1 = 'X₁ является корнем уравнения'
            else:
                ox1 = 'X₁ НЕ является корнем уравнения'

            if evalum2 == 0:
                ox2 = 'X₂ является корнем уравнения'
            else:
                ox2 = 'X₂ НЕ является корнем уравнения'
            print(evalum1)
            print(evalum2)
            self.label_7.hide()
            self.label_6.setText(f'{ox1}, {ox2}')
        if x1 and not x2:
            evalum1 = eval(self.equation.replace('x', x1))

            if evalum1 == 0:
                self.label_6.setText('X₁ является корнем уравнения')
            else:
                self.label_6.setText('X₁ НЕ является корнем уравнения')
            self.label_7.hide()
        if x2 and not x1:
            evalum2 = eval(self.equation.replace('x', x2))
            if evalum2 == 0:
                self.label_6.setText('X₂ является корнем уравнения')
            else:
                self.label_6.setText('X₂ НЕ является корнем уравнения')
            self.label_7.hide()
        print(self.equation)
