from typing import NamedTuple


class Const(NamedTuple):
    COLORS = [(178, 34, 34), (0, 0, 205),
              (218, 165, 32), (0, 128, 0)]  # красный, синий, желтый, зеленый

    MENU_BUTTONS_STYLE = "QPushButton {  background-color: #B468DF; border-style: outset; border-width: 2px;  " \
                                      "border-radius: 10px; border-color: beige; font: bold 25px; padding: 6px;}" \
                                      "QPushButton:hover {background-color: lightblue;}" \
                                      "QPushButton:pressed {background-color: #876c99;}"