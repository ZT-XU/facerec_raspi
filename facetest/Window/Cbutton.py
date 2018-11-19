from PyQt5 import QtGui
import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextBrowser, QTextEdit, QGraphicsTextItem, \
    QPlainTextDocumentLayout, QPlainTextEdit, QGraphicsSimpleTextItem, QWidget

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Window"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setGeometry(self.top, self.left, self.width, self.height)
        #pp = QPlainTextEdit(self)
        oo = QTextBrowser(self)

        self.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
