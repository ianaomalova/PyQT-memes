base_navbar = """
#navWidget {
    background:  #98FB98;
    border-right: 2px solid #009B77;
}"""

navbar_icon = """
    QLabel {
        font-size: 48px;
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
            stop:0 rgba(255, 255, 255, 0.6), stop:1 rgba(153, 255, 153, 1.0));
        border: 2px solid rgba(77, 34, 14, 1.0);
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
            stop:0 rgba(255, 255, 255, 0.9), stop:1 rgba(255, 255, 255, 0.6));
        border: 2px solid rgba(0, 155, 119, 1.0);
    }
"""

navbar_text = """
    QLabel {
        color: #013220;
        font-size: 14px;
        font-weight: 600;
        font-family: 'Segoe UI', Arial, sans-serif;
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
            stop:0 rgba(255, 255, 255, 0.6), stop:1 rgba(153, 255, 153, 1.0));
        border: 2px solid rgba(77, 34, 14, 1.0);
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
        border: 2px solid rgba(0, 155, 119, 1.0);
        color: #2E3A23;
    }
"""

load_buttons = """
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(152, 251, 152, 0.8), stop:1 rgba(0, 255, 127, 0.8));
                color: #013220;
                border: 2px solid #7CFC00;
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
                    stop:0 rgba(0, 255, 0, 1.0), stop:1 rgba(50, 205, 50, 1.0));
                border: 2px solid #009B77;
            }

            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(0, 255, 0, 1.0), stop:1 rgba(50, 205, 50, 1.0));
                border: 2px solid #d68910;
            }

            QPushButton:disabled {
                background: rgba(77, 34, 14, 0.6);
                color: rgba(127, 140, 141, 0.8);
                border: 2px solid rgba(77, 34, 14, 0.8);
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
                selection-background-color: rgba(124, 252, 0, 0.3);
            }

            #statusInput:focus {
                border: 2px solid #7CFC00;
                background: rgba(255, 255, 255, 1.0);
                outline: none;
            }

            #statusInput:hover {
                border: 2px solid rgba(0, 155, 119, 1.0);
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