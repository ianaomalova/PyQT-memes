base_navbar = """
#navWidget {
    background:  #ddadaf;
    border-right: 2px solid #ad5b57;
}"""

navbar_icon = """
    QLabel {
        font-size: 48px;
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 rgba(255, 255, 255, 0.1), stop:1 rgba(26, 188, 156, 0.1));
        border: 2px solid #ad5b57;
        border-radius: 25px;
        padding: 15px;
        margin: 10px 0;
        min-height: 50px;
        min-width: 50px;
        text-align: center;
        qproperty-alignment: AlignCenter;
    }

    QLabel:hover {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 rgba(255, 255, 255, 0.2), stop:1 rgba(26, 188, 156, 0.2));
        border: 2px solid #6b3633;
    }
"""

navbar_text = """
    QLabel {
        color: #ad5b57;
        font-size: 14px;
        font-weight: 600;
        font-family: 'Segoe UI', Arial, sans-serif;
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
            stop:0 rgba(255, 255, 255, 0.8), stop:1 rgba(255, 255, 255, 0.4));
        border: 1px solid #ad5b57;
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
        border: 1px solid #6b3633;
        color: #ad5b57;
    }
"""

load_buttons = """
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(210, 180, 140, 0.8), stop:1 rgba(193, 154, 107, 0.8));
                color: white;
                border: 2px solid #C19A6B;
                border-radius: 10px;
                padding: 14px 20px;
                text-align: center;
                font-size: 16px;
                font-weight: 600;
                min-height: 22px;
                min-width: 100px;
            }

            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(210, 180, 140, 1.0), stop:1 rgba(193, 154, 107, 1.0));
                border: 2px solid #A67C52;
            }

            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(160, 82, 45, 0.9), stop:1 rgba(130, 60, 30, 0.9));
                border: 2px solid #8B4513;
            }

            QPushButton:disabled {
                background: rgba(75, 54, 33, 0.6);
                color: rgba(180, 160, 140, 0.8);
                border: 2px solid rgba(90, 65, 40, 0.8);
            }
        """

cmdbuttons = """
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(255, 100, 100, 0.8), stop:1 rgba(255, 70, 70, 0.8));
                color: white;
                border: 2px solid #ff6464;
                border-radius: 10px;
                padding: 14px 20px;
                text-align: center;
                font-size: 16px;
                font-weight: 600;
                min-height: 22px;
                min-width: 100px;
            }

            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(255, 100, 100, 1.0), stop:1 rgba(255, 70, 70, 1.0));
                border: 2px solid #ff4d4d;
            }

            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(220, 50, 50, 0.9), stop:1 rgba(190, 30, 30, 0.9));
                border: 2px solid #cc3333;
            }

            QPushButton:disabled {
                background: rgba(102, 0, 51, 0.6);
                color: rgba(200, 180, 190, 0.8);
                border: 2px solid rgba(120, 20, 60, 0.8);
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
                border: 2px solid #ad5b57;
                background: rgba(255, 255, 255, 1.0);
                outline: none;
            }

            #statusInput:hover {
                border: 2px solid #ad5b57;
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