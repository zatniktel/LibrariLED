# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PySide2.QtWidgets import QMessageBox, QLabel
from PySide2.QtGui import QPainter, QColor, QMouseEvent, QPixmap, QImage
from PySide2.QtCore import Qt
import numpy as np


class ColorPicker(QLabel):

    def __init__(self, radius):
        super().__init__()
        self.setFixedSize(2*radius, 2*radius)
        self.qc_Color = QColor(0, 0, 0, 255)

        self.radius = radius

        self.qpm_Image = QPixmap()

        #Create the image
        qi_image = QImage(self.width(), self.height(), QImage.Format_RGB32)
        for i in range(self.width()):
            for j in range(self.height()):
                color = QColor(0, 0, 0, 255)
                h = (np.arctan2(i - self.radius, j - self.radius) + np.pi) / (2. * np.pi)
                s = np.sqrt(np.power(i - self.radius, 2) + np.power(j - self.radius, 2)) / self.radius
                v = 1.0
                if s < 1.0:
                    color.setHsvF(h, s, v, 1.0)
                qi_image.setPixelColor(i, j, color)

        self.qpm_Image.convertFromImage(qi_image)
        self.setPixmap(self.qpm_Image)

        # self.showFullScreen()

    def mousePressEvent(self, mouseevent: QMouseEvent):
        super().mouseMoveEvent(mouseevent)

        if mouseevent.button() == Qt.LeftButton:
            x = mouseevent.x()
            y = mouseevent.y()

            h = (np.arctan2(x - self.radius, y - self.radius) + np.pi) / (2. * np.pi)
            s = np.sqrt(np.power(x - self.radius, 2) + np.power(y - self.radius, 2)) / self.radius
            v = 1.0
            if s < 1.0:
                self.qc_Color.setHsvF(h, s, v, 1.0)

            QMessageBox.warning(self, "Color", "Value(" + str(self.qc_Color.toRgb().red()) + ", " + str(self.qc_Color.toRgb().green()) + ", " + str(self.qc_Color.toRgb().blue()) + ")")

