import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QStackedWidget

from navbar import NavBar
from pages.page_one import PageOne
from pages.page_two import PageTwo


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Мемный семинар")

        container = QWidget()
        main_layout = QHBoxLayout(container)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.setCentralWidget(container)

        self.navbar = NavBar(["Страница 1", "Страница 2"], self.switch_page)

        self.stack = QStackedWidget()
        self.page1 = PageOne()
        self.page2 = PageTwo()
        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2)

        main_layout.addWidget(self.navbar)
        main_layout.addWidget(self.stack)


    def switch_page(self, index: int):
        self.stack.setCurrentIndex(index)
        self.navbar.update_active_button(index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setFixedSize(800, 600)
    window.show()
    sys.exit(app.exec())