from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui

"Этот класс окна при входе в программу. Он дает обучение для использования функций программы."

class CustomDialog(QDialog):

    """Метод __init__ создает диалоговое окно при запуске программы"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui(self)
        picture1 = QPixmap('BaseData\static\image1.png')
        picture2 = QPixmap('BaseData\static\image2.png')
        self.label_2.setPixmap(picture1)
        self.label_3.setPixmap(picture2)
        with open('BaseData\static\instruction.txt', 'r', encoding='utf-8') as f:
            a = f.read()
        self.label.setText(a)
        self.label.setWordWrap(True)

    """Метод ui создает интрефейс диалогового окна"""

    def ui(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(728, 388)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(370, 350, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 280, 431, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 331, 231))
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(360, 10, 351, 231))
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)  # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    """Метод retranslateUi помогает создавать интерфейс программы"""

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Mini instruction"))
