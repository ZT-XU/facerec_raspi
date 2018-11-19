from PyQt5.QtWidgets import QApplication, QProgressBar, QPushButton
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QBasicTimer


class ProgressBar(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self,Sec)
        self.timeStep = Sec * 10
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('ProgressBar')
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.button = QPushButton('Start', self)
        self.button.setFocusPolicy(Qt.NoFocus)
        self.button.move(40, 80)

        self.button.clicked.connect(self.onStart)
        self.timer = QBasicTimer()
        self.step = 0

    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            self.timeStep = 0
            self.step = 0
            return
        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def onStart(self):
        if self.timer.isActive():
            self.timer.stop()
            self.button.setText('Start')
        else:
            self.timer.start(tiemStep, self)
            self.button.setText('Stop')


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    qb = ProgressBar()
    qb.show()
    sys.exit(app.exec_())
