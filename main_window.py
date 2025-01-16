from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from sidebar import Sidebar
from dashboard import Dashboard

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AgenteInv")
        self.setMinimumSize(1200, 800)
        
        # Central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        
        # Add sidebar
        self.sidebar = Sidebar()
        main_layout.addWidget(self.sidebar)
        
        # Add dashboard
        self.dashboard = Dashboard()
        main_layout.addWidget(self.dashboard)
        
        # Set layout proportions
        main_layout.setStretch(0, 1)  # Sidebar
        main_layout.setStretch(1, 4)  # Dashboard
