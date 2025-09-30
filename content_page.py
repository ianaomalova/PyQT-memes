from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
import requests
import api
import styles


class ImageLoader(QThread):

    
    def __init__(self, base_url: str, code: str):
        super().__init__()
        self.base_url = base_url
        self.code = code

    finished = pyqtSignal(bytes)

    def run(self):
        response = requests.get(self.base_url + self.code + '.jpg')
        if response.status_code == 200:
            self.finished.emit(response.content)

class PageOne(QWidget):
    def __init__(self):
        super().__init__()
        self.current_api = api.CAT_URL

        layout = QVBoxLayout(self)
        
        self.input = QLineEdit()
        self.input.setPlaceholderText("введите статус ответа")
        self.button = QPushButton("загрузить картинку")
        self.button.setStyleSheet(styles.load_buttons)
        self.cmdbutton = QPushButton("удалить картинку")
        self.cmdbutton.setEnabled(False)
        self.cmdbutton.setStyleSheet(styles.cmdbuttons)
        self.image_label = QLabel("")
        self.image_label.setScaledContents(True)
        

        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.cmdbutton)
        layout.addWidget(self.image_label)
        self.input.setObjectName("statusInput")
        self.input.setStyleSheet(styles.input_status)

        self.button.clicked.connect(self.load_image)
        self.cmdbutton.clicked.connect(self.reload_image)

    def set_api(self, category: str):
        if category == "cat":
            self.current_api = api.CAT_URL
        elif category == "dog":
            self.current_api = api.DOG_URL
        elif category == "garden":
            self.current_api = api.GARDEN_URL
        self.reload_image()

    def reload_image(self):
        self.image_label.clear()
        self.cmdbutton.setEnabled(False)

    def load_image(self):
        text = self.input.text().strip()
        self.button.setEnabled(False)
        self.button.setText("загружаю...")
        self.cmdbutton.setEnabled(False)
        self.cmdbutton.setText("удалить картинку")
        self.thread = ImageLoader(self.current_api, text)
        self.thread.finished.connect(self.display_image)
        self.thread.start()
        

    def display_image(self, data: bytes):
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        self.image_label.setPixmap(pixmap)
        self.button.setEnabled(True)
        self.button.setText("загрузить картинку")
        self.cmdbutton.setEnabled(True)
        self.cmdbutton.setText("удалить картинку")


