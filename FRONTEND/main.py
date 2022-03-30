# RTHM DEVICE V1.
# WRITTEN AND CODED BY JOHN ERIC AZORES
# Github:   https://github.com/Jonnykoder

import sys
from PyQt5.uic import loadUi
from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget ,QLabel,QLineEdit
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap

#####################################################################################
"""
defining a class for the MainWindow
    Content of this class :
                         1. Load the Main  window
                         2. load the gotoNewUser function that loads other class
                      
"""
class MainWindow(QDialog):
    def __init__(self):              #constructor   <--- this function will load the ui within the block
        super(MainWindow, self).__init__()
        loadUi("windowStart.ui", self)

        #load images from images folder
        self.im = QPixmap("./images/startScreenLogo.png")
        self.imgStartScreenLogo.setPixmap(self.im)

        #add event when btnStart is pressed
        self.btnStart.clicked.connect(self.gotoNewUser)   #<----Load gotoNewUserfunction

    def gotoNewUser(self):
        newuser = NewUser()   #<---Instantiate NewUser  Class
        widget.addWidget(newuser)
        widget.setCurrentIndex(widget.currentIndex()+1)  #<----Concat an index number to page 2.

############################################################################
"""
defining a class for the gotoNewUserfile
    Content of this class :
                         1. Load the newUser.py  window
                         2. validate name if present
                         3. Load Scanner.py
"""
class NewUser(QDialog):
    def __init__(self):
        super(NewUser, self).__init__()
        loadUi("newUser.ui", self)
        self.btnHome.clicked.connect(self.goHome)     # gohome button
        self.btnScan.clicked.connect(self.gotoScanner)     #goto Scanner function

        # load images from images folder
        self.im = QPixmap("./images/hello.png")
        self.imgHello.setPixmap(self.im)
        # button = QtGui.btnHome(self)
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("./images/icons/btnHome.png"))
        # button.setIcon(icon)


    def goHome(self):
        home = MainWindow()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex()-1)

    def gotoScanner(self):
        scan = Scanner()
        widget.addWidget(scan)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Scanner(QDialog):
    def __init__(self):
        super(Scanner, self).__init__()
        loadUi("Scanner.ui", self)
        self.btnBack.clicked.connect(self.goBack)

    

    def goBack(self):
        newuser = NewUser()  # <---Instantiate NewUser  Class
        widget.addWidget(newuser)
        widget.setCurrentIndex(widget.currentIndex() -1)  # <----Concat an index number to page 2.


app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(345)
widget.setFixedWidth(600)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("exiting..")