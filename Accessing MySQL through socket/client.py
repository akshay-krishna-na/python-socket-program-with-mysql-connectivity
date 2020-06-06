from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import socket





class MyWindow(QMainWindow):

    
    s=socket.socket()
    #functions for events

    def connect(self):
        host = "localhost"
        
        
        port = int(self.portaddr.text())
        self.s.connect((host,port))
        print("Connected to server")



    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()

    def button_clicked(self):
        adno = self.admno.text()
        self.s.send(adno.encode('utf-8'))
        
        sresponse = self.s.recv(4096).decode('utf-8')
        sr_tup = sresponse.split(',')
        for i in sr_tup:
            print(i)
        
        
        #variables with 'self' are global,others are local to the function
        self.name.setText(sr_tup[0])
        self.branch.setText(sr_tup[1])
        self.div.setText(sr_tup[2])
        self.gen.setText(sr_tup[3])
        self.age.setText(sr_tup[4])
        self.cgpa.setText(sr_tup[5])
        
    

    def initUI(self):

        #UI elements

        self.setGeometry(200, 200, 800, 670)
        self.setWindowTitle("TCP Client")

        self.label0 = QtWidgets.QLabel(self)
        self.label0.setText("Port : ")
        self.label0.move(200,50)

        self.portaddr =QtWidgets.QLineEdit(self)
        self.portaddr.setGeometry(QtCore.QRect(270, 50, 200, 31))

        self.con = QtWidgets.QPushButton(self)
        self.con.setText("Connect")
        self.con.move(490,50)
        self.con.clicked.connect(self.connect)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Admission No.  : ")
        self.label.setGeometry(150,100,341,31)


        
        self.admno =QtWidgets.QLineEdit(self)
        self.admno.setGeometry(QtCore.QRect(300, 100, 341, 31))


        self.namel = QtWidgets.QLabel(self)
        self.namel.setText("Name : ")
        self.namel.setGeometry(150,250,341,31)


        
        self.name =QtWidgets.QLineEdit(self)
        self.name.setGeometry(QtCore.QRect(300, 250, 341, 31))

        
        self.branchl = QtWidgets.QLabel(self)
        self.branchl.setText("Branch : ")
        self.branchl.setGeometry(150,300,341,31)


        
        self.branch =QtWidgets.QLineEdit(self)
        self.branch.setGeometry(QtCore.QRect(300, 300, 341, 31))


        self.divl = QtWidgets.QLabel(self)
        self.divl.setText("Division : ")
        self.divl.setGeometry(150,350,341,31)


        
        self.div =QtWidgets.QLineEdit(self)
        self.div.setGeometry(QtCore.QRect(300, 350, 341, 31))


        self.genl = QtWidgets.QLabel(self)
        self.genl.setText("Gender : ")
        self.genl.setGeometry(150,400,341,31)


        
        self.gen =QtWidgets.QLineEdit(self)
        self.gen.setGeometry(QtCore.QRect(300, 400, 341, 31))


        self.cgpal = QtWidgets.QLabel(self)
        self.cgpal.setText("CGPA : ")
        self.cgpal.setGeometry(150,450,341,31)


        
        self.cgpa =QtWidgets.QLineEdit(self)
        self.cgpa.setGeometry(QtCore.QRect(300, 450, 341, 31))


        self.agel = QtWidgets.QLabel(self)
        self.agel.setText("Age : ")
        self.agel.setGeometry(150,500,341,31)


        
        self.age =QtWidgets.QLineEdit(self)
        self.age.setGeometry(QtCore.QRect(300, 500, 341, 31))


        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Submit")
        self.b1.move(350,150)
        self.b1.clicked.connect(self.button_clicked)

        self.fstatus = QtWidgets.QLabel(self)
        self.fstatus.setText("    ")
        self.fstatus.setGeometry(340,200,150,100)

    def update(self):
        self.label.adjustSize()


def main():

    
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

main()
