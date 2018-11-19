from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QDialog, QGridLayout, QLineEdit, QPushButton, QLabel
import sys
from SSHConnection import SSHConnection


class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(240,200)
        self.setWindowTitle('连接到树莓派')
        self.CANCEL = False
        gridLayout = QGridLayout()

        gridLayout.addWidget(QLabel('用户名:',self),0,0)
        self.U_Line_Edit = QLineEdit(self)
        gridLayout.addWidget(self.U_Line_Edit,0,1)


        gridLayout.addWidget(QLabel('主机名(IP):', self), 1, 0)
        self.H_Line_Edit = QLineEdit(self)
        gridLayout.addWidget(self.H_Line_Edit, 1, 1)


        gridLayout.addWidget(QLabel('密码:', self), 2, 0)
        self.P_Line_Edit = QLineEdit(self)
        self.P_Line_Edit.setEchoMode(QLineEdit.Password)
        gridLayout.addWidget(self.P_Line_Edit, 2, 1)

        btn2 = QPushButton('确定', self)
        btn1 = QPushButton('取消',self)
        btn2.setShortcut('Enter')
        gridLayout.addWidget(btn1,3,0)
        gridLayout.addWidget(btn2,3,1)
        btn1.clicked.connect(self.cancel)
        btn2.clicked.connect(self.btn2_function)

        self.setLayout(gridLayout)
        self.show()

    def cancel(self):
        self.CANCEL = True
        self.close()

    def btn2_function(self):
        self.U_Line_Edit.text()
        self.H_Line_Edit.text()
        self.P_Line_Edit.text()
        self.close()

    def getUsername(self):
        return self.U_Line_Edit.text().strip()

    def getHostname(self):
        return self.H_Line_Edit.text().strip()

    def getPassword(self):
        return self.P_Line_Edit.text().strip()

class OneLineDialog(QDialog):
    def __init__(self,title,message):
        super().__init__()
        self.resize(300,150)
        self.setWindowTitle(title)
        self.text = ""
        self.CANCEL = False
        gridLayout = QGridLayout()
        self.line = QLineEdit(self)
        gridLayout.addWidget(QLabel(message,self),0,0)
        gridLayout.addWidget(self.line,0,1)
        btn2 = QPushButton('确定', self)
        btn1 = QPushButton('取消', self)
        gridLayout.addWidget(btn1, 1, 0)
        gridLayout.addWidget(btn2, 1, 1)
        btn1.clicked.connect(self.cancel)
        btn2.clicked.connect(self.get_text)
        self.setLayout(gridLayout)
        self.show()

    def cancel(self):
        self.CANCEL = True
        self.close()

    def get_text(self):
        self.text = self.line.text().strip()
        self.close()

class exe_dialog(QDialog):

    def __init__(self,username,hostname,password):
        super().__init__()
        self.resize(280,40)
        self.setWindowTitle("正在运行")
        self.tip = QLabel("程序正在进行...请不要关闭此窗口",self)
        self.show()
        self.exe(username,hostname,password)


    def exe(self,username, hostname, password):
        self.conn = SSHConnection(username, hostname, password)
        self.conn.exec_command('python3 /home/pi/Project/data_create.py')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog3 = exe_dialog('pi','192.168.1.4','1')
    sys.exit(app.exec_())

