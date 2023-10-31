import io
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class Organizer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled222.ui', self)