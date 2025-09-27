base_navbar = """
#navWidget {
    background: #e0bfff;  /* Светло-лавандовый фон */
    border-right: 2px solid #9d4edd;  /* Глубокий фиолетовый бордюр */
    border-radius: 15px 0 0 15px;
}
"""

navbar_icon = """
    QLabel {
        font-size: 48px;
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 rgba(255, 255, 255, 0.15), stop:1 rgba(157, 78, 221, 0.1));
        border: 2px solid rgba(157, 78, 221, 0.3);
        border-radius: 30px;
        padding: 16px;
        margin: 12px 0;
        min-height: 56px;
        min-width: 56px;
        text-align: center;
        qproperty-alignment: AlignCenter;
    }

    QLabel:hover {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 rgba(255, 255, 255, 0.25), stop:1 rgba(157, 78, 221, 0.18));
        border: 2px solid rgba(157, 78, 221, 0.5);
        transform: scale(1.05);
    }
"""

navbar_text = """
    QLabel {
        color: #6c248f;
        font-size: 15px;
        font-weight: 600;
        font-family: 'Segoe UI', 'Helvetica', sans-serif;
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
            stop:0 rgba(255, 255, 255, 0.85), stop:1 rgba(255, 255, 255, 0.5));
        border: 1px solid rgba(157, 78, 221, 0.25);
        border-radius: 14px;
        padding: 10px 6px;
        margin: 6px 0;
        letter-spacing: 0.8px;
        line-height: 1.4;
        text-align: center;
        qproperty-alignment: AlignCenter;
    }

    QLabel:hover {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
            stop:0 rgba(255, 255, 255, 0.95), stop:1 rgba(255, 255, 255, 0.7));
        border: 1px solid rgba(157, 78, 221, 0.4);
        color: #9d4edd;
        font-weight: 700;
    }
"""

load_buttons = """
    QPushButton {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop:0 rgba(234, 128, 252, 0.9), stop:1 rgba(199, 105, 233, 0.9));
        color: white;
        border: 2px solid rgba(170, 50, 220, 0.8);
        border-radius: 12px;
        padding: 15px 22px;
        text-align: center;
        font-size: 15px;
        font-weight: 600;
        min-height: 24px;
        min-width: 110px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    QPushButton:hover {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop:0 rgba(234, 128, 252, 1.0), stop:1 rgba(199, 105, 233, 1.0));
        border: 2px solid #9d4edd;
        box-shadow: 0 3px 8px rgba(157, 78, 221, 0.2);
    }

    QPushButton:pressed {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop:0 rgba(170, 50, 220, 0.95), stop:1 rgba(140, 30, 200, 0.95));
        border: 2px solid #8a2be2;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.2);
    }

    QPushButton:disabled {
        background: rgba(180, 180, 180, 0.7);
        color: rgba(100, 100, 100, 0.8);
        border: 2px solid rgba(150, 150, 150, 0.6);
        box-shadow: none;
    }
"""

input_status = """
    #statusInput {
        background: rgba(255, 255, 255, 0.95);
        border: 2px solid rgba(157, 78, 221, 0.5);
        border-radius: 10px;
        padding: 11px 14px;
        font-size: 14px;
        color: #4a148c;
        selection-background-color: rgba(157, 78, 221, 0.4);
        font-family: 'Segoe UI', sans-serif;
    }

    #statusInput:focus {
        border: 2px solid #9d4edd;
        background: white;
        outline: none;
        box-shadow: 0 0 8px rgba(157, 78, 221, 0.3);
    }

    #statusInput:hover:not(:focus) {
        border: 2px solid rgba(157, 78, 221, 0.7);
        background: rgba(255, 255, 255, 0.98);
    }

    #statusInput:read-only {
        background: rgba(240, 240, 245, 0.8);
        color: rgba(120, 120, 120, 1.0);
        border: 2px solid rgba(180, 180, 190, 0.6);
        font-style: italic;
    }

    #statusInput::placeholder {
        color: rgba(150, 100, 180, 0.7);
        font-style: italic;
        font-weight: 500;
    }
"""

clear_button = """
    QPushButton {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop:0 rgba(255, 107, 107, 0.85), stop:1 rgba(220, 70, 70, 0.85));
        color: white;
        border: 2px solid rgba(200, 50, 50, 0.8);
        border-radius: 12px;
        padding: 15px 22px;
        text-align: center;
        font-size: 15px;
        font-weight: 600;
        min-height: 24px;
        min-width: 110px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    QPushButton:hover {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop:0 rgba(255, 107, 107, 1.0), stop:1 rgba(220, 70, 70, 1.0));
        border: 2px solid #c84646;
        box-shadow: 0 3px 8px rgba(220, 70, 70, 0.2);
    }

    QPushButton:pressed {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop:0 rgba(200, 50, 50, 0.95), stop:1 rgba(180, 30, 30, 0.95));
        border: 2px solid #b03030;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.2);
    }

    QPushButton:disabled {
        background: rgba(180, 180, 180, 0.7);
        color: rgba(100, 100, 100, 0.8);
        border: 2px solid rgba(150, 150, 150, 0.6);
        box-shadow: none;
    }
"""