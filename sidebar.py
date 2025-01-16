from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import pyqtSignal

class Sidebar(QWidget):
    pageChanged = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.setMaximumWidth(200)
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # Logo/Title
        title = QLabel("AgenteInv")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)
        
        # Navigation buttons
        nav_buttons = [
            ("Dashboard", "dashboard"),
            ("Portfolio", "portfolio"),
            ("Market Analysis", "market"),
            ("Simulations", "simulations"),
            ("Settings", "settings")
        ]
        
        for btn_text, page_name in nav_buttons:
            btn = QPushButton(btn_text)
            btn.clicked.connect(lambda checked, p=page_name: self.pageChanged.emit(p))
            layout.addWidget(btn)
            
        layout.addStretch()
