from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
import requests
import api
import styles

class ImageLoader(QThread):
    finished = pyqtSignal(bytes)

    def __init__(self, text: str):
        super().__init__()
        self.text = text

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
        self.input.setObjectName("statusInput")
        self.input.setStyleSheet(styles.input_status)

        self.button = QPushButton("Загрузить картинку")
        self.button.setStyleSheet(styles.load_buttons)

        # ➕ Новая кнопка
        self.clear_button = QPushButton("Очистить")
        self.clear_button.setObjectName("clearButton")
        self.clear_button.setStyleSheet(styles.clear_button)
        self.clear_button.setEnabled(False)

        self.image_label = QLabel("")
        self.image_label.setScaledContents(True)

        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.image_label)

        # сигналы
        self.button.clicked.connect(self.load_image)
        self.clear_button.clicked.connect(self.clear_image)

    def load_image(self):
        text = self.input.text().strip()
        if not text:
            return
        self.button.setEnabled(False)
        self.button.setText("Загружаю...")
        self.thread = ImageLoader(text)
        self.thread.finished.connect(self.display_image)
        self.thread.start()

    def display_image(self, data: bytes):
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        self.image_label.setPixmap(pixmap)
        self.clear_button.setEnabled(True)
        self.button.setEnabled(True)
        self.button.setText("Загрузить картинку")

    def clear_image(self):
        self.image_label.clear()
        self.input.clear()
        self.clear_button.setEnabled(False)
