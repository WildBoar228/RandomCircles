import random
import sys
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow,
                             QPushButton, QInputDialog)


class Ui_Circles(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(572, 431)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.drawBtn = QtWidgets.QPushButton(self.centralwidget)
        self.drawBtn.setGeometry(QtCore.QRect(200, 150, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.drawBtn.setFont(font)
        self.drawBtn.setObjectName("drawBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 572, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.drawBtn.setText(_translate("MainWindow", "Нарисовать"))


class Example(QMainWindow, Ui_Circles):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stripes = ''
        self.is_pressed = False;
        self.initUI()

    def initUI(self):
        self.drawBtn.clicked.connect(self.paint)

    def paint(self):
        self.is_pressed = True;
        self.repaint()

    def paintEvent(self, event):
        if self.is_pressed:
            qp = QPainter(self)
            qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255),
                               random.randint(0, 255)))
            qp.begin(self)
            size = random.randint(20, 70)
            qp.drawEllipse(random.randint(size // 2, self.width() - size // 2),
                           random.randint(size // 2, self.height() - size // 2),
                           size, size)
            qp.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
