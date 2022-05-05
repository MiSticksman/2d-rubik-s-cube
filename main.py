import sys

from PyQt5.QtWidgets import QApplication

from init import InitWindow


def main():
    app = QApplication(sys.argv)
    window = InitWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
