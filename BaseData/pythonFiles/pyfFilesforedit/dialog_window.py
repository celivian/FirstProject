from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import uic

"Этот класс окна при входе в программу. Он дает обучение для использования функций программы."

class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('BaseData/uiFiles/dialog.ui', self)
        picture1 = QPixmap('BaseData/static/image1.png')
        picture2 = QPixmap('BaseData/static/image2.png')
        self.label_2.setPixmap(picture1)
        self.label_3.setPixmap(picture2)
        with open('BaseData/static/instruction.txt', 'r', encoding='utf-8') as f:
            a = f.read()
        self.label.setText(a)
        self.label.setWordWrap(True)
