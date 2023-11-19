from main import *
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtWidgets

"""Этот класс проверяте являются введенные числа корнями введенного уравнения"""

class Check_Is_Root(QWidget):
    def __init__(self, main):
        super(Check_Is_Root, self).__init__()
        self.main = main
        self.setupUi(self)

    """Метод setupUI запускает основной интерфейс программы:
        создает объекты виджета в соответствующих контейнерах и 
        присваивает им правильные имена объектов."""

    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.setFixedSize(579, 435)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 559, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setText("")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 511, 21))
        font = QtGui.QFont()
        font.setFamily("Alef")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(18, 140, 241, 149))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 320, 561, 71))
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(290, 190, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(10, 400, 381, 21))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(260, 140, 21, 161))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        text = self.main.label_13.text()
        self.pushButton.clicked.connect(self.check)
        self.label_2.setText(text)
        self.main.statusBar().hide()
        self.label_7.hide()

    """Метод retranslateUi помогает в создании интерфейса программы"""

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Check is root"))
        self.label.setText(_translate("Form", "Введенное уравнение -->"))
        self.label_3.setText(_translate("Form", "Ввести корни: (необязательно вводить оба корня)"))
        self.label_4.setText(_translate("Form", "X₁ = "))
        self.label_5.setText(_translate("Form", "X₂ = "))
        self.label_6.setText(_translate("Form", "Ответ:"))
        self.pushButton.setText(_translate("Form", "Проверить"))

    """Метод check проверяет корни и вывод в зависимости от этого ответ"""

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