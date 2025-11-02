from PyQt6.QtCore import QObject, pyqtSignal


class SignalBus(QObject):
    switchToSampleCard = pyqtSignal(str, int)
    supportSignal = pyqtSignal()


signalBus = SignalBus()
