from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys

class DoraemonApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Doraemon App')
        self.setGeometry(100, 100, 400, 500)
        
        # Crear etiqueta para la imagen
        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 300, 300)
        
        # Botón mágico
        self.magic_button = QPushButton('¡Bolsillo Mágico!', self)
        self.magic_button.setGeometry(150, 400, 100, 30)
        self.magic_button.clicked.connect(self.magic_action)
        
    def magic_action(self):
        self.statusBar().showMessage('¡Sacando un objeto del bolsillo mágico!')

def main():
    app = QApplication(sys.argv)
    window = DoraemonApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()