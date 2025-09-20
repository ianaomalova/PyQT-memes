from PyQt6.QtCore import QThread, pyqtSignal, Qt, QPoint, QRect
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
import requests
import api
import styles
#Класс для кнопки. Захотел кнопочку, которая сама появляется в углу картинки, если подвести мышку
class HoverLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("border: 1px solid #ddd; border-radius: 8px; background: #f9f9f9;")
# собственно здесь это и реализую через считывание позиции мыши
    def mouseMoveEvent(self, event):
        mouse_pos = event.position().toPoint()
        button_zone = QRect(self.width() - 60, 0, 60, 60)
        parent = self.parent()

        if parent and hasattr(parent, 'clear_button'):
            has_image = getattr(parent, 'has_image', False)

            if button_zone.contains(mouse_pos) and has_image: #has_image - чтобы кнопки не было, когда картинки нет
                parent.clear_button.setVisible(True)
            else:
                parent.clear_button.setVisible(False)

        super().mouseMoveEvent(event)

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
        self.image_label = HoverLabel(self) #тут тоже поменял на свой label
        self.image_label.setScaledContents(True)

        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.image_label)
        self.input.setObjectName("statusInput")
        self.input.setStyleSheet(styles.input_status)

        self.button.clicked.connect(self.load_image)
        self.input.returnPressed.connect(self.load_image) #я фанат того, чтобы кнопки полей тыкались по Enter

        self.clear_button=QPushButton("❌", self.image_label)

        self.setStyleSheet(styles.delete_image)
        self.clear_button.clicked.connect(self.clear_image)
        self.clear_button.setVisible(False)
        self.image_label.resizeEvent = lambda event: self.clear_button.move(self.image_label.width() - 50, 8) #шикарную строчку нашёл, это чтобы крестик был прикреплён к картинке

    def clear_image(self):
        self.image_label.setPixmap(QPixmap())  # Очищаем картинку
        self.has_image = False  #Флаг, что картинки нет
        self.clear_button.setVisible(False)  # Скрываем кнопку

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
        self.has_image = True  # Ставлю флаг, что картинка есть
        self.button.setText("Загрузить картинку")
