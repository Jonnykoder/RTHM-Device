# RTHM DEVICE V1.
# WRITTEN AND CODED BY JOHN ERIC AZORES
# Github:   https://github.com/Jonnykoder

import sys
from PyQt5.uic import loadUi
from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget ,QLabel,QLineEdit
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore

#Sensor headers
import max30102
from smbus2 import SMBus
from mlx90614 import MLX90614
import hrcalc
import time

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.IN)

m = max30102.MAX30102()
bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)


#####################################################################################
#Run Sensors on Thread
class Thread(QtCore.QThread):
    data_sensors = QtCore.pyqtSignal(tuple)
    def run(self):
        while True:
           
            celcius = sensor.get_object_1();
            faren = (celcius*1.8)+32
            room = sensor.get_ambient()
            rt = round(room, 2)       #roomTemp
            bt = (round(celcius+5,2)) #bodyTemp
            red, ir = m.read_sequential()
            hr,hrb,sp,spb = hrcalc.calc_hr_and_spo2(ir, red)
            
            
            
            self.data_sensors.emit((hr,sp,hrb,spb,rt,bt))

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
        thread = Thread(self)
        thread.data_sensors.connect(self.update_Sensors)
        thread.start()
        
        #set this button to disable when data is not yet scanned
        self.btnNext.setEnabled(False)
        self.btnNext_2.setEnabled(False)
        

    def update_Sensors(self, data):
        hr, sp , hrb , spb ,rt,bt= data
        hr2 = int(hr)
        sp2 = int(sp)
        
        print("_____________________________________________________")
        print("|\t \t STATUS: SENSORS LOADED    . \t     |")
        print("_____________________________________________________")
        btnctr = 0
        if(hrb == True and spb ==True):
            if(sp != -999 and sp < 100):
                self.lblBodyTemp.setText(str(bt)+"°")   
                self.lblOxygenLevel.setText(str(sp2))
                self.lblRoomTemp.setText(str(rt)+"°")
                btnctr +=1
            if(hr != -999 and hr<105):
                self.lblHeartRate.setText(str(hr2))  # heart rate needs atleast 5-10 seconds and pressure to initialize
                btnctr += 1
                ctr = btnctr
                if (ctr == 2):
                    self.btnNext.setEnabled(True)
                    self.btnNext_2.setEnabled(True)
                    self.btnNext.setStyleSheet("background-color:#FFE2CE;")
                               
        else:
            
            print("_____________________________________________________")
            print("|\t \t STATUS: No vitals detected. \t     |")
            print("_____________________________________________________")
       
        """
        while True:
            red, ir = m.read_sequential()
            hr,hrb,sp,spb = hrcalc.calc_hr_and_spo2(ir, red)
            if(hrb == True and hr != -999):
                hr2 = int(hr)
                self.lblHeartRate.setText(str(hr2))
                self.lblBodyTemp.setText(str(bodyTemp)+"°")
                print("--------------------")
                print("Heart Rate : ",hr2)
                print("Body Temp  : ",bodyTemp,"\N{DEGREE SIGN}") 
                QtGui.QGuiApplication.processEvents()
            if(spb == True and sp != -999):
                sp2 = int(sp)
                self.lblOxygenLevel.setText(str(sp2))
                self.lblRoomTemp.setText(str(roomTemp)+"°")
                print("SPO2       : ",sp2)
                print ("Room Temp  :", roomTemp,u"\N{DEGREE SIGN}C")
                print("--------------------") 
                time.sleep(12)
                break
              
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
        """
    def goBack(self):
        newuser = NewUser()  # <---Instantiate NewUser  Class
        widget.addWidget(newuser)
        widget.setCurrentIndex(widget.currentIndex() -1)  # <----Concat an index number to page 2.
        self.lblHeartRate.setText("-")
        self.lblRoomTemp.setText("-")
        self.lblOxygenLevel.setText("-")
        self.lblBodyTemp.setText("-")
        self.btnNext.setEnabled(False)
        self.btnNext_2.setEnabled(False)
        self.btnNext.setStyleSheet("background-color:gray")
        #stop scanner thread after going back
        thread = Thread(self)
        thread.data_sensors.connect(self.update_Sensors)
        thread.quit()
        print("Thread stopped...")
        
    def sendData(self):
        self.send = SendSms()     
        widget.addWidget(self.send)
        widget.setCurrentIndex(widget.currentIndex() + 1)
class SendSms(QDialog):
    def __init__(self):
        super(sms, self).__init__()
        loadUi("Recepient.ui", self)
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