# Import all necessary packages and classes
import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QMainWindow

# Main class for setting up the GUI window
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Python Stopwatch")
        self.setGeometry(100, 100, 500, 500)

        self.show()

App = QApplication(sys.argv)

window = MainWindow()

sys.exit(App.exec())
