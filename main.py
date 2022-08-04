import sys
import threading
import HomeAssistant.ProcessVoiceCommand as ProcessVoiceCommand
from PySide6 import QtGui, QtCore, QtWidgets
import os

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
os.environ["PATH"] = os.path.dirname(__file__) + os.pathsep + os.environ["PATH"]

import mpv
import HomeAssistant.PlayYt as PlayYt

class NowPlayingWrapper:
    def __init__(self):
        self.nowPlaying = ''

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.nowPlaying = NowPlayingWrapper()
        self.player = mpv.MPV(ytdl=True, video=False)
        self.button = QtWidgets.QPushButton('Say Something')
        self.label = QtWidgets.QLabel('')

        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.button.setMaximumWidth(150)
        self.button.setMinimumWidth(150)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)
        self.button.clicked.connect(self.SayingSomething)
    
    @QtCore.Slot()
    def SayingSomething(self):
        self.label.setText('Listening...')
        self.button.setDisabled(True)
        thread = threading.Thread(target=ProcessVoiceCommand.TakeVoiceCommand, args=(self.nowPlaying, self, self.player, ))
        
        thread.start()
    
    def closeEvent(self, event):
        self.player.stop()

app = QtWidgets.QApplication([])
window = MainWindow()

window.resize(640, 480)
window.setWindowTitle('Home Assitant')
window.show()

sys.exit(app.exec())