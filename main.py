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
    def uiCompLayout(self): 
        self.counterUI()
        self.startUI()
        self.resetUI()
        self.splitUI()
        self.tableUI()

    def showCounter(self):
        if self.Start:
            self.counter += 1
            millisec = int((self.counter / 100 - int(self.counter /100)) * 100)

            if millisec < 10:
                self.millisec = '0' + str(millisec)
            else:
                self.millisec = str(millisec)

            # Set the seconds value
            if int(self.counter / 100) < 10:
                self.seconds = '0' + str(int(self.counter / 100))
            else:
                self.seconds = str(int(self.counter / 100))

                # Set the minutes value
                if self.counter / 100 == 60.0:
                    self.seconds = '00'
                    self.counter = 0
                    minutes = int(self.minutes) + 1
                    if minutes < 10:
                        self.minutes = '0' + str(minutes)
                    else:
                        self.minutes = str(minutes)

        # Merge the minute, second, and millisec values
        text = f"{self.minutes}m : {self.seconds}s : {self.millisec}"
        self.counterlabel.setText('<h2>' + text + '</h2>')

    def counterUI(self):
        self.counterlabel = QLabel(self)
        self.counterlabel.setFrameStyle(QFrame.Panel | QFrame.Plain)
        self.counterlabel.setFixedSize(int(self.window_width * 0.75), int(self.window_height * 0.10))
        self.counterlabel.move(int(self.rect().width() / 2 - self.counterlabel.rect().width() / 2), 100)
        # self.move(QApplication.desktop().screen().rect().center() - self.rect().center())
        self.counterlabel.setFont(QFont('Arial', 20, QFont.Bold))
        self.counterlabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    def startUI(self):
        self.startbutton = QPushButton("START", self)
        # self.startbutton.setGeometry(75, 250, 300, 50)
        self.startbutton.setFixedSize(int(self.window_width * 0.55), int(self.window_height * 0.07))
        self.startbutton.move(int(self.rect().width() / 2 - self.startbutton.rect().width() / 2), 230)
        self.startbutton.pressed.connect(self._startEvent)
