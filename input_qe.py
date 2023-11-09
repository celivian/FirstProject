
"""Это класс ввода информации. Здесь можно брать введеные пользователем данные"""

class InputQE():
    def __init__(self, main1, main2):
        self.main = main1
        self.qe = main2

    """Метод choice_equation отслеживает выбранное уравнение и в соответствии с ним меняет поле вывода информации"""

    def choice_equation(self):
        self.type_of_equation = self.main.comboBox.currentText()
        if self.type_of_equation == 'ax² + bx + c = 0':
            self.main.label_3.show()
            self.main.coefb.show()
            self.main.label_2.show()
            self.main.coefc.show()
            self.main.label_6.show()
            self.main.label_7.show()
            self.main.label_9.show()
            self.main.label_10.show()
            self.main.label_6.setText('D = b² - 4 * a * c = ?')
            self.main.label_7.setText('D ? 0')
            self.main.label_9.setText('X₁ = (-(b) - √D) / 2 * a = ?')
            self.main.label_10.setText('X₂ = (-(b) + √D) / 2 * a = ?')
            self.main.label_13.setText('[Уравнение]')
            self.main.label_9.show()
            self.main.label_10.show()
        if self.type_of_equation == 'ax² + bx = 0':
            self.main.label_3.show()
            self.main.coefb.show()
            self.main.label_2.hide()
            self.main.coefc.hide()
            self.main.label_6.hide()
            self.main.label_7.hide()
            self.main.label_9.setText('X₁ = ?')
            self.main.label_10.setText('X₂ = -b / a = ?')
            self.main.label_13.setText('[Уравнение]')
            self.main.label_9.show()
            self.main.label_10.show()
        if self.type_of_equation == 'ax² + c = 0':
            self.main.label_2.show()
            self.main.coefc.show()
            self.main.label_3.hide()
            self.main.coefb.hide()
            self.main.label_6.hide()
            self.main.label_7.hide()
            self.main.label_9.setText('X₁ = √(-с / a) = ?')
            self.main.label_10.setText('X₂ = -√(-с / a) = ?')
            self.main.label_13.setText('[Уравнение]')
            self.main.label_9.show()
            self.main.label_10.show()
        if self.type_of_equation == 'ax² = 0':
            self.main.label_2.hide()
            self.main.coefc.hide()
            self.main.label_3.hide()
            self.main.coefb.hide()
            self.main.label_6.hide()
            self.main.label_7.hide()
            self.main.label_10.setText('X = ?')
            self.main.label_13.setText('[Уравнение]')
            self.main.label_9.hide()
        self.main.coefa.setText('')
        self.main.coefb.setText('')
        self.main.coefc.setText('')
        self.main.label_8.setText('Количество корней: ?')
        self.main.label_11.setText(f'Ответ: ?')

    """Метод calculation отправляет полученную информацию в другой класс для решения уравнения"""

    def calculation(self):
        coefa = self.main.coefa.text()
        coefb = self.main.coefb.text()
        coefc = self.main.coefc.text()
        self.coefficients = [coefa, coefb, coefc]
        self.type_of_equation = self.main.comboBox.currentText()
        self.qe.solution(self.coefficients, self.type_of_equation)


