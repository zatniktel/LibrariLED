# This class manage a Pushbutton for a Zone of the Library

from PySide2.QtWidgets import QPushButton


class Zone(QPushButton):

    def __init__(self, offset1, ledlength, offset2=-1):
        super().__init__()
        self.offset1 = offset1
        self.offset2 = offset2
        self.ledlength = ledlength