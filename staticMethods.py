from PyQt5.QtWidgets import QPushButton


def create_btn(name, w, h, style):
    btn = QPushButton(name)
    btn.setMinimumSize(w, h)
    btn.setStyleSheet(style)
    return btn