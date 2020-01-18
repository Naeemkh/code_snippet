"""
Qt for Python: Sending Notifications to a Dashboard
Author: Naeem Khoshnevis (Jan 18, 2020)
www.linkedin.com/in/datahacker

Last update: Jan 18, 2020

Description:
PySide2==5.14.0

"""
import sys
import time
import random

from PySide2.QtWidgets import (QApplication, QWidget,
                               QLineEdit, QTextEdit, QLabel, QPushButton,
                               QFormLayout, QHBoxLayout, QVBoxLayout)

from PySide2.QtCore import Signal, QObject, QThread

class Dashboard(QWidget):
    """
    Main GUI window (Dashboard).
    """
    def __init__(self):
        super().__init__()
        self.edit = QTextEdit()
        button = QPushButton("Get Input")
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(button)
        self.setLayout(layout)
        self.setMinimumWidth(450)
        self.setWindowTitle("Dashboard")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Dashboard()
    sys.exit(app.exec_())
