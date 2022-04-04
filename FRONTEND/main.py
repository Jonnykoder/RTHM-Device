# RTHM DEVICE V1.
# WRITTEN AND CODED BY JOHN ERIC AZORES
# Github:   https://github.com/Jonnykoder

import sys
from PyQt5.uic import loadUi
from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget ,QLabel,QLineEdit,QGridLayout,QDesktopWidget,QMessageBox
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
import PyQt5
#Sensor headers
import max30102
from smbus2 import SMBus
from mlx90614 import MLX90614
import hrcalc
import time
from sim800l import SIM800L
import RPi.GPIO as GPIO
from datetime import date
from datetime import datetime
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.IN)
sim800l=SIM800L('/dev/serial0')
m = max30102.MAX30102()
bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)
btnctr =0
ctr = btnctr

from sim800l import SIM800L
sim800l=SIM800L('/dev/serial0')
"""
name="John"
hr = str(92)
sp02 = str(120)
roomTemp = str(35.2)
bodyTemp = str(34.2)
deg = "C"
date ="04-18-2023"
time = "05:30 PM" 
userData = ("--------------------------------------\nDate: {} \nTime: {} \n--------------------------------------\nName: {} \nHeart Rate: {} Bpm\nOxygen Saturation: {}% \nRoom Temp:{} C \nBody Temperature:{} C \n--------------------------------------\n\n RTHM DEVICE V1.03.22 BETA"
            .format(
                date,
                time,
                name,
                hr,
                sp02,
                roomTemp,
                bodyTemp)
            )
print(userData )
sms=("test again")
num = '9155006780' #this will be from the user input
pref = '63'
cp = pref+num
"""
#####################################################################################
#Run Sensors on Thread
class Thread(QtCore.QThread):
    data_sensors = QtCore.pyqtSignal(tuple)
    userName = QtCore.pyqtSignal(tuple)
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
        self.center()
        loadUi("windowStart.ui", self)
       
        #load images from images folder
        self.im = QPixmap("./images/startScreenLogo.png")
        self.imgStartScreenLogo.setPixmap(self.im)

        #add event when btnStart is pressed
        self.btnStart.clicked.connect(self.gotoNewUser)   #<----Load gotoNewUserfunction
    def center(self):
        
        screen = QtGui.QGuiApplication.screenAt(QtGui.QCursor().pos())
        fg = self.frameGeometry()
        fg.moveCenter(screen.geometry().center())
        self.move(fg.topLeft())
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
        self.btnBack.clicked.connect(self.goBack)
       
        # load images from images folder
        self.im = QPixmap("./images/hello.png")
        self.imgHello.setPixmap(self.im)
        
        self.btnScan.clicked.connect(self.gotoScanner)     #goto Scanner function
  

    def gotoScanner(self):
    
        newuser = (self.txtName.text()).lstrip()
      
        if (newuser ==""):
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Please enter a name to proceed \n with scanning.")
            msg.setIcon(QMessageBox.Warning)
            x=msg.exec()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("notice")
            msg.setText("you will proceed to the scanning window. \nPlease put your finger on the scanner.")
            msg.setIcon(QMessageBox.Information)
            x=msg.exec()
            
            self.scan = Scanner()
            self.recep = SendSms()
            widget.addWidget(self.scan)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            
            #assign this name to the next windows
            self.scan.lblName.setText(self.txtName.text())
            self.recep.lblName.setText(self.txtName.text())
    def goBack(self):
        self.mainwin = MainWindow()     
        widget.addWidget(self.mainwin)
        widget.setCurrentIndex(widget.currentIndex() -1)
class Scanner(QDialog):
    def __init__(self):
        super(Scanner, self).__init__()
        loadUi("Scanner.ui", self)
        QtGui.QGuiApplication.processEvents()
        self.btnBack.clicked.connect(self.goBack)
        thread = Thread(self)
        thread.data_sensors.connect(self.update_Sensors)
        thread.start()
        self.lblScanning.setText("Scanning..")
        #set this button to disable when data is not yet scanned
        self.btnNext.setEnabled(False)
        self.btnNext.clicked.connect(self.sendData)
        self.btnNext_2.setEnabled(False)
        self.btnNext.setStyleSheet("background-color:gray; border:gray")
        #print(ctr)
    def update_Sensors(self, data ):
        hr, sp , hrb , spb ,rt,bt= data
        hr2 = int(hr)
        sp2 = int(sp)
       
        print("DEVICE STATUS: \t SCANNING SENSOR DATA...")
        ctr = btnctr + 1
        
       
        if(hrb == True and spb ==True):
            print("DEVICE STATUS: \t VITALS DETECTED...")
            ctr = btnctr + 1
            #print(ctr)
            if(sp2 < 50 and hr2 <50):
                self.label.setText("please put pressure on the sensor")
            
            else:
                self.label.setText("")
                if(hr != -999 and hr > 50):
                    
                    ctr = btnctr + 2
                    #print (ctr)
                    if(sp >50):
                        self.lblBodyTemp.setText(str(bt)+"°")   
                        self.lblOxygenLevel.setText(str(sp2))
                        self.lblRoomTemp.setText(str(rt)+"°")
                        self.lblHeartRate.setText(str(hr2))  # heart rate needs atleast 5-10 seconds and pressure to initialize
                        ctr = btnctr + 3
                        #print (ctr)
                   
                    if (ctr < 3):
                        self.label.setText("")
                    if (ctr == 3):
                        self.lblScanning.setText("Done Scanning")
                        self.btnNext.setEnabled(True)
                        self.btnNext_2.setEnabled(True)
                        self.btnNext.setStyleSheet("background-color:#FFE2CE; border:2px solid rgb(255,102,0);")
                          
        else:
            self.label.setText("please put pressure on the sensor if you want to continue scanning")
            ctr = btnctr + 1
            #print(ctr)
            
       
       
    def goBack(self):
        msg = QMessageBox()
        msg.setWindowTitle("Warning")
        msg.setText("This action will cancel the scanning proccess. \nDo you want still want to go back?.")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Cancel)
        msg.buttonClicked.connect(self.popup_button)
        x=msg.exec()
        
    def popup_button(self, i):
        val = i.text()
        if(val == "OK"):
            newuser = NewUser()  # <---Instantiate NewUser  Class
            widget.addWidget(newuser)
            widget.setCurrentIndex(widget.currentIndex() -1)  # <----Concat an index number to page 2.
            self.lblScanning.setText("Scanning..")
            self.lblHeartRate.setText("-")
            self.lblRoomTemp.setText("-")
            self.lblOxygenLevel.setText("-")
            self.lblBodyTemp.setText("-")
            self.btnNext.setEnabled(False)
            self.btnNext_2.setEnabled(False)
            self.btnNext.setStyleSheet("background-color:gray; border:gray")
            self.label.setText("")
            
           
        
    def sendData(self):
        self.sendsms = SendSms()     
        widget.addWidget(self.sendsms)
        widget.setCurrentIndex(widget.currentIndex() + 1)
