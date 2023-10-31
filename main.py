import io
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Organizer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

    def initUI(self):



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Organizer()
    ex.show()
    sys.exit(app.exec_())
