base_navbar = """
#navWidget {
    background:  #EE82EE;
    border-right: 2px solid #C71585;
}"""

navbar_icon = """
    QLabel {
        font-size: 80px;
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 rgba(255, 255, 255, 0.1), stop:1 rgba(255, 0, 255, 0.1));
        border: 2px solid rgba(255, 0, 255, 0.3);
        border-radius: 50px;
        padding: 15px;
        margin: 10px 0;
        min-height: 50px;
        min-width: 50px;
        text-align: center;
        qproperty-alignment: AlignCenter;
    }

    QLabel:hover {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 rgba(255, 255, 255, 0.2), stop:1 rgba(199, 21, 133, 0.2));
        border: 2px solid rgba(199, 21, 133, 0.5);
    }
"""

navbar_text = """
    QLabel {
        color: #800080;
        font-size: 18px;
        font-weight: 600;
        font-family: 'Segoe UI', Arial, sans-serif;
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
            stop:0 rgba(255, 255, 255, 0.8), stop:1 rgba(255, 0, 255, 0.4));
        border: 1px solid rgba(0, 0, 128, 0.2);
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
            stop:0 rgba(255, 255, 255, 0.9), stop:1 rgba(199, 21, 133, 0.6));
        border: 1px solid rgba(186, 85, 211, 0.4);
        color: #800080;
    }
"""

load_buttons = """
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(255, 0, 255, 0.8), stop:1 rgba(30, 144, 255, 0.7));
                color: aqua;
                border-radius: 20px;
                padding: 14px 20px;
                text-align: center;
                font-size: 24px;
                font-weight: 600;
                min-height: 22px;
                min-width: 100px;
            }

            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:1 rgba(30, 144, 255, 1.0), stop:0 rgba(255, 0, 255, 1.0));
            }

            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(0, 255, 255, 0.9), stop:1 rgba(127, 255, 212, 0.9));
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
                border: 2px solid rgba(224, 255, 255, 0.6);
                border-radius: 20px;
                padding: 10px 12px;
                font-size: 16px;
                color: #2c3e50;
                selection-background-color: rgba(119, 136, 153, 0.3);
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