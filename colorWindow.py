import sys
from functools import partial

from PyQt5.QtWidgets import *
from context import Const
from staticMethods import *


class ColorWindow(QMainWindow):
    WIDTH = 400
    HEIGHT = 500

    def __init__(self, colors):
        super().__init__()

        self.colors = colors
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, self.WIDTH, self.HEIGHT)
        self.setWindowTitle('Color dialog')


        self.widget = QWidget()
        self.grid = QGridLayout(self.widget)
        self.setCentralWidget(self.widget)


        self.area_1 = create_btn("Square 1", 100, 50, Const.MENU_BUTTONS_STYLE)
        self.area_1.clicked.connect(partial(self.showDialog, 1))
        self.grid.addWidget(self.area_1, 0, 0)

        self.frm_1 = QFrame(self)
        self.frm_1.setStyleSheet("QWidget { background-color: rgb%s;}" % str(self.colors[0]))
        self.grid.addWidget(self.frm_1, 1, 0)

        self.area_2 = create_btn("Square 2", 100, 50, Const.MENU_BUTTONS_STYLE)
        self.area_2.clicked.connect(partial(self.showDialog, 2))
        self.grid.addWidget(self.area_2, 0, 1)

        self.frm_2 = QFrame(self)
        self.frm_2.setStyleSheet("QWidget { background-color: rgb%s;}" % str(self.colors[1]))
        self.grid.addWidget(self.frm_2, 1, 1)

        self.area_3 = create_btn("Square 3", 100, 50, Const.MENU_BUTTONS_STYLE)
        self.area_3.clicked.connect(partial(self.showDialog, 3))
        self.grid.addWidget(self.area_3, 2, 0)

        self.frm_3 = QFrame(self)
        self.frm_3.setStyleSheet("QWidget { background-color: rgb%s;}" % str(self.colors[2]))
        self.grid.addWidget(self.frm_3, 3, 0)

        self.area_4 = create_btn("Square 4", 100, 50, Const.MENU_BUTTONS_STYLE)
        self.area_4.clicked.connect(partial(self.showDialog, 4))
        self.grid.addWidget(self.area_4, 2, 1)
        self.frm_4 = QFrame(self)

        self.frm_4.setStyleSheet("QWidget { background-color: rgb%s;}" % str(self.colors[3]))
        self.grid.addWidget(self.frm_4, 3, 1)

        self.show()

    def showDialog(self, area):
        col = QColorDialog.getColor()
        rgb = col.getRgb()
        if col.isValid():
            if area == 1:
                self.frm_1.setStyleSheet("QWidget { background-color: %s }" % col.name())
                self.colors[0] = rgb[:3]
            if area == 2:
                self.frm_2.setStyleSheet("QWidget { background-color: %s }" % col.name())
                self.colors[1] = rgb[:3]
            if area == 3:
                self.frm_3.setStyleSheet("QWidget { background-color: %s }" % col.name())
                self.colors[2] = rgb[:3]
            if area == 4:
                self.frm_4.setStyleSheet("QWidget { background-color: %s }" % col.name())
                self.colors[3] = rgb[:3]