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