from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
import styles
import theme


class NavBar(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addStretch()
        layout.setSpacing(5)
        layout.setContentsMargins(15, 20, 15, 20)

        self.setObjectName("navWidget")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.button = QPushButton("сменить тему🎨")
        self.button.setStyleSheet(styles.load_buttons)

        self.icon = QLabel('🐱')
        self.updateTheme()

        text = QLabel("Мемные статусы")
        text.setStyleSheet(styles.navbar_text)

        layout.addWidget(self.icon)
        layout.addWidget(text)
        layout.addWidget(self.button)

        self.button.clicked.connect(self.changeTheme)

        layout.addStretch()

        self.setLayout(layout)
        self.setFixedWidth(200)
        self.setStyleSheet(styles.navbar_dark)

    def changeTheme(self):
        theme.Themes.changeTheme() 
        self.updateTheme()          

    def updateTheme(self):
        if theme.Themes.themeIsDark:
            self.icon.setStyleSheet(styles.icon_style_dark)
            self.setStyleSheet(styles.navbar_dark)
        else:
            self.icon.setStyleSheet(styles.icon_style_light)
            self.setStyleSheet(styles.navbar_light)
            
