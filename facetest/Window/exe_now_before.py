import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QDialog, QLabel
import pexpect,os
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap



class exe_dialog(QDialog):

    def __init__(self):
        super().__init__()
        self.resize(320,240)
        self.child = None
        self.setWindowTitle("正在运行")
        self.tip = QLabel("程序正在进行...请不要关闭此窗口")
        vbox = QVBoxLayout()
        self.image = QLabel()
        self.button = QPushButton("退出")
        self.image.resize(240,360)
        self.timer = QTimer()
        self.timer2 = QTimer()
        self.timer.start(1000)
        self.timer2.start(1)
        #self.timer.timeout.connect(self.shutdown)
        vbox.addWidget(self.tip)
        vbox.addWidget(self.image)
        vbox.addWidget(self.button)
        self.setLayout(vbox)
        self.conn = None
        self.show()
        #self.exe()
        #self.getimage()
        self.timer2.timeout.connect(self.getimage)
        self.button.clicked.connect(self.shutdown)


    def getimage(self):
        if os.path.isfile('frame2.jpg'):
            self.image.setPixmap(QPixmap("frame2.jpg"))
        with open("process.txt","r") as f:
            b = f.read()
        if "F" in b:
            with open("proceed.txt","w") as f:
                f.write("False")
            self.close()

    def shutdown(self):
        with open("proceed.txt", "w") as f:
            f.write("False")
        with open("process.txt", "w") as f:
            f.write("False")
        self.close()

app = QApplication(sys.argv)
dialog3 = exe_dialog()
sys.exit(app.exec_())

