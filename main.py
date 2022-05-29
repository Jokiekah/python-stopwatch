# Import all necessary packages and classes
import sys

from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QLabel,
    QFrame,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
)
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont

# Main class for setting up the GUI window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Python Stopwatch")

        # Window's positioning on the actual screen
        screen_rect = QApplication.desktop().screen().rect()

        self.window_width = int(screen_rect.width() * 0.30)
        self.window_height = int(screen_rect.height() * 0.75)

        self.setFixedSize(self.window_width, self.window_height)
        self.move(QApplication.desktop().screen().rect().center() - self.rect().center())

        # Important variable declarations
        self.counter = 0
        self.seconds = '00'
        self.minutes = '00'
        self.millisec = '00'

        # Column data counter
        self.col_counter = 0

        # Start/stop flag
        self.Start = False
        
        # Main timer counter object instance
        timer = QTimer(self)
        timer.timeout.connect(self.showCounter)
        timer.start(10)

        # Draw all the defined user interfaces
        self.uiCompLayout()