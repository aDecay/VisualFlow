from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class ObjectsWidget(QWidget):
    def __init__(self):
        super(ObjectsWidget, self).__init__()

        self.imageLabel = QLabel()
        self.imageLabel2 = QLabel()
        self.image = QImage("test.jpg")
        self.image2 = QImage("test2.jpg")
        self.imageLabel.setPixmap(QPixmap.fromImage(self.image))
        self.imageLabel2.setPixmap(QPixmap.fromImage(self.image2))

        self.v_box = QVBoxLayout(self)
        self.v_box.addWidget(self.imageLabel)
        self.v_box.addWidget(self.imageLabel2)
        self.v_box.setAlignment(Qt.AlignTop)
