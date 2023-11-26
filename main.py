from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
import sys
import random


class YellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circles(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circles(self, qp):
        for n in range(3):
            r = random.randint(10, 40)
            qp.setPen(QColor(238, 210, 18))
            qp.drawEllipse(50 * n, 100, r, r)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    yc = YellowCircles()
    yc.show()
    sys.exit(app.exec())
