# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PySide2.QtWidgets import QApplication, QMainWindow
import sys
from ColorPicker import ColorPicker
from MainWindow import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    qmw_MainWindow = MainWindow()
    qmw_MainWindow.show()
    app.exec_()
