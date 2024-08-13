# Entry point of the application.

from PySide6.QtWidgets import (QApplication, QMainWindow, QStyleFactory)
from main_window import Ui_MainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Set up UI

def main():
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("WindowsVista"))  # Set style
    window = MainWindow()
    window.show()
    sys.exit(app.exec())  # Start event loop

if __name__ == "__main__":
    main()


###### QStyleFactory ######
# Windows
# WindowsXP
# WindowsVista
# Fusion
# Macintosh
# Windows7
# Windows8
# Windows10
