import random

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor, QBrush
from PyQt5.QtCore import Qt
from PyQt5 import uic
from random import randint
import sys
from UI import Ui_MainWindow


class Test(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.circle)
        canvas = QPixmap(600, 600)
        self.label.setPixmap(canvas)

    def circle(self):
        x, y = randint(10, 320), randint(150, 400)
        radius = randint(20, 50)
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        color = QColor(*[random.randint(0, 256) for _ in range(3)])
        pen.setColor(color)
        painter.setPen(pen)
        painter.setBrush(QBrush(color, Qt.SolidPattern))
        painter.drawEllipse(x, y, radius, radius)
        painter.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())
