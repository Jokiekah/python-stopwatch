from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
from datetime import timedelta

class HelperFunctions():
    "Class for initialization of all necessary helper functions"
    def __init__(self, variables):
        self.variables = variables

    def _formatCounter(self):
        """Function for minutes : seconds : millisecs formatting of data"""
        minutes = '0' + str(self.variables.minutes) if self.variables.minutes < 10 else str(self.variables.minutes)
        seconds = '0' + str(self.variables.seconds) if self.variables.seconds < 10 else str(self.variables.seconds)
        millisecs = '0' + str(self.variables.millisecs) if self.variables.millisecs < 10 else str(self.variables.millisecs)
    
        text = f"{minutes}m : {seconds}s . {millisecs[0:2]}"
        return text

    def _startEvent(self):
        """Function event handler for the startUI function."""
        if self.variables.startbutton.text() == "STOP":
            self.variables.startbutton.setText("RESUME")
            self.variables.Start = False
        else:
            self.variables.Start = True
            self.variables.startbutton.setText('STOP')

    def _resetEvent(self):
        """Function event handler for the resetUI function."""
        self.variables.Start = False
        self.variables.seconds = 0
        self.variables.minutes = 0
        self.variables.millisecs = 0
        self.variables._colCounter = 0

        self.variables.datatable.clearContents()

        self.variables.counterlabel.setText("00m : 00s . 00")
        self.variables.startbutton.setText("START")


    def _splitEvent(self):
        """Function event handler for the splitUI funtion."""
        if self.variables.Start:
            self.variables.datatable.setItem(self.variables._colCounter, 0, QTableWidgetItem(str(self.variables._colCounter + 1)))
            self.variables.datatable.setItem(self.variables._colCounter, 1, QTableWidgetItem(f"{self._formatCounter()}"))

            # Compute time difference between the current and the previous
            if self.variables._colCounter == 0:
                self.variables.datatable.setItem(self.variables._colCounter, 2, QTableWidgetItem(f"{self._formatCounter()}"))
            else:
                # Computer the difference between previous time and current time
                time_length = str(timedelta(minutes=int(self.variables.minutes), seconds=int(self.variables.seconds), milliseconds=int(self.variables.millisecs)) - timedelta(minutes=int(self.variables.prev_minutes), seconds=int(self.variables.prev_seconds), milliseconds=int(self.variables.prev_millisecs)))
                final_result = f"{time_length[2:4]}m : {time_length[5:7]}s . {time_length[8:10]}"
                # if time_length is not None and time_length.text() != '':
                self.variables.datatable.setItem(self.variables._colCounter, 2, QTableWidgetItem(f"{final_result}"))

            self.variables._colCounter += 1

        # Get the previous time record
        self.variables.prev_minutes = self.variables.minutes
        self.variables.prev_seconds = self.variables.seconds
        self.variables.prev_millisecs = self.variables.millisecs
