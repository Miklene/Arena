from PyQt5.Qt import QObject
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class SignalPhysiqueIncreased(QObject):

    signal = pyqtSignal()

    def __init__(self):
        super().__init__()

    def run(self):
        self.signal.emit()

class SignalPhysiqueDecreased(QObject):

    signal = pyqtSignal()

    def __init__(self):
        super().__init__()

    def run(self):
        self.signal.emit()
