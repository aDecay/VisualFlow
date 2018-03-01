from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Soksung(QWidget):
    def __init__(self):
        super(Soksung, self).__init__()

        self.table = QTableWidget(10,2)
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)
        dictionary = {1: ['a', 'b', 'c'], 2: ['d', 'e', 'f'], 3:[]}
        dictionary2 = {1: 'a', 2: 'f', 3: 'asdf'}

        choice = 'a' or 'f'
        for i in dictionary.keys():
            if dictionary[i] == []:
                le = QLineEdit(dictionary2[i])
                self.layout.addWidget(le)
            else:
                cb = QComboBox()
                for k in dictionary[i]:
                    cb.addItem(k)
                    if k == dictionary2[i]:
                        cb.setCurrentIndex(dictionary[i].index(k))
                    self.layout.addWidget(cb)

        self.setLayout(self.layout)




# class Soksung(QTableWidget):
#     def __init__(self, r, c):
#         super().__init__(r, c)
#         self.verticalHeader().setVisible(False)
#
#         self.setItem(0, 0, QTableWidgetItem(dictionary.values()))
