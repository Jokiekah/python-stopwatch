#!/usr/bin/env python3

# Import all necessary packages and classes
import sys

from screeninfo import get_monitors
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Main class for setting up the GUI window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Python Stopwatch")

        # Window's positioning on the actual screen
        self.window_width = int(get_monitors()[0].width * 0.30)
        self.window_height = int(get_monitors()[0].height * 0.75)

        self.setFixedSize(self.window_width, self.window_height)
        self.move(500, 150)

        # Important variable declarations
        self.seconds = 0
        self.minutes = 0
        self.hours = 0

        # Start/stop flag
        self.Start = False
        
       # Draw all the defined user interfaces
        self.uiComponents()

    def uiComponents(self): 
        self.counterUI()
        self.startUI()

    def showCounter(self):
        return 

    def counterUI(self):
        counter = QLabel(self)
        counter.setFrameStyle(QFrame.Panel | QFrame.Plain)
        counter.setGeometry(75, 100, int(self.window_width * 0.75), int(self.window_height * 0.10))
        counter.setText(f"00h : 00m : 00s")
        counter.setFont(QFont('Arial', 30, QFont.Bold))
        counter.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

    def startUI(self):
        self.startbutton = QPushButton("Start", self)
        self.startbutton.setGeometry(75, 250, 300, 50)
        self.startbutton.pressed.connect(self._startEvent)

    def _startEvent(self):
        if self.startbutton.text() == 'Pause':
            self.startbutton.setText('Resume')
            self.Start = False
        else:
            self.Start = True
            self.startbutton.setText('Pause')
            

# Main function for the stopwatch app
def stopwatch():
    App = QApplication([])
    window = MainWindow()
    window.show()

    sys.exit(App.exec())

if __name__ == "__main__":
    stopwatch()
