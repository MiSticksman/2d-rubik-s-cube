import sys

from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QIcon, QColor, QPainter, QFont
from PyQt5.QtWidgets import QMainWindow, QPushButton, QDesktopWidget, QGridLayout, QWidget, QLabel, QDialog

from mainWindow import MainWindow
from rulesWindow import RulesWindow
from context import *
from staticMethods import *


class InitWindow(QMainWindow):
    WIDTH = 350
    HEIGHT = 500

    def __init__(self):
        super().__init__()


        self.grid = QGridLayout()
        self.widget = QWidget()
        self.widget.setLayout(self.grid)
        self.setCentralWidget(self.widget)

        self.init()

    def init(self):
        self.setWindowTitle('Menu')icon
        self.resize(self.WIDTH, self.HEIGHT)
        self.center()

        self.name = QLabel("2D Rubik's Cube")
        self.name.setMinimumSize(360, 50)
        self.name.setStyleSheet("font-family: Decorative;"
                                "color: white;"
                                "font-weight: bold;"
                                "font-size: 45px;"
                                )

        self.btn_start = create_btn("Start", 200, 50, Const.MENU_BUTTONS_STYLE)
        self.btn_start.clicked.connect(self.clicked_on_start)

        self.btn_rules = create_btn("Rules", 250, 50, Const.MENU_BUTTONS_STYLE)
        self.btn_rules.clicked.connect(self.clicked_on_rules)

        self.btn_exit = create_btn("Exit", 250, 50, Const.MENU_BUTTONS_STYLE)
        self.btn_exit.clicked.connect(self.clicked_on_exit)
        self.grid.setVerticalSpacing(20)
        self.grid.setAlignment(Qt.AlignCenter)

        self.grid.addWidget(self.name, 0, 0, 1, 3)
        self.grid.addWidget(self.btn_start, 1, 1)
        self.grid.addWidget(self.btn_rules, 2, 1)
        self.grid.addWidget(self.btn_exit, 3, 1)

        self.setStyleSheet("QMainWindow {background: #296D8E;}")

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def clicked_on_start(self):
        self.main = MainWindow(self)
        self.main.show()
        self.setVisible(False)

    def clicked_on_rules(self):
        self._dialog = QDialog()
        ui = RulesWindow(self._dialog)
        self._dialog.show()

    def clicked_on_exit(self):
        self.close()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.end()

    def _init_info_dialog(self):
        self._dialog = QDialog()
        self._dialog.show()
