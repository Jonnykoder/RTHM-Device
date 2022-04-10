# RTHM DEVICE V1.
# WRITTEN AND CODED BY JOHN ERIC AZORES
# Github:   https://github.com/Jonnykoder
import PyQt5
import max30102
import sys
import hrcalc

import RPi.GPIO as GPIO
from PyQt5.uic import loadUi
from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget ,QLabel,QLineEdit,QGridLayout,QDesktopWidget,QMessageBox
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from smbus2 import SMBus
from mlx90614 import MLX90614
from datetime import date , datetime
import time
from sim800l import SIM800L
import csv

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.IN)
sim800l=SIM800L('/dev/ttyS0')
m = max30102.MAX30102()
bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)
btnctr =0
ctr = btnctr

#Run Sensors on Thread
class Thread(QtCore.QThread):
  
    data_sensors = QtCore.pyqtSignal(tuple)
    userName = QtCore.pyqtSignal(tuple)
    def run(self):
        cal = 3.75  #set temp calibration value
        while True:
            celcius = sensor.get_object_1();
            faren = (celcius*1.8)+32
            r = sensor.get_ambient()
            red, ir = m.read_sequential()
           
            roomTemp = round(r, 2)       #roomTemp
            bodyTemp = (round(celcius+cal,2)) #bodyTemp
            heartRate,hrb,oxySat,spb = hrcalc.calc_hr_and_spo2(ir, red)
            self.data_sensors.emit((heartRate,oxySat,hrb,spb,roomTemp,bodyTemp))
          

class MainWindow(QDialog):
    def __init__(self):              #constructor   <--- this function will load the ui within the block
        super(MainWindow, self).__init__()
        self.center()
        loadUi("./src/uiFiles/windowStart.ui", self)
        self.im = QPixmap("./src/images/startScreenLogo.png")
        self.imgStartScreenLogo.setPixmap(self.im)
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
        self.close()
class NewUser(QDialog):
    def __init__(self):
        super(NewUser, self).__init__()
        loadUi("./src/uiFiles/newUser.ui", self)
        self.btnBack.clicked.connect(self.goBack)
        self.im = QPixmap("./src/images/hello.png")
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
            self.saveToLocalTemp()
            self.scan = Scanner()
            self.scan.displayInfo()
            self.scan.lblName.setText(self.txtName.text())
            widget.addWidget(self.scan)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            self.scan.setUiDisabled()
    def saveToLocalTemp(self):
        newuser = (self.txtName.text()).lstrip()
        fields = ['Name']
        v_name = newuser
        data = [[v_name]]
        filename = "temp_user_name.csv"
        with open(filename, 'w') as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(fields)
            csvwriter.writerows(data)
    def goBack(self):
        self.mainwin = MainWindow()     
        widget.addWidget(self.mainwin)
        widget.setCurrentIndex(widget.currentIndex() -1)
      
