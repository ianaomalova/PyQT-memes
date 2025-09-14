import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QStackedWidget

from navbar import NavBar
from content_page import PageOne

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Семинар")

        container = QWidget()
        main_layout = QHBoxLayout(container)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.setCentralWidget(container)

        self.navbar = NavBar()
        self.page1 = PageOne()

        main_layout.addWidget(self.navbar)
        main_layout.addWidget(self.page1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setFixedSize(800, 600)
    window.show()
    sys.exit(app.exec())