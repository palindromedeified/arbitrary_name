from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor, QBrush
from PyQt5.QtCore import Qt
from PyQt5 import uic
from random import randint
import sys


class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.circle)
        canvas = QPixmap(600, 600)
        self.label.setPixmap(canvas)

    def circle(self):
        x, y = randint(10, 320), randint(150, 400)
        radius = randint(20, 50)
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(Qt.yellow))
        painter.setPen(pen)
        painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        painter.drawEllipse(x, y, radius, radius)
        painter.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())
