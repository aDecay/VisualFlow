from PyQt5.QtWidgets import *

class BaseWidget(QWidget):
    def __init__(self):
        super(BaseWidget, self).__init__()

        BaseWidget.layout = QHBoxLayout(self)

        self.tabs = QTabWidget()

        self.tabs.addTab(self.tab1, "UI")
        self.tabs.addTab(self.tab2, "Code")

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)




