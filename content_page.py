from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt6.QtCore import QTimer
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
        self.input.setObjectName("statusInput")
        self.input.setStyleSheet(styles.input_status)

        self.load_button = QPushButton("Загрузить картинку")
        self.load_button.setStyleSheet(styles.load_buttons)

        self.clear_button = QPushButton("Удалить изображение")
        self.clear_button.setStyleSheet(styles.clear_button)
        self.clear_button.setEnabled(False)

        self.image_label = QLabel("")
        self.image_label.setScaledContents(True)

        layout.addWidget(self.input)
        layout.addWidget(self.load_button)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.image_label)

        self.load_button.clicked.connect(self.load_image)
        self.clear_button.clicked.connect(self.clear_image)

    def load_image(self):
        text = self.input.text().strip()
        self.load_button.setEnabled(False)
        self.load_button.setText("Загружаю...")
        self.thread = ImageLoader(text)
        self.thread.finished.connect(self.display_image)
        self.thread.start()

    def display_image(self, data: bytes):
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        self.image_label.setPixmap(pixmap)
        self.load_button.setEnabled(True)
        self.load_button.setText("Загрузить картинку")
        self.clear_button.setEnabled(True)

    def clear_image(self):
        pixmap = self.image_label.pixmap()
        if pixmap and not pixmap.isNull():
            self.image_label.clear()
            self.clear_button.setText("Картинка удалена")
            self.clear_button.setEnabled(False)
            QTimer.singleShot(1500, lambda: self.clear_button.setText("Удалить изображение"))
        else:
            self.clear_button.setText("Картинка не загружена")
            QTimer.singleShot(1500, lambda: self.clear_button.setText("Удалить изображение"))

