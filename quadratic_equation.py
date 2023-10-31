from input_error import *
from main import *


class Quadratic_Equation():
    def __init__(self, type_of_equation, a, b, c):
        self.coefficients = [a, b, c]
        self.toe = type_of_equation

    def solution(self, main):
        if self.toe == 'ax² + bx + c = 0':
            try:
                if self.coefficients[1] and self.coefficients[2]:
                    main.statusBar().hide()
                    discr = int(self.coefficients[1]) ** 2 - 4 * int(self.coefficients[0]) * int(
                        self.coefficients[2])
                    main.label_6().setText('D = {self.coefficients[1]}² - 4 * {self.coefficients[0]} * {self.coefficients[2]} = {discr}')

                else:
                    raise Input_Error()
            except Input_Error:
                main.statusBar().show()
                main.statusBar().showMessage("Заполните обязательные поля!")
