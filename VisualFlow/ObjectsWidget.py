from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class ObjectsWidget(QWidget):
    def __init__(self,baseWidget):
        super(ObjectsWidget, self).__init__()
        self.baseWidget = baseWidget

        self.Pb = QPushButton("누르면 옆으로 길어져요!")
        self.Pb.clicked.connect(self.btn_click)

        self.imageLabel = QLabel()
        self.imageLabel2 = QLabel()
        self.image = QImage("test.jpg")
        self.image2 = QImage("test2.jpg")
        self.imageLabel.setPixmap(QPixmap.fromImage(self.image))
        self.imageLabel2.setPixmap(QPixmap.fromImage(self.image2))

        self.v_box = QVBoxLayout(self)
        self.v_box.addWidget(self.Pb)
        self.v_box.addWidget(self.imageLabel)
        self.v_box.addWidget(self.imageLabel2)
        self.v_box.setAlignment(Qt.AlignTop)

    def btn_click(self):
        self.baseWidget.tab1.insertColumn(0)