class Scanner(QDialog):
    def __init__(self):
        super(Scanner, self).__init__()
        loadUi("./src/uiFiles/Scanner.ui", self)
        QtGui.QGuiApplication.processEvents()
        self.btnBack.clicked.connect(self.goBack)
        self.btnRescan.clicked.connect(self.reScan)
        self.getNamedata()
       
        thread = Thread(self)
        thread.data_sensors.connect(self.update_Sensors)
        thread.start()
        self.setUiDisabled()
    def displayInfo(self):
        self.show()
    def setUiDisabled(self):
        #set this button to disable when data is not yet scanned
        self.btnNext.setEnabled(False)
        self.btnNext.clicked.connect(self.gotoSms)
        self.btnRescan.setEnabled(False)
        self.btnNext_2.setEnabled(False)
        self.label_19.setEnabled(False)
        self.label_20.setEnabled(False)
        self.label_21.setEnabled(False)
        self.label_15.setEnabled(False)
        self.label_16.setEnabled(False)
        self.label_17.setEnabled(False)
        self.label_18.setEnabled(False)
        self.btnNext.setStyleSheet("background-color:gray; border:gray")
        self.lblHeartRate.setText("-")
        self.lblRoomTemp.setText("-")
        self.lblOxygenLevel.setText("-")
        self.lblBodyTemp.setText("-")
        self.btnNext.setEnabled(False)
        self.btnNext_2.setEnabled(False)
        self.label.setText("")
        self.label_7.setStyleSheet("background-color:#FFE7D7; border:1px solid #FFE7D7;")
        self.label_9.setStyleSheet("background-color:#FFE7D7; border:1px solid #FFE7D7;")
        self.label_11.setStyleSheet("background-color:#FFE7D7; border:1px solid #FFE7D7;")
        self.lblScanning.setText("Scanning..")
    def reScan(self):
        self.setUiDisabled()
    def getNamedata(self):
        filename = "temp_user_name.csv"
        with open(filename, 'r') as r:
            csv_reader = csv.reader(r)
            for line_no , line in enumerate(csv_reader , 1):
                if line_no == 2:
                    self.name = (line[0])
                    self.setName(self.name)
                    QApplication.processEvents()
        self.lblName.repaint() #this doesn't work
        
    def setName(self , name):
        name = self.name
        if (name != ""):
            print("new name{}".format(name))
            self.lblName.setText("{}".format(name))
        
    def update_Sensors(self, data):
        heartRate, oxySat , hrb , spb ,roomTemp,bodyTemp= data
        heartRate_val = int(heartRate)
        oxySat_val = int(oxySat)
       
        print("DEVICE STATUS: \t SCANNING SENSOR DATA...")
        ctr = btnctr + 1
        self.label_15.setEnabled(True)
        self.lblRoomTemp.setText(str(roomTemp)+"°C")
        if(hrb == True and spb ==True):
            
            print("DEVICE STATUS: \t VITALS DETECTED...")
            
            self.lblBodyTemp.setText(str(bodyTemp)+"°C")
            ctr = btnctr + 2
            self.label_7.setStyleSheet("background-color:#FF6600; border:1px solid rgb(255,102,0);")
            self.label_19.setEnabled(True)
            self.label_16.setEnabled(True)
        
            if(heartRate != -999 and  50 <= heartRate <= 150):
                self.label_9.setStyleSheet("background-color:#FF6600; border:1px solid rgb(255,102,0);")
                ctr = btnctr + 3
                self.lblHeartRate.setText(str(heartRate_val))  # heart rate needs atleast 5-10 seconds and pressure to initialize
                self.label_20.setEnabled(True)
                self.label_17.setEnabled(True)
        
        
                if(oxySat >85):
                    if(ctr >2 and hrb == True and spb ==True):
                        self.lblOxygenLevel.setText(str(oxySat_val) + "%")
                        ctr = btnctr + 4
                        self.label_18.setEnabled(True)
                        t = 4
                        self.label_21.setEnabled(True)
                        while t:
                            s = divmod(t ,60)
                                #time_format = '{:02}'.format(s)
                                #print("Scanning in:" +time_format)
                            time.sleep(1)
                            t -=1
                        self.btnNext.setEnabled(True)
                        self.btnNext_2.setEnabled(True)
                        self.btnRescan.setEnabled(True)
                        self.lblScanning.setText("Done Scanning")
                        self.label_11.setStyleSheet("background-color:#FF6600; border:1px solid rgb(255,102,0);")
                        self.btnNext.setStyleSheet("background-color:#FFE2CE; border:2px solid rgb(255,102,0);")
                        self.saveTempData(data)
            else:
                self.lblNotice.setText("please put pressure on the sensor if you want to continue scanning")
                ctr = btnctr + 1
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
            self.setUiDisabled()
            self.close()
            
    def gotoSms(self):
        self.sendsms = SendSms()     
        widget.addWidget(self.sendsms)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self.close()
    def saveTempData(self , data):
        heartRate, oxySat , hrb , spb ,roomTemp,bodyTemp= data
        # field names will be assigned to the csv file
        fields = [ 'Room_Temp' ,'Body_Temp' , 'Oxy_Sat' , 'Heart_rate']
        v_rt = roomTemp
        v_bt = bodyTemp 
        v_oxs = int(oxySat)
        v_hr = heartRate
        data = [[v_rt , v_bt , v_oxs , v_hr]]
        print(data)
        filename = "temp_user_data.csv"
        with open(filename, 'w') as f:
            # creating a csv writer object
            csvwriter = csv.writer(f)
            # writing the fields
            csvwriter.writerow(fields)
            # writing the data rows
            csvwriter.writerows(data)
class SendSms(QDialog):
    def __init__(self):
        super(SendSms, self).__init__()
        loadUi("./src/uiFiles/Recepient.ui", self)
        self.btnBack.clicked.connect(self.goBack)
        self.btnSend.clicked.connect(self.validationSend)
        self.btnRestart.clicked.connect(self.reStart)
        self.txtNumber.mousePressEvent = (self.mousePressed)
        self.disabledUiSms()
        userName = "temp_user_name.csv"
        self.scan = Scanner()
        with open(userName, 'r') as n:
            csv_reader = csv.reader(n)
            for line_no , line in enumerate(csv_reader , 1):
                if line_no == 2:
                    v_name = (line[0])
                    self.lblName.setText(v_name)
                    self.lblName.repaint()
    def reStart(self):
        self.restart = MainWindow()
        widget.addWidget(self.restart)
        widget.setCurrentIndex(widget.currentIndex()-3)
        self.scan.setUiDisabled()
    def disabledUiSms(self):
        self.btnRestart.setEnabled(False)
        self.btnRestart2.setEnabled(False)
        self.btnRestart.setStyleSheet("background-color:#FFE7D7; border:1px solid #FFE7D7;")
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
        self.disabledUiSms()
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
        num = (self.txtNumber.text()).lstrip()
        val = i.text()
        Today = date.today()
        d2day = Today.strftime("%B %d, %Y")
        time = (datetime.today().strftime("%I:%M %p"))
        if(val == "OK"):
            userName = "temp_user_name.csv"
            filename = "temp_user_data.csv"
            with open(userName, 'r') as n:
                csv_reader = csv.reader(n)
                for line_no , line in enumerate(csv_reader , 1):
                    if line_no == 2:
                        v_name = (line[0])
            with open(filename, 'r') as r:
                csv_reader = csv.reader(r)
                for line_no , line in enumerate(csv_reader , 1):
                    if line_no == 2:
                        rt = (line[0])
                        bt = (line[1])
                        sp2 = (line[2])
                        hr2 = (line[3])
            name = v_name
            userData = ("----------------------------------\nDate: {} \nTime: {} \n----------------------------------\nName: {} \nHeart Rate: {} Bpm\nOxygen Saturation: {}% \nRoom Temp:{} C \nBody Temperature:{} C \n----------------------------------\n\n RTHM DEVICE V1.03.22 BETA"
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
            cp = pref+num
            sim800l.send_sms(cp,userData)
            msg = QMessageBox()
            msg.setWindowTitle("Success!")
            msg.setText("The data has been sent .")
            msg.setIcon(QMessageBox.Information)
            x=msg.exec()
            self.btnRestart.setEnabled(True)
            self.btnRestart2.setEnabled(True)
            self.btnRestart.setStyleSheet("background-color:#FFE2CE; border: 2px solid  rgb(255, 102, 0);")
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
