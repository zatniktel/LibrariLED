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

        zoneconf1.append({"pin": 21, "offset1": 0, "lengthled": 11})
        zoneconf1.append({"pin": 21, "offset1": 12, "lengthled": 7})
        zoneconf1.append({"pin": 21, "offset1": 19, "lengthled": 10})
        zoneconf1.append({"pin": 21, "offset1": 29, "lengthled": 9})
        zoneconf1.append({"pin": 21, "offset1": 38, "lengthled": 16})

        zoneconf2.append({"pin": 12, "offset1": 110, "lengthled": 20})
        zoneconf2.append({"pin": 12, "offset1": 130, "lengthled": 10})
        zoneconf2.append({"pin": 12, "offset1": 140, "lengthled": 10})
        zoneconf2.append({"pin": 12, "offset1": 150, "lengthled": 10})
        zoneconf2.append({"pin": 12, "offset1": 160, "lengthled": 10})

        # Create the specific push button for each Zone of the Library

        offset2 = 0

        for zone in zoneconf1:
            offset2 = offset2 + zone["lengthled"]

        for zone in zoneconf1:
            self.Zones1.append(Zone(zone["pin"], zone["offset1"], zone["lengthled"], 0))
            self.Zones1[-1].setStyleSheet("QPushButton {background-color:black}")
            self.Zones1[-1].clickeddata.connect(self.DialogColorPicker.showFullScreen)

        zoneconf1.reverse()

        i = -1

        for zone in zoneconf1:
            self.Zones1[i].offset2 = offset2
            offset2 = offset2 + self.Zones1[i].get_ledlength()
            i = i - 1

        for zone in self.Zones1:
            print("Zone")

        # The second part of the Library

        offset2 = 0

        for zone in zoneconf2:
            offset2 = offset2 + zone["lengthled"]

        for zone in zoneconf2:
            self.Zones2.append(Zone(zone["pin"], ["offset1"], zone["lengthled"], offset2))
            self.Zones2[-1].setStyleSheet("QPushButton {background-color:black}")
            self.Zones2[-1].clickeddata.connect(self.DialogColorPicker.showFullScreen)

        zoneconf2.reverse()

        i = -1

        for zone in zoneconf2:
            self.Zones2[i].offset2 = offset2
            offset2 = offset2 + self.Zones2[i].get_ledlength()
            i = i - 1

        for zone in self.Zones2:
            print("Zone")

        # Create the interface
        i = 0
        for zone in self.Zones1:
            self.MainLayout.addWidget(zone, i, 1)
            i = i + 1

        i = 0
        for zone in self.Zones2:
            self.MainLayout.addWidget(zone, i, 2)
            i = i + 1
