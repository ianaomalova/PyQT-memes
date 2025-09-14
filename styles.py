base_navbar = """
#navWidget {
    background:  #ADD8E6;
    border-right: 2px solid #1abc9c;
}"""

buttons_navbar = """
            QPushButton {
                background: transparent;
                border: 1px solid #1E90FF;;
                color: #1E90FF;
                border-radius: 8px;
                padding: 12px 16px;
                text-align: center;
                font-size: 13px;
                font-weight: 500;
                min-height: 20px;
            }

            QPushButton:hover {
                background: rgba(52, 152, 219, 0.2);
                border: 2px solid rgba(52, 152, 219, 0.5);
                color: #3498db;
            }

            QPushButton:pressed {
                background: rgba(52, 152, 219, 0.3);
                border: 2px solid #3498db;
            }
        """

active_buttons_navbar = """
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(26, 188, 156, 0.3), stop:1 rgba(26, 188, 156, 0.1));
                color: #1abc9c;
                border: 2px solid #1abc9c;
                border-radius: 8px;
                padding: 12px 16px;
                text-align: center;
                font-size: 13px;
                font-weight: 600;
                min-height: 20px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(26, 188, 156, 0.4), stop:1 rgba(26, 188, 156, 0.2));
                border: 2px solid #16a085;
                color: #16a085;
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
                transform: translateY(-1px);
            }

            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(255, 152, 0, 0.9), stop:1 rgba(230, 126, 34, 0.9));
                border: 2px solid #d68910;
                transform: translateY(1px);
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