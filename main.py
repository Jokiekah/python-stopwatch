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
    def _startEvent(self):
        if self.startbutton.text() == "STOP":
            self.startbutton.setText("RESUME")
            self.Start = False
        else:
            self.Start = True
            self.startbutton.setText('STOP')

    def resetUI(self):
        self.resetbutton = QPushButton("RESET", self)
        # self.resetbutton.setGeometry(75, 310, 300, 50)
        self.resetbutton.setFixedSize(int(self.window_width * 0.55), int(self.window_height * 0.07))
        self.resetbutton.move(int(self.rect().width() / 2 - self.startbutton.rect().width() / 2), 300)
        self.resetbutton.pressed.connect(self._resetEvent)

    def _resetEvent(self):
        self.Start = False
        self.counter = 0
        self.seconds = '00'
        self.minutes = '00'
        self.millisec = '00'
        self.col_counter = 0

        self.datatable.clearContents()

        self.counterlabel.setText(str(self.counter))
        self.startbutton.setText("Start")
    def splitUI(self):
        self.splitbutton = QPushButton("SPLIT (Lap)", self)
        # self.resetbutton.setGeometry(75, 310, 300, 50)
        self.splitbutton.setFixedSize(int(self.window_width * 0.55), int(self.window_height * 0.07))
        self.splitbutton.move(int(self.rect().width() / 2 - self.splitbutton.rect().width() / 2), 370)
        self.splitbutton.pressed.connect(self._splitEvent)

    def _splitEvent(self):
        if self.Start:
            self.datatable.setItem(self.col_counter, 0, QTableWidgetItem(str(self.col_counter + 1)))
            self.datatable.setItem(self.col_counter, 1, QTableWidgetItem(f"{self.minutes} : {self.seconds} : {self.millisec}"))

            # Compute time difference between the current and the previous
            if self.col_counter == 0:
                self.datatable.setItem(self.col_counter, 2, QTableWidgetItem(f"{self.minutes} : {self.seconds} : {self.millisec}"))
            else:
                time_length = self.datatable.item(self.col_counter - 1, 1)
                if time_length is not None and time_length.text() != '':
                    print(time_length.text())
                    self.datatable.setItem(self.col_counter, 2, QTableWidgetItem(f"{self.col_counter}"))

            self.col_counter += 1
            
    def tableUI(self):
        self.datatable = QTableWidget(self)
        self.datatable.setRowCount(10)
        self.datatable.setColumnCount(3)
        self.datatable.setFixedSize(int(self.window_width * 0.75), 250)

        # int(self.window_height * 0.10)
        self.datatable.move(int(self.rect().width() / 2 - self.counterlabel.rect().width() / 2), 440)

        self.datatable.verticalHeader().setVisible(False)
        self.datatable.setHorizontalHeaderLabels(["Split", "Time", "Length"])
        self.datatable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.datatable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

        # Make the first column different
        self.datatable.horizontalHeader().setSectionsClickable

        # make the table read-only
        self.datatable.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

# Main function for the stopwatch app
def stopwatch():
    App = QApplication([])
    window = MainWindow()
    window.show()

    sys.exit(App.exec())

if __name__ == "__main__":
    stopwatch()
