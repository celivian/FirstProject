class Quadratic_Equation():
    def __init__(self, type_of_equation, a, b, c):
        self.coefficients = [a, b, c]
        self.toe = type_of_equation

    def solution(self):
        if self.toe == 'ax² + bx + c = 0':
            print(self.coefficients)
