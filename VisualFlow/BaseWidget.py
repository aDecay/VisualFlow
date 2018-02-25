from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import UITab

class BaseWidget(QWidget):
    def __init__(self):
        super(BaseWidget, self).__init__()

        self.layout = QHBoxLayout(self)

        self.tabs = QTabWidget()
        self.tab1 = UITab.UITab(1,10)
        self.tab2 = QLabel("Hello World!")

        self.tabs.setTabPosition(QTabWidget.South)
        self.tabs.addTab(self.tab1, 'UI')
        self.tabs.addTab(self.tab2, 'Code')

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)