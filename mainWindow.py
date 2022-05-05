from game import Game
from color import Color
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QRect, QObject, QTimer
from PyQt5.QtGui import QPainter, QColor, QPen, QFont, QIcon
from functools import partial
from colorWindow import ColorWindow
from context import Const
from staticMethods import *


class MainWindow(QMainWindow):
    WIDTH = 1000
    HEIGHT = 800

    def __init__(self, init_window):
        super().__init__()
        self.init_window = init_window

        self.game = Game()
        self.field = self.game.field
        self.colors = Const.COLORS

        self.__GAME_BUTTONS_STYLE = "QPushButton { background: rgba(215, 215, 215, 0.15); " \
                                    "border-radius: 10px; border-color: beige; font: bold 25px; padding: 6px;}" \
                                    "QPushButton:hover {background: rgba(215, 215, 215, 0.8);}" \
                                    "QPushButton:pressed {background: rgba(215, 215, 215, 0.6);}"
        self.lcd = QLCDNumber()
        self.check_time = True
        self.timer = QTimer(self)
        self.count_sec = 0
        self.timer.timeout.connect(self.showNum)
        self.startCount()

        self.__init()
        self.__init_buttons()

        self.widgets = QStackedWidget(self)

        self.widget_win = QWidget()
        self.widget_win.setWindowTitle("WIN")
        self.widget_win.setLayout(self.game_win())

        self.widgets.addWidget(self.widget_btn)
        self.widgets.addWidget(self.widget_win)
        self.widgets.setCurrentWidget(self.widget_btn)
        self.setCentralWidget(self.widgets)


    def startCount(self):
        self.timer.start(1000)

    def showNum(self):
        self.count_sec = self.count_sec + 1
        self.lcd.display(self.count_sec)

    def write_time(self):
        with open("results.txt", "a") as file:
            file.write(str(self.count_sec) + '\n')

    def clicked_to_menu(self):
        self.init_window.show()
        self.close()

    def clicked_restart(self):
        self.game.new_game()
        self.count_sec = 0
        Const.COLORS = [(178, 34, 34), (0, 0, 205),
              (218, 165, 32), (0, 128, 0)]
        self.colors = Const.COLORS
        self.update()

    def clicked_exit(self):
        self.close()

    def clicked_color(self):
        self.color_window = ColorWindow(self.colors)
        self.color_window.show()

    def clicked_timer(self):
        if self.check_time:
            self.check_time = False
            self.timer.stop()
        else:
            self.check_time = True
            self.timer.start()


    def mouseMoveEvent(self, event):
        self.moved0(event)
        self.moved1(event)
        self.moved2(event)
        self.moved3(event)
        self.moved4(event)

    def setMouseTracking(self, flag):
        def recursive_set(parent):
            for child in parent.findChildren(QObject):
                try:
                    child.setMouseTracking(flag)
                except:
                    pass
                recursive_set(child)

        QWidget.setMouseTracking(self, flag)
        recursive_set(self)

    def __init_buttons(self):

        self.widget_btn = QWidget()
        self.grid_btn = QGridLayout(self.widget_btn)
        self.grid_btn.setSpacing(10)
        self.grid_btn.setVerticalSpacing(120)
        self.grid_btn.setHorizontalSpacing(30)
        self.grid_btn.setAlignment(Qt.AlignBottom)

        self.grid_btn.addWidget(self.lcd)

        self.btn_to_init = create_btn("Menu", 120, 50, Const.MENU_BUTTONS_STYLE)
        self.btn_to_init.clicked.connect(self.clicked_to_menu)
        self.grid_btn.addWidget(self.btn_to_init, 4, 0)

        self.btn_restart = create_btn("Restart", 120, 50, Const.MENU_BUTTONS_STYLE)
        self.btn_restart.clicked.connect(self.clicked_restart)
        self.grid_btn.addWidget(self.btn_restart, 4, 1)

        self.btn_color = create_btn("Color", 120, 50, Const.MENU_BUTTONS_STYLE)
        self.btn_color.clicked.connect(self.clicked_color)
        self.grid_btn.addWidget(self.btn_color, 4, 2)

        self.btn_timer = create_btn("Timer", 120, 50, Const.MENU_BUTTONS_STYLE)
        self.btn_timer.clicked.connect(self.clicked_timer)
        self.grid_btn.addWidget(self.btn_timer, 4, 3)

        self.btn_exit = create_btn("Exit", 120, 50, Const.MENU_BUTTONS_STYLE)
        self.btn_exit.clicked.connect(self.clicked_exit)
        self.grid_btn.addWidget(self.btn_exit, 4, 4)


        self.btn0 = create_btn("", 50, 70, self.__GAME_BUTTONS_STYLE)
        self.btn0.clicked.connect(partial(self.btn_clicked, 0))
        self.grid_btn.addWidget(self.btn0, 0, 1)

        self.btn1 = create_btn("", 50, 70, self.__GAME_BUTTONS_STYLE)
        self.btn1.clicked.connect(partial(self.btn_clicked, 1))
        self.grid_btn.addWidget(self.btn1, 0, 3)

        self.btn2 = create_btn("", 50, 70, self.__GAME_BUTTONS_STYLE)
        self.btn2.clicked.connect(partial(self.btn_clicked, 2))
        self.grid_btn.addWidget(self.btn2, 2, 1)

        self.btn3 = create_btn("", 50, 70, self.__GAME_BUTTONS_STYLE)
        self.btn3.clicked.connect(partial(self.btn_clicked, 3))
        self.grid_btn.addWidget(self.btn3, 2, 3)

        self.btn4 = create_btn("", 50, 70, self.__GAME_BUTTONS_STYLE)
        self.btn4.clicked.connect(partial(self.btn_clicked, 4))
        self.grid_btn.addWidget(self.btn4, 1, 2)

        self.setMouseTracking(True)
        self.btn0.mouseMoveEvent = self.moved0
        self.btn1.mouseMoveEvent = self.moved1
        self.btn2.mouseMoveEvent = self.moved2
        self.btn3.mouseMoveEvent = self.moved3
        self.btn4.mouseMoveEvent = self.moved4

    def btn_clicked(self, area):
        self.game.rotate(area)

        self.update()

    def moved0(self, event):
        op0 = QGraphicsOpacityEffect()
        if event.pos() in self.btn0.rect():
            op0.setOpacity(0.15)
            self.btn0.setGraphicsEffect(op0)
        else:
            op0.setOpacity(0)
            self.btn0.setGraphicsEffect(op0)

    def moved1(self, event):
        op1 = QGraphicsOpacityEffect()
        if event.pos() in self.btn1.rect():
            op1.setOpacity(0.15)
            self.btn1.setGraphicsEffect(op1)
        else:
            op1.setOpacity(0)
            self.btn1.setGraphicsEffect(op1)

    def moved2(self, event):
        op2 = QGraphicsOpacityEffect()
        if event.pos() in self.btn2.rect():
            op2.setOpacity(0.15)
            self.btn2.setGraphicsEffect(op2)
        else:
            op2.setOpacity(0)
            self.btn2.setGraphicsEffect(op2)

    def moved3(self, event):
        op3 = QGraphicsOpacityEffect()
        if event.pos() in self.btn3.rect():
            op3.setOpacity(0.15)
            self.btn3.setGraphicsEffect(op3)
        else:
            op3.setOpacity(0)
            self.btn3.setGraphicsEffect(op3)

    def moved4(self, event):
        op4 = QGraphicsOpacityEffect()
        if event.pos() in self.btn4.rect():
            op4.setOpacity(0.15)
            self.btn4.setGraphicsEffect(op4)
        else:
            op4.setOpacity(0)
            self.btn4.setGraphicsEffect(op4)

    def __init(self):
        self.setWindowTitle('Game')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(self.WIDTH, self.HEIGHT)
        self.center()
        self.setFixedSize(self.width(), self.height())
        self.init_game_opt()
        self.setStyleSheet("QMainWindow {background: #296D8E;}")

    def keyPressEvent(self, e):
        keyCode = e.key()
        flag = True
        if keyCode == Qt.Key_7:
            area = 0
            self.game.rotate(area)
        elif keyCode == Qt.Key_9:
            area = 1
            self.game.rotate(area)
        elif keyCode == Qt.Key_1:
            area = 2
            self.game.rotate(area)
        elif keyCode == Qt.Key_3:
            area = 3
            self.game.rotate(area)
        elif keyCode == Qt.Key_5:
            area = 4
            self.game.rotate(area)
        else:
            flag = False
        if flag:
            self.repaint()

    def init_game_opt(self):
        self.lgFont = QFont('SimSun', 50)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width()) / 2),
                  int((screen.height() - size.height()) / 2))

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_game_graph(qp)
        qp.end()

    def draw_game_graph(self, qp):
        self.draw_log(qp)
        self.draw_rects(qp)
        if self.game.check_win():
            self.widgets.setCurrentWidget(self.widget_win)


    def draw_rects(self, qp):
        color = 0
        k = 130
        for i in range(len(self.field)):
            for j in range(len(self.field)):
                if self.field[i][j] == Color.RED:
                    color = self.colors[0]
                elif self.field[i][j] == Color.BLUE:
                    color = self.colors[1]
                elif self.field[i][j] == Color.YELLOW:
                    color = self.colors[2]
                elif self.field[i][j] == Color.GREEN:
                    color = self.colors[3]
                qp.setPen(QColor(*color))
                qp.setBrush(QColor(*color))
                qp.drawRoundedRect(250 + j * k, 165 + i * k, 100, 100, 15, 15)
                self.update()


    def draw_log(self, qp):
        pen = QPen(QColor(75, 0, 30))
        qp.setFont(self.lgFont)
        qp.setPen(pen)
        qp.drawText(QRect(30, 0, 900, 150), Qt.AlignCenter, "matching wheel")

    def game_win(self):
        grid = QGridLayout(self.widget_win)
        grid.setAlignment(Qt.AlignCenter)
        win_btn = create_btn("YOU WIN!", 100, 50, Const.MENU_BUTTONS_STYLE)
        win_btn.clicked.connect(self.clicked_win)
        grid.addWidget(win_btn)
        return grid

    def clicked_win(self):
        self.init_window.show()
        self.widgets.setCurrentWidget(self.widget_btn)
        self.write_time()
        self.close()

