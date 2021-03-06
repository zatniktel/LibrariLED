# This widget is the interface to select the zone of the Library to change

from PySide2.QtWidgets import QWidget, QGridLayout, QPushButton
from ZoneWidget import Zone
from DialogColorPicker import DialogColorPicker


class Library(QWidget):

    def __init__(self):
        super().__init__()
        self.Zones1 = []
        self.Zones2 = []
        self.MainLayout = QGridLayout()
        self.setLayout(self.MainLayout)
        self.DialogColorPicker = DialogColorPicker()

        # Create a list of Dictionnary to manage the Library manually
        zoneconf1 = []
        zoneconf2 = []

        zoneconf1.append({"offset1": 0, "lengthled": 20})
        zoneconf1.append({"offset1": 20, "lengthled": 10})
        zoneconf1.append({"offset1": 30, "lengthled": 10})
        zoneconf1.append({"offset1": 40, "lengthled": 10})
        zoneconf1.append({"offset1": 50, "lengthled": 10})

        zoneconf2.append({"offset1": 60, "lengthled": 20})
        zoneconf2.append({"offset1": 80, "lengthled": 10})
        zoneconf2.append({"offset1": 90, "lengthled": 10})
        zoneconf2.append({"offset1": 100, "lengthled": 10})
        zoneconf2.append({"offset1": 110, "lengthled": 10})

        # Create the specific push button for each Zone of the Library


        offset2 = 0

        for zone in zoneconf1:
            offset2 = offset2 + zone["lengthled"]

        print(offset2)

        for zone in zoneconf1:
            self.Zones1.append(Zone(zone["offset1"], zone["lengthled"], offset2))
            self.Zones1[-1].setStyleSheet("QPushButton {background-color:black}")
            self.Zones1[-1].clickeddata.connect(self.DialogColorPicker.showFullScreen)

        offset2 = 0

        for zone in zoneconf2:
            offset2 = offset2 + zone["lengthled"]

        print(offset2)

        for zone in zoneconf2:
            self.Zones2.append(Zone(zone["offset1"], zone["lengthled"], offset2))
            self.Zones2[-1].setStyleSheet("QPushButton {background-color:black}")
            self.Zones2[-1].clickeddata.connect(self.DialogColorPicker.showFullScreen)

        # Create the interface
        i = 0
        for zone in self.Zones1:
            self.MainLayout.addWidget(zone, i, 1)
            i = i + 1

        i = 0
        for zone in self.Zones2:
            self.MainLayout.addWidget(zone, i, 2)
            i = i + 1
