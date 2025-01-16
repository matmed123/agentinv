import sys
from pathlib import Path
from dotenv import load_dotenv
from PyQt5.QtWidgets import QApplication

from agenteinv.ui.main_window import MainWindow
from backend.logger import setup_logger

def main():
    app = QApplication(sys.argv)
    print("Iniciando Agente de Inversiones...")
    
    # Load environment variables
    load_dotenv()
    
    # Setup logging
    setup_logger()
    
    # Initialize application
    window = MainWindow()
    window.show()
    
    print("Interfaz gráfica cargada correctamente")
    
    # Ejecutar loop principal
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()