class SendSms(QDialog):
    def __init__(self):
        
        super(SendSms, self).__init__()
        loadUi("Recepient.ui", self)
        self.btnBack.clicked.connect(self.goBack)
        self.btnSend.clicked.connect(self.validationSend)
        self.txtNumber.mousePressEvent = (self.mousePressed)
        thread = Thread(self)
        thread.data_sensors.connect(self.validationSend)
        
    def mousePressed(self, event):
        self.txtNumber.clear()
    def goBack(self):
        
    
       
        scan = Scanner()  # <---Instantiate NewUser  Class
        widget.addWidget(scan)
        scan.lblScanning.setText("Scanning..")
        widget.setCurrentIndex(widget.currentIndex() -1)  # <----Concat an index number to page 2.
        inp = (self.txtNumber.text()).lstrip()
        if(inp == ""):
            self.txtNumber.setText("9123456789")
    def validationSend(self ):

        num = (self.txtNumber.text()).lstrip()
        if(num == "9123456789"):
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("The number must not be same as the placeholder!")
            msg.setIcon(QMessageBox.Warning)
            x=msg.exec()
        else:
            if(num == ""):
                msg = QMessageBox()
                msg.setWindowTitle("Missing Value")
                msg.setText("Cannot send to empty phone number .")
                msg.setIcon(QMessageBox.Warning)
                x=msg.exec()
                
            else:
                nLen = len(num)
                f_dig = num[0]
                if (f_dig =="9" and num.isdigit() ):
                    if (nLen != 10):
                        msg = QMessageBox()
                        msg.setWindowTitle("Incomplete value")
                        msg.setText("The phone number must contain 10 digits and starts with 9.")
                        msg.setIcon(QMessageBox.Warning)
                        x=msg.exec()
                    else:
                        
                        
                        #print("first digit"+f_dig)
                        pref = self.lblNumber.text()
                        number = self.txtNumber.text()
                        msg = QMessageBox()
                        msg.setWindowTitle("Send Data")
                        msg.setText("Do you want to send data \n to {}{} phone number?.".format(pref,number))
                        msg.setIcon(QMessageBox.Question)
                        msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
                        msg.setDefaultButton(QMessageBox.Cancel)
                        msg.buttonClicked.connect(self.popup_button)
                        x=msg.exec()
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Input error")
                    msg.setText("Please enter a correct value .. \n example:9123456789")
                    msg.setIcon(QMessageBox.Warning)
                    x=msg.exec()
    def popup_button(self, i):
        val = i.text()
        Today = date.today()
        d2day = Today.strftime("%B %d, %Y")
        time = (datetime.today().strftime("%I:%M %p"))
        if(val == "OK"):
            self.scanData = Scanner()
            hr2 = self.scanData.lblHeartRate.text()
            sp2 = self.scanData.lblOxygenLevel.text()
            rt = self.scanData.lblRoomTemp.text()
            bt = self.scanData.lblBodyTemp.text()
            name = "null"
            userData = ("--------------------------------------\nDate: {} \nTime: {} \n--------------------------------------\nName: {} \nHeart Rate: {} Bpm\nOxygen Saturation: {}% \nRoom Temp:{} C \nBody Temperature:{} C \n--------------------------------------\n\n RTHM DEVICE V1.03.22 BETA"
                .format(
                    d2day,
                    time,
                    name,
                    hr2,
                    sp2,
                    rt,
                    bt)
                    )
            pref = "63"
            num ="9155006780"
            cp = pref+num
            sim800l.send_sms(cp,userData)
            msg = QMessageBox()
            msg.setWindowTitle("Success!")
            msg.setText("The data has been sent .")
            msg.setIcon(QMessageBox.Information)
            x=msg.exec()
        
        
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(564)
widget.setFixedWidth(1024)

widget.show()

try:
    sys.exit(app.exec_())
except:
    print("exiting..")
