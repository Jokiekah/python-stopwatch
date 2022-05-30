
# Import all necessary packages and classes
import sys

from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QFrame,
    QTableWidget,
    QHeaderView,
    QDesktopWidget
)
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont

from helpers import HelperFunctions
from variables import Variables

# Main class for setting up the GUI window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize all important variables
        self.variables = Variables(self)

        # Initialize all helper functions imports
        self.helpers = HelperFunctions(self.variables)

       # Set the windows main title
        self.setWindowTitle("Python Stopwatch")

        # Window's positioning on the actual screen
        self.setFixedSize(self.variables.window_width, self.variables.window_height)
        self.move(QApplication.desktop().screen().rect().center() - self.rect().center())

        # Main timer counter object instance
        timer = QTimer(self)
        timer.timeout.connect(self.showCounter)
        timer.start(1)

        # Draw all the defined user interfaces
        self.uiCompLayout()

    def uiCompLayout(self): 
        self.counterUI()
        self.startUI()
        self.resetUI()
        self.splitUI()
        self.tableUI()
        
        

    def showCounter(self):
        if self.variables.Start:
            # Compute for the minute, seconds, and millisecs
            if self.variables.millisecs >= 999:
                self.variables.millisecs = 0

                if self.variables.seconds >= 59:
                    self.variables.seconds = 0

                    if self.variables.minutes >= 59:
                        self.helpers._resetEvent()
                        return
                    else:
                        self.variables.minutes += 1
                else:
                    self.variables.seconds += 1

            self.variables.millisecs += 1

        # Format and merge the minute, second, and millisecs values
        self.variables.counterlabel.setText('<h2>' + self.helpers._formatCounter() + '</h2>')

    def counterUI(self):
        self.variables.counterlabel.setFrameStyle(QFrame.Panel | QFrame.Plain)
        self.variables.counterlabel.setFixedSize(int(self.variables.window_width * 0.75), int(self.variables.window_height * 0.10))
        self.variables.counterlabel.move(int(self.rect().width() / 2 - self.variables.counterlabel.rect().width() / 2), int(self.variables.window_height * 0.13))

        if self.variables.screen_rect.width() == 1024 and self.variables.screen_rect.height() == 768:
            self.variables.counterlabel.setFont(QFont('Arial', 15, QFont.Bold))
        else:
            self.variables.counterlabel.setFont(QFont('Arial', 20, QFont.Bold))

        self.variables.counterlabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    def startUI(self):
        self.variables.startbutton.setFixedSize(self.variables.buttonwidth, self.variables.buttonheight)
        self.variables.startbutton.move(int(self.rect().width() / 2 - self.variables.startbutton.rect().width() / 2), int(self.variables.counterlabel.y() + self.variables.counterlabel.height() + (self.variables.window_height * 0.05)))
        self.variables.startbutton.pressed.connect(self.helpers._startEvent)

    def splitUI(self):
        self.variables.splitbutton.setFixedSize(self.variables.buttonwidth, self.variables.buttonheight)
        # self.variables.splitbutton.move(int(self.rect().width() / 2 - self.variables.splitbutton.rect().width() / 2), 370)
        self.variables.splitbutton.move(int(self.rect().width() / 2 - self.variables.resetbutton.rect().width() / 2), int(self.variables.resetbutton.y() + self.variables.resetbutton.height() + (self.variables.window_height * 0.021)))
        self.variables.splitbutton.pressed.connect(self.helpers._splitEvent)
    
    def resetUI(self):
        self.variables.resetbutton.setFixedSize(self.variables.buttonwidth, self.variables.buttonheight)
        # self.variables.resetbutton.move(int(self.rect().width() / 2 - self.variables.startbutton.rect().width() / 2), 300)
        self.variables.resetbutton.move(int(self.rect().width() / 2 - self.variables.resetbutton.rect().width() / 2), int(self.variables.startbutton.y() + self.variables.startbutton.height() + (self.variables.window_height * 0.021)))
        self.variables.resetbutton.pressed.connect(self.helpers._resetEvent)

    def tableUI(self):
        self.variables.datatable.setRowCount(10)
        self.variables.datatable.setColumnCount(3)

        if self.variables.screen_rect.height() >= 1080:
            self.variables.datatable.setFixedSize(int(self.variables.window_width * 0.75), 263)
        elif self.variables.screen_rect.height() >= 720:
            self.variables.datatable.setFixedSize(int(self.variables.window_width * 0.75), 200)

        # Minimize table data font on smaller screens
        if self.variables.screen_rect.width() == 1024 and self.variables.screen_rect.height() == 768:
            self.variables.datatable.setFont(QFont('Arial', 8, QFont.Normal))
 
        # int(self.window_height * 0.10)
        # self.variables.datatable.move(int(self.rect().width() / 2 - self.variables.counterlabel.rect().width() / 2), 440)
        self.variables.datatable.move(int(self.rect().width() / 2 - self.variables.counterlabel.rect().width() / 2), int(self.variables.splitbutton.y() + self.variables.splitbutton.height() + (self.variables.window_height * 0.021)))

        self.variables.datatable.verticalHeader().setVisible(False)
        self.variables.datatable.setHorizontalHeaderLabels(["Split", "Time", "Length"])
        self.variables.datatable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.variables.datatable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

        # make the table read-only
        self.variables.datatable.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

# Main function for the stopwatch app
def stopwatch():
    App = QApplication([])
    window = MainWindow()
    window.show()

    sys.exit(App.exec())

if __name__ == "__main__":
    stopwatch()
