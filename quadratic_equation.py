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