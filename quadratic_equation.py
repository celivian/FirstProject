from input_qe import *
import math as m
from errors import *

"""Этот класс решает уравнения, исходя из полученных данных"""

class Quadratic_Equation():
    def __init__(self, main):
        self.main = main
        self.inputqe = InputQE(self.main, self)
        self.inputqe.choice_equation()

    """Метод solution определяет для какого уравнения нужно предоставить решение"""

    def solution(self, coefs, toe):
        self.coefficients = coefs
        self.type_of_equation = toe
        if not self.coefficients[0]:
            self.coefficients[0] = '1'
        if self.coefficients[0] == '-':
            self.coefficients[0] = '-1'
        try:
            if self.coefficients[0] == '0' or self.coefficients[1] == '0' or self.coefficients[2] == '0' or \
                    self.coefficients[0] == '-0' or self.coefficients[1] == '-0' or self.coefficients[2] == '-0' or \
                    self.coefficients[0] == '+0' or self.coefficients[1] == '+0' or self.coefficients[2] == '+0':
                raise Zero_Error()
            if self.type_of_equation == 'ax² + bx + c = 0':
                self.quadratic_equation1()
            if self.type_of_equation == 'ax² + bx = 0':
                self.quadratic_equation2()
            if self.type_of_equation == 'ax² + c = 0':
                self.quadratic_equation3()
            if self.type_of_equation == 'ax² = 0':
                self.quadratic_equation4()
        except ValueError:
            self.main.statusBar().showMessage("Ввeдите числа правильно!")
            self.main.statusBar().show()
            self.aftererror()
        except Input_Error:
            self.main.statusBar().showMessage("Заполните обязательные поля!")
            self.main.statusBar().show()
            self.aftererror()
        except Zero_Error:
            self.main.statusBar().showMessage("Ноль не может быть введен!")
            self.main.statusBar().show()
            self.aftererror()

    """Метод quadratic_equation1 решает полное квадратное уравнение ax² + bx + c = 0"""

    def quadratic_equation1(self):
        if self.coefficients[1] and self.coefficients[2]:
            self.main.statusBar().hide()
            discr = float(self.coefficients[1]) ** 2 - 4 * float(self.coefficients[0]) * float(
                self.coefficients[2])
            discr = int(discr) if discr == float(int(discr)) else discr
            self.main.label_6.setText(
                f'D = ({self.coefficients[1]})² - 4 * {self.coefficients[0]} * {self.coefficients[2]} = {discr}')
            if discr > 0:
                self.main.label_7.setText('D > 0')
                self.main.label_8.setText('Количество корней: 2')
                x1 = (-float(self.coefficients[1]) - m.sqrt(discr)) / (2 * float(self.coefficients[0]))
                x1 = int(x1) if x1 == float(int(x1)) else x1
                x2 = (-float(self.coefficients[1]) + m.sqrt(discr)) / (2 * float(self.coefficients[0]))
                x2 = int(x2) if x2 == float(int(x2)) else x2
                multiplication1 = 2 * float(self.coefficients[0])
                multiplication1 = int(multiplication1) if multiplication1 == float(
                    int(multiplication1)) else multiplication1
                minus = -float(self.coefficients[1])
                minus = int(minus) if minus == float(int(minus)) else minus
                if '.' in str(x1):
                    if len(str(x1).split('.')[1]) > 3 and m.sqrt(discr) != float(int(m.sqrt(discr))):
                        x1 = f'({minus} - √{discr}) / {multiplication1}'
                    elif len(str(x1).split('.')[1]) > 3 and m.sqrt(discr) == float(int(m.sqrt(discr))):
                        x1 = f'{minus - int(m.sqrt(discr))} / {multiplication1}'
                if '.' in str(x2):
                    if len(str(x2).split('.')[1]) > 3 and m.sqrt(discr) != float(int(m.sqrt(discr))):
                        x2 = f'({minus} + √{discr}) / {multiplication1}'
                    elif len(str(x2).split('.')[1]) > 3 and m.sqrt(discr) == float(int(m.sqrt(discr))):
                        x2 = f'{minus + int(m.sqrt(discr))} / {multiplication1}'
                if '/' in x1 and '√' not in x1:
                    sp = x1.split(' / ')
                    if float(sp[0]) == float(int(sp[0])) and float(sp[1]) == float(int(sp[1])):
                        nod = m.gcd(int(sp[0]), int(sp[1]))
                        x1 = f'{int(int(sp[0]) / nod)} / {int(int(sp[1]) / nod)}'
                if '/' in x2 and '√' not in x2:
                    sp = x2.split(' / ')
                    if float(sp[0]) == float(int(sp[0])) and float(sp[1]) == float(int(sp[1])):
                        nod = m.gcd(int(sp[0]), int(sp[1]))
                        x2 = f'{int(int(sp[0]) / nod)} / {int(int(sp[1]) / nod)}'
                self.main.label_9.setText(
                    f'X₁ = (-({self.coefficients[1]}) - √{discr}) / (2 * {self.coefficients[0]}) = {x1}')
                self.main.label_10.setText(
                    f'X₂ = (-({self.coefficients[1]}) + √{discr}) / (2 * {self.coefficients[0]}) = {x2}')
                self.main.label_11.setText(f'Ответ: {x1}; {x2}')
            if discr == 0:
                self.main.label_7.setText('D = 0')
                self.main.label_8.setText('Количество корней: 1')
                x1 = (-int(self.coefficients[1]) - m.sqrt(discr)) / 2 * int(self.coefficients[0])
                x1 = int(x1) if x1 == float(int(x1)) else x1
                self.main.label_9.setText(
                    f'X = (-({self.coefficients[1]}) ± {discr}) / 2 * {self.coefficients[0]} = {x1}')
                self.main.label_10.hide()
                self.main.label_11.setText(f'Ответ: {x1}')
                self.main.label_9.show()
            if discr < 0:
                self.main.label_7.setText('D < 0')
                self.main.label_8.setText('Количество корней: 0')
                self.main.label_9.hide()
                self.main.label_10.hide()
                self.main.label_11.setText(f'Ответ: нет корней')
        else:
            raise Input_Error()

    """Метод quadratic_equation2 решает неполное квадратное уравнение ax² + bx = 0"""

    def quadratic_equation2(self):
        if self.coefficients[1]:
            self.main.statusBar().hide()
            x1 = 0
            x2 = -float(self.coefficients[1]) / float(self.coefficients[0])
            x2 = int(x2) if x2 == float(int(x2)) else x2
            self.main.label_9.setText(f'X₁ = {x1}')
            self.main.label_10.setText(f'X₂ = -({self.coefficients[1]}) / {self.coefficients[0]} = {x2}')
            self.main.label_8.setText('Количество корней: 2')
            self.main.label_11.setText(f'Ответ: {x1}; {x2}')
        else:
            raise Input_Error()

    """Метод quadratic_equation3 решает неполное квадратное уравнение ax² + c = 0"""

    def quadratic_equation3(self):
        if self.coefficients[2]:
            self.main.statusBar().hide()
            separation = -float(self.coefficients[2]) / float(self.coefficients[0])
            if separation < 0:
                self.main.label_11.setText(f'Ответ: нет корней')
                self.main.label_9.hide()
                self.main.label_10.hide()
            if separation > 0:
                self.main.label_8.setText('Количество корней: 2')
                x1 = m.sqrt(separation)
                x1 = int(x1) if x1 == float(int(x1)) else x1
                x2 = -m.sqrt(separation)
                x2 = int(x2) if x2 == float(int(x2)) else x2
                c = float(self.coefficients[2])
                c = int(c) if c == float(int(c)) else c
                a = float(self.coefficients[0])
                a = int(a) if a == float(int(a)) else a
                separation = int(separation) if separation == float(int(separation)) else separation
                if '.' in str(separation):
                    if len(str(separation).split('.')[1]) > 3:
                        separation = f'({-c} / {a})'
                if '.' in str(x1):
                    if len(str(x1).split('.')[1]) > 3:
                        x1 = f'√{separation}'
                if '.' in str(x2):
                    if len(str(x2).split('.')[1]) > 3:
                        x2 = f'-√{separation}'
                self.main.label_9.setText(
                    f'X₁ = √(-({c}) / {a}) = {x1}')
                self.main.label_10.setText(
                    f'X₂ = - √(-({c}) / {a}) = {x2}')
                self.main.label_11.setText(f'Ответ: {x1}; {x2}')
                self.main.label_9.show()
                self.main.label_10.show()
        else:
            raise Input_Error()
