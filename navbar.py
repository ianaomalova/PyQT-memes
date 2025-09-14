from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton
import styles


class NavBar(QWidget):
    def __init__(self, buttons: list[str], on_click):
        super().__init__()

        layout = QVBoxLayout()
        layout.addStretch()
        layout.setSpacing(5)
        layout.setContentsMargins(15, 20, 15, 20)

        self.setObjectName("navWidget")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.buttons = []
        for i, text in enumerate(buttons):
            btn = QPushButton(text)
            btn.clicked.connect(lambda _, idx=i: on_click(idx))
            btn.setStyleSheet(styles.buttons_navbar)
            layout.addWidget(btn)
            self.buttons.append(btn)

        layout.addStretch()

        self.setLayout(layout)
        self.setFixedWidth(160)
        self.setStyleSheet(styles.base_navbar)

        self.active_index = None
        self.update_active_button(0)

    def update_active_button(self, active_index):
        for i, btn in enumerate(self.buttons):
            if i == active_index:
                btn.setStyleSheet(styles.active_buttons_navbar)
            else:
                btn.setStyleSheet(styles.buttons_navbar)
        self.active_index = active_index