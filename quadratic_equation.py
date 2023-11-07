from input_qe import *
import math as m
from errors import *

"""Этот класс решает уравнения, исходя из полученных данных"""

class Quadratic_Equation():
    def __init__(self, main):
        self.main = main
        self.inputqe = InputQE(self.main, self)
        self.inputqe.choice_equation()
