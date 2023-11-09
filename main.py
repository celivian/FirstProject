import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from quadratic_equation import *
from input_qe import *
from check_is_root import *
from grahps import *

"""Это класс окна. Он запускает интерфейс программы"""


class Organizer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    """Метод initUI запускает основной интерфейс программы:
    создает объекты виджета в соответствующих контейнерах и 
    присваивает им правильные имена объектов."""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 592)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.setFixedSize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 821, 541))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 0, 291, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic UI")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(320, 0, 20, 481))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(90, 390, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(20, 110, 281, 101))
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 220, 110, 149))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.coefa = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.coefa.setObjectName("coefa")
        self.horizontalLayout_6.addWidget(self.coefa)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.coefb = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.coefb.setObjectName("coefb")
        self.horizontalLayout_3.addWidget(self.coefb)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.coefc = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.coefc.setObjectName("coefc")
        self.horizontalLayout_5.addWidget(self.coefc)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(340, 40, 361, 181))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(340, 220, 361, 261))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic")
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 450, 151, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 450, 161, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(340, 0, 401, 31))
        self.label_13.setObjectName("label_13")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quadratic equations"))
        self.label.setText(_translate("MainWindow", "Выберите вид квадратного уравнения"))
        self.comboBox.setItemText(0, _translate("MainWindow", "ax² + bx + c = 0"))
        self.comboBox.setItemText(1, _translate("MainWindow", "ax² + bx = 0"))
        self.comboBox.setItemText(2, _translate("MainWindow", "ax² + c = 0"))
        self.comboBox.setItemText(3, _translate("MainWindow", "ax² = 0"))
        self.pushButton.setText(_translate("MainWindow", "Рассчитать"))
        self.label_5.setText(_translate("MainWindow",
                                        "Введите коэффициенты. Если коэффициент a = 1, можете оставить эту ячейку пустой. А если a = -1, напишите просто -."))
        self.label_4.setText(_translate("MainWindow", "a ="))
        self.label_3.setText(_translate("MainWindow", "b ="))
        self.label_2.setText(_translate("MainWindow", "c ="))
        self.label_6.setText(_translate("MainWindow", "D = b² - 4 * a * c = ?"))
        self.label_7.setText(_translate("MainWindow", "D ? 0"))
        self.label_8.setText(_translate("MainWindow", "Количество корней: ?"))
        self.label_9.setText(_translate("MainWindow", "X₁ = (-(b) - √D) / 2 * a = ?"))
        self.label_10.setText(_translate("MainWindow", "X₂ = (-(b) + √D) / 2 * a = ?"))
        self.label_11.setText(_translate("MainWindow", "Ответ: ?"))
        self.pushButton_2.setText(_translate("MainWindow", "Проверить корни"))
        self.pushButton_3.setText(_translate("MainWindow", "Построить график"))
        self.label_13.setText(_translate("MainWindow", "[Уравнение]"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Квадратные уравнения"))
        self.input = InputQE(self, Quadratic_Equation(self))
        self.pushButton_2.clicked.connect(self.window2)
        self.pushButton.clicked.connect(self.input.calculation)
        self.comboBox.activated.connect(self.input.choice_equation)

    def window2(self):
        self.win = Check_Is_Root(self)
        self.win.show()

    def form(self):
        fl1 = False
        fl2 = False
        coefa = self.coefa.text()
        coefb = self.coefb.text()
        coefc = self.coefc.text()
        type_of_equation = self.comboBox.currentText()
        try:
            if (coefb and coefc and type_of_equation == "ax² + bx + c = 0") or (
                    coefb and type_of_equation == 'ax² + bx = 0') or (
                    coefc and type_of_equation == 'ax² + c = 0') or type_of_equation == "ax² = 0":
                if not coefa:
                    coefa = '1'
                if not coefb:
                    coefb = '1'
                    fl1 = True
                if not coefc:
                    coefc = '1'
                    fl2 = True
                coefficients = [coefa, coefb, coefc]
                if coefficients[0][0] == '0' or '-0' in coefficients[0] or '+0' in coefficients[0] or \
                        coefficients[1][0] == '0' or '-0' in coefficients[1] or '+0' in coefficients[1] \
                        or coefficients[2][0] == '0' or '-0' in coefficients[2] or \
                        '+0' in coefficients[2]:
                    raise ValueError
                else:
                    if fl1:
                        coefb = ''
                        fl1 = False
                    if fl2:
                        coefc = ''
                        fl2 = False
                    formed = type_of_equation.replace('a', coefa)
                    test = float(coefa)
                    if coefb:
                        if float(coefb) < 0:
                            i = formed.index('+')
                            formed = formed[:i] + '-' + formed[i + 1:]
                            coefb = coefb[1:]
                        formed = formed.replace('b', coefb)
                    if coefc:
                        if float(coefc) < 0:
                            i = formed.index('+')
                            i2 = formed.index('+', i, len(formed))
                            formed = formed[:i2] + '-' + formed[i2 + 1:]
                            coefc = coefc[1:]
                        formed = formed.replace('c', coefc)
                    self.label_13.setText(formed)
            else:
                self.label_13.setText('[Уравнение]')
        except ValueError:
            self.label_13.setText('[Уравнение]')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Organizer()
    ex.show()
    sys.exit(app.exec_())
