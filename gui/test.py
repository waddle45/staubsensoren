from PyQt6.QtWidgets import QApplication, QWidget, QLabel
import sys


class main_window(QWidget):
    def init(self):
        super().init()
        self.label = QLabel("Amogus", self)
        self.show()


def main():
    global main_window
    app = QApplication(sys.argv)
    main = main_window()
    main.show()

    app.exec()

if __name__ == '__main__':
    main()
