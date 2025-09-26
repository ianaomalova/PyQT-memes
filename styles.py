base_navbar = """
#navWidget {
    background:  #ADD8E6;
    border-right: 2px solid #1abc9c;
}"""


navbar_icon = """
    QLabel {
        font-size: 48px;
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 rgba(34, 153, 200, 1), stop:1 rgba(111, 23, 211, 0.1));
        border: 3px solid rgba(50, 110, 220, 0.3);
        border-radius: 40px;
        padding: 13px;
        margin: 10px 0;
        min-height: 50px;
        min-width: 50px;
        text-align: center;
        qproperty-alignment: AlignCenter;
    }

    QLabel:hover {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 rgba(111, 222, 111, 0.6), stop:1 rgba(123, 133, 210, 0.2));
        border: 2px solid rgba(100, 188, 100, 0.5);
    }3
"""

knopka_clear = """
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(230, 5, 5, 1), stop:1 rgba(209, 5, 5, 0.9));
                color: white;
                border: 2px solid #e74c3c;
                border-radius: 12px;
                padding: 12px 16px;
                font-size: 13px;
                font-weight: 600;
                min-height: 20px;
                margin: 5px 10px;
            }

            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(230, 7, 6, 1.0), stop:1 rgba(200, 5, 4, 1.0));
                border: 2px solid #c0392b;
            }

            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(192, 57, 43, 0.7), stop:1 rgba(155, 48, 39, 0.9));
                border: 2px solid #a93226;
            }

            QPushButton:disabled {
                background: rgba(130, 130, 130, 0.5);
                color: grey;
                border: 2px solid rgba(189, 195, 199, 0.8);
            }
"""
navbar_text = """
    QLabel {
        color: #2c3e50;
        font-size: 14px;
        font-weight: 600;
        font-family: 'Segoe UI', Arial, sans-serif;
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
            stop:0 rgba(255, 255, 255, 0.8), stop:1 rgba(255, 255, 255, 0.4));
        border: 1px solid rgba(26, 188, 156, 0.2);
        border-radius: 12px;
        padding: 12px 8px;
        margin: 5px 0;
        letter-spacing: 0.5px;
        line-height: 1.4;
        text-align: center;
        qproperty-alignment: AlignCenter;
    }

    QLabel:hover {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
            stop:0 rgba(255, 255, 255, 0.9), stop:1 rgba(255, 255, 255, 0.6));
        border: 1px solid rgba(26, 188, 156, 0.4);
        color: #1abc9c;
    }
"""

load_buttons = """
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(255, 193, 7, 0.8), stop:1 rgba(255, 152, 0, 0.8));
                color: white;
                border: 2px solid #ffc107;
                border-radius: 10px;
                padding: 14px 20px;
                text-align: center;
                font-size: 14px;
                font-weight: 600;
                min-height: 22px;
                min-width: 100px;
            }

            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(255, 193, 7, 1.0), stop:1 rgba(255, 152, 0, 1.0));
                border: 2px solid #e0a800;
            }

            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(255, 152, 0, 0.9), stop:1 rgba(230, 126, 34, 0.9));
                border: 2px solid #d68910;
            }

            QPushButton:disabled {
                background: rgba(189, 195, 199, 0.6);
                color: rgba(127, 140, 141, 0.8);
                border: 2px solid rgba(189, 195, 199, 0.8);
            }
        """

input_status = """
            #statusInput {
                background: rgba(255, 255, 255, 0.9);
                border: 2px solid rgba(52, 152, 219, 0.6);
                border-radius: 8px;
                padding: 10px 12px;
                font-size: 13px;
                color: #2c3e50;
                selection-background-color: rgba(52, 152, 219, 0.3);
            }

            #statusInput:focus {
                border: 2px solid #3498db;
                background: rgba(255, 255, 255, 1.0);
                outline: none;
            }

            #statusInput:hover {
                border: 2px solid rgba(52, 152, 219, 0.8);
                background: rgba(255, 255, 255, 0.95);
            }

            #statusInput:read-only {
                background: rgba(236, 240, 241, 0.8);
                color: rgba(127, 140, 141, 1.0);
                border: 2px solid rgba(189, 195, 199, 0.6);
            }

            #statusInput::placeholder {
                color: rgba(149, 165, 166, 0.8);
                font-style: italic;
            }
        """