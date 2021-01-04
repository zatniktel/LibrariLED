# This class manage a Pushbutton for a Zone of the Library

from PySide2.QtWidgets import QPushButton
from PySide2.QtCore import Signal, Slot

class Zone(QPushButton):

    clickeddata = Signal(int)

    def __init__(self, offset1, ledlength, offset2=-1):
        super().__init__()
        self.offset1 = offset1
        self.offset2 = offset2
        self.ledlength = ledlength

        self.clicked.connect(self.senddata)

    def get_offset1(self):
        return self.offset1

    def get_offset2(self):
        return self.offset2

    def get_ledlength(self):
        return self.ledlength

    @Slot()
    def senddata(self):
        self.clickeddata.emit(0)
