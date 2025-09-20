from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
import styles


class NavBar(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.addStretch()
        layout.setSpacing(5)
        layout.setContentsMargins(15, 20, 15, 20)

        self.setObjectName("navWidget")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        icon = QLabel('🐱')
        icon.setStyleSheet(styles.navbar_icon)
        icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        text = QLabel("Мемные статусы")
        text.setStyleSheet(styles.navbar_text)
        text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 👇Менял стили, сначала всё сломалось, потом починил как-то вот так
        fixed_width = 120
        icon.setFixedWidth(fixed_width)
        text.setFixedWidth(fixed_width)
        layout.addWidget(icon, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(text, alignment=Qt.AlignmentFlag.AlignHCenter)

        layout.addStretch()

        self.setLayout(layout)
        self.setFixedWidth(200)
        self.setStyleSheet(styles.base_navbar)
