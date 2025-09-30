from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
import styles


class NavBar(QWidget):
    category_selected = pyqtSignal(str)
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.addStretch()
        layout.setSpacing(5)
        layout.setContentsMargins(15, 20, 15, 20)

        self.setObjectName("navWidget")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        icon = QLabel('🐈‍⬛')
        icon.setStyleSheet(styles.navbar_icon)
        text = QLabel("коты")
        text.setStyleSheet(styles.navbar_text)
    
        self.btn_cat = QPushButton("коты")
        self.btn_cat.setStyleSheet(styles.load_buttons)
        self.btn_cat.setFlat(True)
        self.btn_cat.clicked.connect(self.on_cat_clicked)

        self.btn_dog = QPushButton("собаки")
        self.btn_dog.setStyleSheet(styles.load_buttons)
        self.btn_dog.setFlat(True)
        self.btn_dog.clicked.connect(self.on_dog_clicked)

        self.btn_garden = QPushButton("сад")
        self.btn_garden.setStyleSheet(styles.load_buttons)
        self.btn_garden.setFlat(True)
        self.btn_garden.clicked.connect(self.on_garden_clicked)
    
        layout.addWidget(icon)
        layout.addWidget(self.btn_cat)
        layout.addWidget(self.btn_dog)
        layout.addWidget(self.btn_garden)
        layout.addStretch()



        self.setLayout(layout)
        self.setFixedWidth(200)
        self.setStyleSheet(styles.base_navbar)

    def on_cat_clicked(self):
        self.category_selected.emit("cat")

    def on_dog_clicked(self):
        self.category_selected.emit("dog")

    def on_garden_clicked(self):
        self.category_selected.emit("garden")

