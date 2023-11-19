from main import *
from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from errors import *

"""Этот класс НЕ ЗАКОНЧЕН"""

class Check_Is_Root(QWidget):
    def __init__(self, main):
        super(Check_Is_Root, self).__init__()
        uic.loadUi('BaseData/uiFiles/wincheckisroot.ui', self)
        self.main = main
        self.setupUi()

    def setupUi(self):
        self.setFixedSize(579, 435)
        text = self.main.label_13.text()
        self.pushButton.clicked.connect(self.check)
        self.label_2.setText(text)
        self.main.statusBar().hide()
        self.label_7.hide()

    def check(self):
        self.type_of_equation = self.main.comboBox.currentText()
        x1 = self.lineEdit_2.text()
        x2 = self.lineEdit.text()
        fl1 = False
        fl2 = False
        if not x1:
            x1 = '0'
            fl1 = True
        if not x2:
            x2 = '0'
            fl2 = True
        coefa = self.main.coefa.text()
        coefb = self.main.coefb.text()
        coefc = self.main.coefc.text()
        if not coefa:
            coefa = '1'
        if coefa == '-':
            coefa = '-1'
        if self.type_of_equation == 'ax² + bx = 0':
            self.equation1 = eval(f'{coefa} * ({x1}) ** 2 + {coefb} * {x1}')
            self.equation2 = eval(f'{coefa} * ({x2}) ** 2 + {coefb} * {x2}')
        if self.type_of_equation == 'ax² + c = 0':
            self.equation1 = eval(f'{coefa} * ({x1}) ** 2 + {coefc}')
            self.equation2 = eval(f'{coefa} * ({x2}) ** 2 + {coefc}')
        if self.type_of_equation == 'ax² + bx + c = 0':
            self.equation1 = eval(f'{coefa} * ({x1}) ** 2 + {coefb} * {x1} + {coefc}')
            self.equation2 = eval(f'{coefa} * ({x2}) ** 2 + {coefb} * {x2} + {coefc}')
        if self.type_of_equation == 'ax² = 0':
            self.equation1 = eval(f'{coefa} * ({x1}) ** 2')
            self.equation2 = eval(f'{coefa} * ({x2}) ** 2')
        if not fl1:
            if self.equation1 == 0:
                x1 = 'X₁ является корнем уравнения'
            else:
                x1 = 'X₁ НЕ является корнем уравнения'
        else:
            x1 = ''
        if not fl2:
            if self.equation2 == 0:
                x2 = 'X₂ является корнем уравнения'
            else:
                x2 = 'X₂ НЕ является корнем уравнения'
        else:
            x2 = ''
        self.label_6.setText(f'Ответ: {x1} {x2}')


        #else:
        #    x1 =
        #try:
        #    if float(x1) < 0:
        #        x1 = f'({x1})'
        #    if float(x2) < 0:
        #        x2 = f'({x2})'
        #except ValueError:
        #    self.label_7.setText('Введите конкретные числа!')
        #    self.label_7.show()
        #self.equation = self.label_2.text().replace('²', '**2')
        #i1 = self.equation.index('x')
        #self.equation = self.equation[:-4]
        #if self.type_of_equation == 'ax² + bx = 0':
        #    self.equation = self.equation[:-1] + '*' + self.equation[-1]
        #if self.type_of_equation == 'ax² + c = 0':
        #    self.equation = self.equation
        #if self.type_of_equation == 'ax² + bx + c = 0':
        #    sp = self.equation.split('x')
        #    self.equation = '*x'.join(sp)
        #if self.type_of_equation == 'ax² = 0':
        #    self.equation = self.equation
        #if x1 and x2:
        #    print(self.equation)
        #    evalum1 = eval(self.equation.replace('x', x1))
        #    evalum2 = eval(self.equation.replace('x', x2))
        #    if evalum1 == 0:
        #        ox1 = 'X₁ является корнем уравнения'
        #    else:
        #        ox1 = 'X₁ НЕ является корнем уравнения'
#
        #    if evalum2 == 0:
        #        ox2 = 'X₂ является корнем уравнения'
        #    else:
        #        ox2 = 'X₂ НЕ является корнем уравнения'
        #    print(evalum1)
        #    print(evalum2)
        #    self.label_7.hide()
        #    self.label_6.setText(f'{ox1}, {ox2}')
        #if x1 and not x2:
        #    evalum1 = eval(self.equation.replace('x', x1))
#
        #    if evalum1 == 0:
        #        self.label_6.setText('X₁ является корнем уравнения')
        #    else:
        #        self.label_6.setText('X₁ НЕ является корнем уравнения')
        #    self.label_7.hide()
        #if x2 and not x1:
        #    evalum2 = eval(self.equation.replace('x', x2))
        #    if evalum2 == 0:
        #        self.label_6.setText('X₂ является корнем уравнения')
        #    else:
        #        self.label_6.setText('X₂ НЕ является корнем уравнения')
        #    self.label_7.hide()
        #print(self.equation)
