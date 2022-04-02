# RTHM DEVICE V1.
# WRITTEN AND CODED BY JOHN ERIC AZORES
# Github:   https://github.com/Jonnykoder

import sys
from PyQt5.uic import loadUi
from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget ,QLabel,QLineEdit
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap

#Sensor headers
import max30102
from smbus2 import SMBus
from mlx90614 import MLX90614
import hrcalc
import time

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
        
        # load images from images folder
        self.im = QPixmap("./images/hello.png")
        self.imgHello.setPixmap(self.im)
        
        self.btnScan.clicked.connect(self.gotoScanner)     #goto Scanner function
    def goHome(self):
        home = MainWindow()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex()-1)

    def gotoScanner(self):
        
        self.thread={} #Initialize a thread
        #self.thread[1].start()
        self.scan = Scanner()
    
        widget.addWidget(self.scan)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        newuser = self.txtName.text()
        #assign this name to the next windows
        self.scan.lblName.setText(newuser)
        
        
class Scanner(QDialog):
    def __init__(self):
        super(Scanner, self).__init__()
        loadUi("Scanner.ui", self)
        QtGui.QGuiApplication.processEvents()
        self.btnBack.clicked.connect(self.goBack)
        
       
        self.InitializeSensor()
    def InitializeSensor(self):
        m = max30102.MAX30102()
        bus = SMBus(1)
        sensor = MLX90614(bus, address=0x5A)
        celcius = sensor.get_object_1();
        faren = (celcius*1.8)+32
        room = sensor.get_ambient()
        roomTemp = round(room, 2)
        bodyTemp = (round(celcius+5,2))
        hr2 = 0
        sp2 = 0
        print("_____________________________________________________")
        print("|\t \t STATUS: SENSORS LOADED    . \t     |")
        print("_____________________________________________________")
        
        while True:
            red, ir = m.read_sequential()
            hr,hrb,sp,spb = hrcalc.calc_hr_and_spo2(ir, red)
            if(hrb == True and hr != -999):
                hr2 = int(hr)
                self.lblHeartRate.setText(str(hr2))
                self.lblBodyTemp.setText(str(bodyTemp)+"°")
                """print("--------------------")
                print("Heart Rate : ",hr2)
                print("Body Temp  : ",bodyTemp,"\N{DEGREE SIGN}") """
                QtGui.QGuiApplication.processEvents()
            if(spb == True and sp != -999):
                sp2 = int(sp)
                self.lblOxygenLevel.setText(str(sp2))
                self.lblRoomTemp.setText(str(roomTemp)+"°")
                """ print("SPO2       : ",sp2)
                print ("Room Temp  :", roomTemp,u"\N{DEGREE SIGN}C")
                print("--------------------") """
                time.sleep(12)
                break
                QtGui.QGuiApplication.processEvents()
            else:
                print("_____________________________________________________")
                print("|\t \t STATUS: No vitals detected. \t     |")
                print("_____________________________________________________")
        
        print("result : \n Heart Rate: {} \n Oxygen Level: {} \n Room Temp: {}°C \n Body Temp: {}°C"
              .format(
                  hr2,
                  sp2,
                  roomTemp,
                  bodyTemp)
              )
        return False
        QtGui.QGuiApplication.processEvents()
        
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