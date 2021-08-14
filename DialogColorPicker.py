# This class is the window to choose the color of the LEDs
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QDialog, QVBoxLayout, QPushButton
from PySide2.QtGui import QMouseEvent
from ColorPicker import ColorPicker
from ZoneWidget import Zone

import board
import neopixel

class DialogColorPicker(QDialog):

    def __init__(self):
        super().__init__()
        self.cp_ColorPicker = ColorPicker(200)
        self.qpb_Validate = QPushButton("CLOSE")
        self.qvbl_MainLayout = QVBoxLayout()
        self.setLayout(self.qvbl_MainLayout)

        self.zone = Zone(0, 1, 0)

        # Create the neopixel strip object
        self.pixels = neopixel.NeoPixel(board.D12, 150)

        # Construct the interface
        self.qvbl_MainLayout.addWidget(self.cp_ColorPicker)
        self.qvbl_MainLayout.addWidget(self.qpb_Validate)

        self.qpb_Validate.clicked.connect(self.close)

    def mousePressEvent(self, mouseevent: QMouseEvent) -> None:
        super().mousePressEvent(mouseevent)

        # Get the color from the color picker
        color = self.cp_ColorPicker.get_color()

        # Update the color of the Push Button
        style = "Background-color: " + color.name()
        self.qpb_Validate.setStyleSheet(style)
        self.zone.setStyleSheet(style)

        # Update the Color of the LED
        print("offset1 = ", self.zone.get_offset1())
        print("ledlength = ", self.zone.get_ledlength())
        for i in range(self.zone.get_offset1(), self.zone.get_ledlength() + self.zone.get_offset1()):
             self.pixels[i] = (color.red(), color.green(), color.blue())
             print("i = ", i)

        print("offset2 = ", self.zone.get_offset2())
        for i in range(self.zone.get_offset2(), self.zone.get_ledlength() + self.zone.get_offset2()):
             self.pixels[i] = (color.red(), color.green(), color.blue())

    @Slot(int)
    def showFullScreen(self, dummy):
        # super().showFullScreen()
        self.show()
        self.zone = self.sender()
        print(type(self.sender()))
        print(self.sender().get_offset1())
        print(self.sender().get_ledlength())
        print(self.sender().get_offset2())
        self.qpb_Validate.setStyleSheet(self.sender().styleSheet())
