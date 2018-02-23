import sys

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QDockWidget, QLabel, QFrame
from PyQt5.QtWidgets import QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QAction, qApp
from PyQt5.QtCore import *

import BaseWidget
import ObjectsWidget
from PyQt5.uic.properties import QtWidgets


class VisualFlow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.form_widget = BaseWidget.BaseWidget()
        self.setCentralWidget(self.form_widget)

        self.init_ui()

    def init_ui(self):
        self.init_dock()
        bar = self.menuBar()
        file = bar.addMenu('File')
        edit = bar.addMenu('Edit')
        options = bar.addMenu('Options')
        window = bar.addMenu('Window')
        help = bar.addMenu('Help')

        new_action = QAction('&Clear', self)
        new_action.setShortcut('Ctrl+N')

        save_action = QAction('&Save', self)
        save_action.setShortcut('Ctrl+S')

        open_action = QAction('&Open', self)

        quit_action = QAction('&Quit', self)

        edit_action = QAction('&Edit',self)

        options_action = QAction('&Options', self)

        window_action = QAction('&Window', self)

        help_action = QAction('&Help', self)

        file.addAction(new_action)
        file.addAction(save_action)
        file.addAction(open_action)
        file.addAction(quit_action)

        edit.addAction(edit_action)

        options.addAction(options_action)

        window.addAction(window_action)

        help.addAction(help_action)

        quit_action.triggered.connect(self.quit_trigger)
        file.triggered.connect(self.respond)

        self.showMaximized()

    def init_dock(self):
        self.objects = QDockWidget('Objects')

        self.objects.setWidget(ObjectsWidget.ObjectsWidget())

        self.properties = QDockWidget('Properties')

        self.addDockWidget(Qt.LeftDockWidgetArea, self.objects)
        self.addDockWidget(Qt.RightDockWidgetArea, self.properties)

    def quit_trigger(self):
        qApp.quit()

    def respond(self, q):
        signal = q.text()

        if signal == '&Clear':
            self.form_widget.clear_text()
        elif signal == '&Open':
            self.form_widget.open_text()
        elif signal == '&Save':
            self.form_widget.save_text()

app = QApplication(sys.argv)
visualFlow = VisualFlow()
sys.exit(app.exec_())