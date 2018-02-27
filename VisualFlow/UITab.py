from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

# class UITab(QWidget):
#     def __init__(self):
#         super(UITab, self).__init__()
#
#         self.layout = QHBoxLayout(self)
#
#         self.pushButton1 = QPushButton("PyQt5 button")
#         self.layout.addWidget(self.pushButton1)
#         self.setLayout(self.layout)


class UITab(QTableWidget):
    def __init__(self, r, c):
        super().__init__(r, c)
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)
        #self.verticalHeader().setDefaultSectionSize(500)