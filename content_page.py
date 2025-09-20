from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
import requests
import api
import styles


class ImageLoader(QThread):
    def __init__(self, text: str):
        super().__init__()
        self.text = text

    finished = pyqtSignal(bytes)

    def run(self):
        response = requests.get(api.CAT_URL + self.text)
        if response.status_code == 200:
            self.finished.emit(response.content)

class PageOne(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        
        self.input = QLineEdit()
        self.input.setPlaceholderText("Введите статус ответа")
        self.button = QPushButton("Загрузить картинку")
        self.button.setStyleSheet(styles.load_buttons)
        self.image_label = QLabel("")
        self.image_label.setScaledContents(True)

        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.image_label)
        self.input.setObjectName("statusInput")
        self.input.setStyleSheet(styles.input_status)

        self.button.clicked.connect(self.load_image)
        self.input.returnPressed.connect(self.load_image) #я фанат того, чтобы кнопки полей тыкались по Enter

    def load_image(self):
        text = self.input.text().strip()
        self.button.setEnabled(False)
        self.button.setText("Загружаю...")
        self.thread = ImageLoader(text)
        self.thread.finished.connect(self.display_image)
        self.thread.start()

    def display_image(self, data: bytes):
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        self.image_label.setPixmap(pixmap)
        self.button.setEnabled(True)
        self.button.setText("Загрузить картинку")
