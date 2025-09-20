base_navbar = """
#navWidget {
    background:  #ADD8E6;
    border-right: 2px solid #1abc9c;
}"""
delete_image = """
    QPushButton {
        background: rgba(255, 255, 255, 0.1);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 16px;
        padding: 6px;
        width: 32px;
        height: 32px;
        font-size: 16px;
        font-weight: bold;
    }

    QPushButton:hover {
        background: rgba(255, 255, 255, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.4);
        color: #ffffff;
    }

    QPushButton:pressed {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.3);
        padding: 7px;
    }
"""
navbar_icon = """
    QLabel {
        font-size: 48px;
        color: #ffffff; /* Белый текст */
        background: qradialgradient(
            cx: 0.5, cy: 0.5, radius: 1,
            fx: 0.5, fy: 0.5,
            stop:0 rgba(67, 93, 168, 0.8),
            stop:1 rgba(24, 42, 100, 0.9)
        );
        border: 2px solid rgba(100, 120, 190, 0.6);
        border-radius: 30px;
        padding: 20px;
        margin: 12px 0;
        min-height: 60px;
        min-width: 60px;
        text-align: center;
        qproperty-alignment: AlignCenter;
        /* Эффект свечения через бордер */
        border-image: radial-gradient(circle at center, transparent 0%, rgba(67, 93, 168, 0.3) 100%);
    }

    QLabel:hover {
        background: qradialgradient(
            cx: 0.5, cy: 0.5, radius: 1.1,
            fx: 0.5, fy: 0.5,
            stop:0 rgba(80, 110, 200, 0.9),
            stop:1 rgba(20, 50, 120, 0.95)
        );
        border: 2px solid rgba(120, 140, 220, 0.8);
        color: #e0e0ff;
        padding: 22px;
        margin: 10px 0;
        min-height: 64px;
        min-width: 64px;
    }

    QLabel:pressed {
        background: qradialgradient(
            cx: 0.5, cy: 0.5, radius: 0.7,
            fx: 0.5, fy: 0.5,
            stop:0 rgba(50, 70, 140, 0.9),
            stop:1 rgba(15, 25, 60, 0.8)
        );
        border: 2px solid rgba(80, 100, 180, 0.7);
        color: #a0c0ff;
        padding: 18px;
        margin: 14px 0;
        min-height: 56px;
        min-width: 56px;
    }
"""

navbar_text = """
    QLabel {
        color: #ffffff;
        font-size: 15px;
        font-weight: 600;
        font-family: 'Segoe UI', 'Helvetica Neue', sans-serif;
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgba(50, 60, 110, 0.9),
            stop: 1 rgba(20, 30, 70, 0.9)
        );
        border: none;
        border-radius: 16px;
        padding: 16px 16px; 
        margin: 8px 8px;  
        min-width: 130px;
        letter-spacing: 0.8px;
        line-height: 1.5;
        text-align: center;
        qproperty-alignment: AlignCenter;
        border-top: 1px solid rgba(80, 90, 140, 0.6);
        border-left: 1px solid rgba(80, 90, 140, 0.6);
        border-right: 1px solid rgba(50, 60, 100, 0.4);
        border-bottom: 1px solid rgba(50, 60, 100, 0.4);
    }

    QLabel:hover {
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgba(70, 80, 130, 0.95),
            stop: 1 rgba(30, 40, 80, 0.9)
        );
        color: #d0d0ff;
        border: none;
        border-top: 1px solid rgba(100, 110, 160, 0.8);
        border-left: 1px solid rgba(100, 110, 160, 0.8);
        border-right: 1px solid rgba(70, 80, 130, 0.6);
        border-bottom: 1px solid rgba(70, 80, 130, 0.6);
        padding: 17px 17px;  /* ← Соответственно и здесь */
        margin: 7px 7px;
    }

    QLabel:pressed {
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgba(40, 50, 100, 0.9),
            stop: 1 rgba(15, 20, 40, 0.8)
        );
        color: #b0b0e0;
        border: none;
        border-top: 1px solid rgba(60, 70, 120, 0.7);
        border-left: 1px solid rgba(60, 70, 120, 0.7);
        border-right: 1px solid rgba(50, 60, 100, 0.5);
        border-bottom: 1px solid rgba(50, 60, 100, 0.5);
        padding: 19px 19px;  /* ← И здесь */
        margin: 9px 9px;
        min-width: 130px;
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