"""
Qt for Python: Sending Notifications to a Dashboard
Author: Naeem Khoshnevis (Jan 19, 2020)
www.linkedin.com/in/datahacker
Last update: Jan 20, 2020


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


class Notification:
    """
    The Notificaiton object contains:
    instance id (my_id) and time of construction (time_val)
    """
    def __init__(self, my_id, time_val):
        self.my_id = my_id
        self.time_val = time_val

def singleton(cls):
    """ decorator function to implement singleton design pattern. See PEP318."""
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class MySignal(QObject):
    """
    Signal Class which includes a signal as class attribute.
    """
    object_signal = Signal(Notification)

class MyThread(QThread):
    """
    This class contains a signal and run method.
    An object of the signal is activated by .start() method
    and sends the results using MySignal Class instance.
    """
    def __init__(self, val):
        super().__init__()
        self.object_signal = MySignal().object_signal
        self.val = val

    def run(self):
        """
        Function is called when Thread is .strat().
        """
        for _ in range(self.val):
            my_id = MyObject().send_id()
            time_val = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.object_signal.emit(Notification(my_id, time_val))
            # Defining a ranodm sleep time (0-10) seconds.
            sleep_time = random.random()*10
            time.sleep(sleep_time)

class MyObject:
    """A class for generating an object"""
    def __init__(self):
        num = random.randint(1000, 2000)
        self.my_id = str(num)

    def send_id(self):
        """Function to return my_id value of the class."""
        return self.my_id

class InputWindow(QWidget):
    """
    Class for second GUI window.
    """
    def __init__(self):
        super().__init__()
        self.initialize()

    def initialize(self):
        """ Initializes the InputWindow Class """

        self.num_object = QLineEdit()
        form = QFormLayout()
        form.addRow(QLabel("Number of Objects: "), self.num_object)

        start_button = QPushButton("Start")
        close_button = QPushButton("Close")

        start_button.clicked.connect(self.send_clicked)
        close_button.clicked.connect(self.close)

        layout = QHBoxLayout()
        layout.addWidget(start_button)
        layout.addWidget(close_button)

        form.addRow(layout)

        self.setLayout(form)
        self.setWindowTitle("Input Parameters")
        self.setMinimumWidth(350)

    def send_clicked(self):
        """ Function to start and execute a thread."""
        self.mythread = MyThread(int(self.num_object.text()))
        self.mythread.start()


class Dashboard(QWidget):
    """
    Main GUI window (Dashboard).
    """
    def __init__(self):
        super().__init__()
        self.input_param = InputWindow()
        self.edit = QTextEdit()
        button = QPushButton("Get Input")
        button.clicked.connect(self.get_input)
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(button)
        self.setLayout(layout)
        self.setMinimumWidth(450)
        self.my_signal = MySignal()
        self.object_signal = self.my_signal.object_signal
        self.object_signal.connect(self.show_it)
        self.setWindowTitle("Dashboard")
        self.show()


    def get_input(self):
        """ Function to display input_param window."""
        self.input_param.show()

    def show_it(self, nval=None):
        """ Function to update incoming notification on the dashboard """
        my_text = f"{nval.time_val}:  Record number  {nval.my_id}  is generated."
        self.edit.setText(self.edit.toPlainText()+"\n"+my_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Dashboard()
    sys.exit(app.exec_())
