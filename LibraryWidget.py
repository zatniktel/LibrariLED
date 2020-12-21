# This widget is the interface to select the zone of the Library to change

from PySide2.QtWidgets import QWidget, QPushButton, QGridLayout


class Library(QWidget):

    def __init__(self):
        super().__init__()
        self.Zone = []
        self.MainLayout = QGridLayout()
        self.setLayout(self.MainLayout)

        for i in range(10):
            self.Zone.append(QPushButton("Toto"))
            self.Zone[i].setStyleSheet("QPushButton {background-color:black}")

        for i in range(5):
            self.MainLayout.addWidget(self.Zone[i], i, 1)

        for i in range(5):
            self.MainLayout.addWidget(self.Zone[5+i], i, 2)
