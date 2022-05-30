from PyQt5.QtWidgets import QApplication, QPushButton, QTableWidget, QLabel

class Variables():
    def __init__(self, main):
        self.screen_rect = QApplication.desktop().screen().rect()

        self.window_width = int(self.screen_rect.width() * 0.30)
        self.window_height = int(self.screen_rect.height() * 0.75)

        # Start/stop flag 
        self.Start = False

        # Time counter variables
        self.seconds = 0
        self.minutes = 0
        self.millisecs = 0
        
        # Helper variables
        self._colCounter = 0
        self.prev_seconds = 0
        self.prev_minutes = 0
        self.prev_millisecs = 0

        # Set relative sizes of the button widgets
        self.buttonwidth = int(self.window_width * 0.55)
        self.buttonheight = int(self.window_height * 0.07)

        # Widgets class instances
        self.counterlabel = QLabel(main)
        self.startbutton = QPushButton("START", main)
        self.resetbutton = QPushButton("RESET", main)
        self.splitbutton = QPushButton("SPLIT (Lap)", main)
        self.datatable = QTableWidget(main)
