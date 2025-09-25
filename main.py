import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout

from navbar import NavBar
from content_page import PageOne

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Константин Дробязкин")

        main_layout = QHBoxLayout(self)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)

        navbar = NavBar()
        page = PageOne()

        main_layout.addWidget(navbar)
        main_layout.addWidget(page)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    font = QFont("Arial", 12)
    app.setFont(font)
    window = MainWindow()
    window.setFixedSize(800, 600)
    window.show()
    sys.exit(app.exec())