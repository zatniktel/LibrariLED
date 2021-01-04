# Widget to manage the main window of the project

from PySide2.QtWidgets import QMainWindow, QPushButton
from LibraryWidget import Library


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ColorPicker = Library()
        self.setCentralWidget(self.ColorPicker)
