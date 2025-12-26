base_navbar = """
#navWidget {
    background: #0a0a0a;
    border-right: 2px solid #00ff88;
}
"""

navbar_icon = """
    QLabel {
        font-size: 48px;
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 rgba(255, 255, 255, 0.1), stop:1 rgba(26, 188, 156, 0.1));
        border: 2px solid rgba(26, 188, 156, 0.3);
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
        border: 2px solid rgba(26, 188, 156, 0.5);
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
    background: transparent;
    color: #00ff88;
    border: 2px solid #00ff88;
    border-radius: 8px;
    padding: 10px 20px;
    font-family: 'Courier New', monospace;
    text-transform: uppercase;
}

QPushButton:hover {
    background: rgba(0, 255, 136, 0.1);
    box-shadow: 0 0 15px #00ff88;
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