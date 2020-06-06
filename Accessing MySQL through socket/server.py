from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import os
import socket
import mysql.connector





class MyWindow(QMainWindow):
	
    c=0    
    #functions for events

    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()

    def button_clicked(self):
        host ="localhost"
        port = int(self.portaddr.text())

        s = socket.socket()
        self.update()
        s.bind((host,port))
        s.listen(5)
        print("SERVER UP")
        self.c,addr = s.accept()
        while True:
            # For enabling multiple submit of 'admno' for infinit times(else after on admno ipc pipe will break !)
            admnos = self.c.recv(1024).decode('utf-8')
            admno = int(admnos)
            print(admno)
            mydb = mysql.connector.connect(host='localhost',user='cypherx',passwd='pswd',database='fisat')
            print("Connected to DB")
            mycursor = mydb.cursor()
            mycursor.execute("SELECT name,branch,division,gender,cgpa,age FROM student WHERE admno="+str(admno)+";")  
            myresult = mycursor.fetchall()
            for x in myresult:
                y=x
                print(y)
                stry=""
                for i in y:
                    stry=stry+str(i)+","
                self.c.send(stry.encode('utf-8'))
        s.close()

    def initUI(self):

        #UI elements

        self.setGeometry(200, 200, 800, 300)
        self.setWindowTitle("TCP Server")

        self.label0 = QtWidgets.QLabel(self)
        self.label0.setText("port : ")
        self.label0.move(200,50)

        self.portaddr =QtWidgets.QLineEdit(self)
        self.portaddr.setGeometry(QtCore.QRect(300, 50, 341, 31))
        

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Run Server")
        self.b2.setGeometry(350,120,100,30)
        self.b2.clicked.connect(self.button_clicked)

        self.sstatus = QtWidgets.QLabel(self)
        self.sstatus.setText("    ")
        self.sstatus.setGeometry(340,200,150,100)

    def update(self):
        self.sstatus.adjustSize()


def main():

    
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

main()
