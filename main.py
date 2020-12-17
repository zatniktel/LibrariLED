# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PySide2.QtWidgets import QApplication
import sys
from ColorPicker import ColorPicker

if __name__ == '__main__':
    app = QApplication(sys.argv)
    cp_ColorPicker = ColorPicker(200)
    cp_ColorPicker.show()
    app.exec_()
