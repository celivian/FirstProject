import math as m
from input_qe import *
from errors import *

"""Этот класс решает уравнения, исходя из полученных данных и выводит решение в специальные поля"""


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
            if float(self.coefficients[0]) == 0.0 or float(self.coefficients[0]) == -0.0:
                raise Zero_Error()
            elif '.' in self.coefficients[0] and float(self.coefficients[0]) < 0:
                if self.coefficients[0][1] == '0' and self.coefficients[0][2] != '.':
                    raise ValueError()
            elif '.' in self.coefficients[0] and float(self.coefficients[0]) > 0:
                if self.coefficients[0][0] == '0' and self.coefficients[0][1] != '.':
                    raise ValueError()
            elif int(self.coefficients[0]) == int(float(self.coefficients[0])) and int(self.coefficients[0]) > 0:
                if self.coefficients[0][0] == '0':
                    raise ValueError()
            elif int(self.coefficients[0]) == int(float(self.coefficients[0])) and int(self.coefficients[0]) < 0:
                if self.coefficients[0][1] == '0':
                    raise ValueError()
            if self.coefficients[1]:
                if float(self.coefficients[1]) == 0.0 or float(self.coefficients[1]) == -0.0:
                    raise Zero_Error()
                elif '.' in self.coefficients[1] and float(self.coefficients[1]) < 0:
                    if self.coefficients[1][1] == '0' and self.coefficients[1][2] != '.':
                        raise ValueError()
                elif '.' in self.coefficients[1] and float(self.coefficients[1]) > 0:
                    if self.coefficients[1][0] == '0' and self.coefficients[1][1] != '.':
                        raise ValueError()
                elif int(self.coefficients[1]) == int(float(self.coefficients[1])) and int(self.coefficients[1]) > 0:
                    if self.coefficients[1][0] == '0':
                        raise ValueError()
                elif int(self.coefficients[1]) == int(float(self.coefficients[1])) and int(self.coefficients[1]) < 0:
                    if self.coefficients[1][1] == '0':
                        raise ValueError()
            if self.coefficients[2]:
                if float(self.coefficients[2]) == 0.0 or float(self.coefficients[2]) == -0.0:
                    raise Zero_Error()
                elif '.' in self.coefficients[2] and float(self.coefficients[2]) < 0:
                    if self.coefficients[2][1] == '0' and self.coefficients[2][2] != '.':
                        raise ValueError()
                elif '.' in self.coefficients[2] and float(self.coefficients[2]) > 0:
                    if self.coefficients[2][0] == '0' and self.coefficients[2][1] != '.':
                        raise ValueError()
                elif int(self.coefficients[2]) == int(float(self.coefficients[2])) and int(self.coefficients[2]) > 0:
                    if self.coefficients[2][0] == '0':
                        raise ValueError()
                elif int(self.coefficients[2]) == int(float(self.coefficients[2])) and int(self.coefficients[2]) < 0:
                    if self.coefficients[2][1] == '0':
                        raise ValueError()
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
            self.aftererror()
        except Input_Error:
            self.main.statusBar().showMessage("Заполните обязательные поля!")
            self.aftererror()
        except Zero_Error:
            self.main.statusBar().showMessage("Ноль не может быть введен!")
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
                divider = 2 * float(self.coefficients[0])
                divider = int(divider) if divider == float(int(divider)) else divider
                coefbminus = -float(self.coefficients[1])
                coefbminus = int(coefbminus) if coefbminus == float(int(coefbminus)) else coefbminus
                root = self.checkroot(discr)
                if isinstance(root, int) or isinstance(root, float):
                    divisiblex1 = coefbminus - root
                    quotientx1 = self.checkseparation(f'{divisiblex1} / {divider}')
                    divisiblex2 = coefbminus + root
                    quotientx2 = self.checkseparation(f'{divisiblex2} / {divider}')
                    x1 = quotientx1
                    x2 = quotientx2
                else:
                    x1 = f'({coefbminus} - {root}) / {divider}'
                    x2 = f'({coefbminus} + {root}) / {divider}'
                self.main.label_7.setText('D > 0')
                self.main.label_8.setText('Количество корней: 2')
                self.main.label_9.setText(
                    f'X₁ = (-({self.coefficients[1]}) - √{discr}) / (2 * {self.coefficients[0]}) = {x1}')
                self.main.label_10.setText(
                    f'X₂ = (-({self.coefficients[1]}) + √{discr}) / (2 * {self.coefficients[0]}) = {x2}')
                self.main.label_11.setText(f'Ответ: {x1}; {x2}')
                self.main.label_9.show()
                self.main.label_10.show()
            if discr == 0:
                quotientx = self.checkseparation(f'{-int(self.coefficients[1])} / {2 * int(self.coefficients[0])}')
                x = quotientx
                self.main.label_7.setText('D = 0')
                self.main.label_8.setText('Количество корней: 1')
                self.main.label_9.setText(
                    f'X = (-({self.coefficients[1]}) ± {discr}) / 2 * {self.coefficients[0]} = {x}')
                self.main.label_11.setText(f'Ответ: {x}')
                self.main.label_10.hide()
                self.main.label_9.show()
            if discr < 0:
                self.main.label_7.setText('D < 0')
                self.main.label_8.setText('Количество корней: 0')
                self.main.label_11.setText(f'Ответ: нет корней')
                self.main.label_9.hide()
                self.main.label_10.hide()
            self.main.form()
        else:
            raise Input_Error()

    """Метод quadratic_equation2 решает неполное квадратное уравнение ax² + bx = 0"""

    def quadratic_equation2(self):
        if self.coefficients[1]:
            self.main.statusBar().hide()
            x1 = 0
            quotientx2 = self.checkseparation(f'{-float(self.coefficients[1])} / {float(self.coefficients[0])}')
            x2 = quotientx2
            self.main.label_9.setText(f'X₁ = {x1}')
            self.main.label_10.setText(f'X₂ = -({self.coefficients[1]}) / {self.coefficients[0]} = {x2}')
            self.main.label_8.setText('Количество корней: 2')
            self.main.label_11.setText(f'Ответ: {x1}; {x2}')
            self.main.form()
        else:
            raise Input_Error()

    """Метод quadratic_equation3 решает неполное квадратное уравнение ax² + c = 0"""

    def quadratic_equation3(self):
        if self.coefficients[2]:
            self.main.statusBar().hide()
            separation = -float(self.coefficients[2]) / float(self.coefficients[0])
            if separation >= 0:
                coefc = -float(self.coefficients[2])
                coefc = int(coefc) if coefc == float(int(coefc)) else coefc
                coefa = float(self.coefficients[0])
                coefa = int(coefa) if coefa == float(int(coefa)) else coefa
                quotientx = self.checkseparation(f'{coefc} / {coefa}')
                if isinstance(quotientx, int) or isinstance(quotientx, float):
                    root = self.checkroot(quotientx)
                    if isinstance(root, int) or isinstance(root, float):
                        x1 = root
                        x2 = -root
                    else:
                        x1 = f'{root}'
                        x2 = f'-{root}'
                else:
                    x1 = f'√({quotientx})'
                    x2 = f'-√({quotientx})'
                self.main.label_8.setText('Количество корней: 2')
                self.main.label_9.setText(
                    f'X₁ = √(-({coefc}) / {coefa}) = {x1}')
                self.main.label_10.setText(
                    f'X₂ = - √(-({coefc}) / {coefa}) = {x2}')
                self.main.label_11.setText(f'Ответ: {x1}; {x2}')
                self.main.label_9.show()
                self.main.label_10.show()
            if separation < 0:
                self.main.label_8.setText('Количество корней: 0')
                self.main.label_11.setText(f'Ответ: нет корней')
                self.main.label_9.hide()
                self.main.label_10.hide()
            self.main.form()
        else:
            raise Input_Error()

    """Метод quadratic_equation4 решает неполное квадратное уравнение ax² = 0"""

    def quadratic_equation4(self):
        self.main.statusBar().hide()
        if self.coefficients[0] == str(int(self.coefficients[0])):
            self.main.label_10.setText(f'X = 0')
            self.main.label_8.setText('Количество корней: 1')
            self.main.label_11.setText(f'Ответ: 0')
            self.main.label_9.hide()
            self.main.form()
        else:
            raise ValueError()

    """Метод aftererror возвращает поле вывода в первоначальный вид"""

    def aftererror(self):
        self.main.statusBar().show()
        if self.type_of_equation == 'ax² + bx + c = 0':
            self.main.label_6.setText('D = b² - 4 * a * c = ?')
            self.main.label_7.setText('D ? 0')
            self.main.label_9.setText('X₁ = (-(b) - √D) / 2 * a = ?')
            self.main.label_10.setText('X₂ = (-(b) + √D) / 2 * a = ?')
            self.main.label_13.setText('[Уравнение]')
            self.main.label_9.show()
            self.main.label_10.show()
        if self.type_of_equation == 'ax² + bx = 0':
            self.main.label_9.setText('X₁ = ?')
            self.main.label_10.setText('X₂ = -b / a = ?')
            self.main.label_13.setText('[Уравнение]')
        if self.type_of_equation == 'ax² + c = 0':
            self.main.label_9.setText('X₁ = √(-с / a) = ?')
            self.main.label_10.setText('X₂ = - √(-с / a) = ?')
            self.main.label_13.setText('[Уравнение]')
            self.main.label_9.show()
            self.main.label_10.show()
        if self.type_of_equation == 'ax² = 0':
            self.main.label_10.setText('X = ?')
            self.main.label_13.setText('[Уравнение]')
            self.main.label_10.show()
        self.main.label_8.setText('Количество корней: ?')
        self.main.label_11.setText('Ответ: ?')

    """Метод checkroot делает число из под корня "красивым", то есть, если оно иррациональное, то запись остается та же,
    а если нет, то записывается целое число"""

    def checkroot(self, rootexpression):
        root = m.sqrt(rootexpression)
        if '.' in str(root):
            if len(str(root).split('.')[1]) > 3:
                return f'√{rootexpression}'
        root = int(root) if root == float(int(root)) else root
        return root

    """Метод checkseparation делает частное при делении двух чисел "красивым", то есть, если частное целое число, то 
    оно и записывается, а если нет, то запись идет в виде дроби"""

    def checkseparation(self, separationexpression):
        sepstr = separationexpression.split(' / ')
        sepint = float(sepstr[0]) / float(sepstr[1])
        if '.' in str(sepint):
            if len(str(sepint).split('.')[1]) > 3 and float(sepstr[0]) == float(int(float(sepstr[0]))) and float(
                    sepstr[1]) == float(int(float(sepstr[1]))):
                nod = m.gcd(int(float(sepstr[0])), int(float(sepstr[1])))
                return f'{int(int(float(sepstr[0])) / nod)} / {int(int(float(sepstr[1])) / nod)}'
            if float(sepstr[0]) != float(int(float(sepstr[0]))) and float(sepstr[1]) != float(int(float(sepstr[1]))):
                return f'{separationexpression}'

        sepint = int(sepint) if sepint == float(int(sepint)) else sepint
        return sepint
