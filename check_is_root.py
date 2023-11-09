from main import *
from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from errors import *


class Check_Is_Root(QWidget):
    def __init__(self, main):
        super(Check_Is_Root, self).__init__()
        self.main = main
        self.main.form()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(587, 435)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 559, 78))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 511, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 150, 132, 149))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 320, 471, 71))
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 200, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(10, 400, 381, 21))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        text = self.main.label_13.text()
        try:
            if text == '[Уравнение]':
                raise Input_Error()
            else:
                self.pushButton.clicked.connect(self.check)
                self.label_2.setText(text)
        except Input_Error:
            self.label_7.setText('Введены неверные данные!')
            self.label_7.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Check is root"))
        self.label.setText(_translate("Form", "Введеное уравнение:"))
        self.label_2.setText(_translate("Form", "?"))
        self.label_3.setText(_translate("Form", "Ввести корни: (необязательно вводить оба корня)"))
        self.label_4.setText(_translate("Form", "X₁"))
        self.label_5.setText(_translate("Form", "X₂"))
        self.label_6.setText(_translate("Form", "Ответ:"))
        self.pushButton.setText(_translate("Form", "Проверить"))
        self.label_7.hide()

    def check(self):
        self.type_of_equation = self.main.comboBox.currentText()
        x1 = self.lineEdit_2.text()
        x2 = self.lineEdit.text()
        try:
            if float(x1) < 0:
                x1 = f'({x1})'
            if float(x2) < 0:
                x2 = f'({x2})'
        except ValueError:
            self.label_7.setText('Введите конкретные числа!')
            self.label_7.show()
        self.equation = self.label_2.text().replace('²', '**2')
        i1 = self.equation.index('x')
        self.equation = self.equation[:-4]
        if self.type_of_equation == 'ax² + bx = 0':
            self.equation = self.equation[:-1] + '*' + self.equation[-1]
        if self.type_of_equation == 'ax² + c = 0':
            self.equation = self.equation
        if self.type_of_equation == 'ax² + bx + c = 0':
            sp = self.equation.split('x')
            self.equation = '*x'.join(sp)
        if self.type_of_equation == 'ax² = 0':
            self.equation = self.equation
        if x1 and x2:
            print(self.equation)
            evalum1 = eval(self.equation.replace('x', x1))
            evalum2 = eval(self.equation.replace('x', x2))
            if evalum1 == 0:
                ox1 = 'X₁ является корнем уравнения'
            else:
                ox1 = 'X₁ НЕ является корнем уравнения'

            if evalum2 == 0:
                ox2 = 'X₂ является корнем уравнения'
            else:
                ox2 = 'X₂ НЕ является корнем уравнения'
            print(evalum1)
            print(evalum2)
            self.label_7.hide()
            self.label_6.setText(f'{ox1}, {ox2}')
        if x1 and not x2:
            evalum1 = eval(self.equation.replace('x', x1))

            if evalum1 == 0:
                self.label_6.setText('X₁ является корнем уравнения')
            else:
                self.label_6.setText('X₁ НЕ является корнем уравнения')
            self.label_7.hide()
        if x2 and not x1:
            evalum2 = eval(self.equation.replace('x', x2))
            if evalum2 == 0:
                self.label_6.setText('X₂ является корнем уравнения')
            else:
                self.label_6.setText('X₂ НЕ является корнем уравнения')
            self.label_7.hide()
        print(self.equation)
