# RTHM DEVICE V2.
# WRITTEN AND CODED BY JOHN ERIC AZORES
# Github:   https://github.com/Jonnykoder
import PyQt5
import max30102
import sys
import hrcalc

from traceback import print_tb
from PyQt5.uic import loadUi
from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QWidget, QStackedWidget ,QLabel,QLineEdit,QGridLayout,QDesktopWidget,QMessageBox,QPushButton
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, QCoreApplication
import sys
import csv
import logging
from PyQt5 import QtCore
from smbus2 import SMBus
from mlx90614 import MLX90614
from datetime import date , datetime
import time
from sim800l import SIM800L

import RPi.GPIO as GPIO
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
          
class MainWindow(QMainWindow):
    update_win = pyqtSignal()
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("./src/uiFiles/mainWindow.ui", self)
        self.btnPreferences.clicked.connect(self.view_preferences)   #set method to the button preferences
        self.btnScan.clicked.connect(self.goto_scanner)
        self.repaint()
        self.update_win.connect(self.load_data)
        
    def goto_scanner(self):
        print("scanner enabled")
        self.scanner = Scanner()
        widget.addWidget(self.scanner)
        #self.set_notice_msg()  <---reserved
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.view_guide()
        
    def view_preferences(self):
        self.login = Login()
        self.preferences = Preferences()
        self.preferences.window_closed.connect(self.load_data)
        self.login.show()
       # self.preferences.show()
       
    def view_guide(self):
        self.show_guide = Sensor_guide()
        self.show_guide.show()
   
    def load_data(self):
        filename = "temp_preferences.csv"
        
        try:
            with open(filename, 'r') as r:
                csv_reader = csv.reader(r)
                self.btnScan.setEnabled(True)
                self.btnScan.setStyleSheet("background-color: rgb(255, 102, 0); border:none; color:white; icon-size: 53px;")
                for line_no , line in enumerate(csv_reader , 1):
                    
                    if line_no == 2:
                        #print(line[0])
                        self.name = (line[0])
                        self.recipient =(line[3])
                        if (self.name != "" and self.recipient !=""):
                            print("================================\n|\tData loaded.... \t|\n================================")
                            
                            self.pref = Preferences()
                            self.pref.btnSave.setText("Update")
                        else:
                            print("================================\n|\tData Missing.... \t|\n===========x=====================")
                            self.btnScan.setEnabled(False)
                            self.btnScan.setStyleSheet("background-color: #FF954F; border:none; icon-size: 53px;")
        except IOError: 
            print("========================================\n| Data not found, button is disabled....|\n========================================")   
        if not filename:
            raise ValueError('No data available')
        return filename
    def Try(self):
        print("dapat mag enable")
    
class Login(QDialog):
    window_closed = pyqtSignal()
    def __init__(self):
        super(Login,self).__init__()
        loadUi("./src/uiFiles/Login.ui", self) 
        self.btnlogin.clicked.connect(self.validate_password)
        
    def validate_password(self):
        var_pass = "admin"
        var_input_pass = (self.txtPassword.text()).lstrip()
        if (var_input_pass ==""):
            msg = QMessageBox()
            msg.setWindowTitle("Missing value")
            msg.setText("Please enter the password ")
            msg.setIcon(QMessageBox.Warning)
            x=msg.exec()
        else:
            if (var_input_pass == var_pass):
                print("success validation")
                self.view_preferences_pass()
                self.close()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Password Incorrect!")
                msg.setIcon(QMessageBox.Warning)
                x=msg.exec()
    
    def view_preferences_pass(self):
        self.preferences = Preferences()
        self.main = MainWindow()
        self.preferences.window_closed.connect(self.main.load_data)
        self.preferences.show()
    
class Preferences(QDialog):
    window_closed = pyqtSignal()
    def __init__(self):
        super(Preferences,self).__init__()
        loadUi("./src/uiFiles/preferences.ui", self)  # <--import preferences ui file
        self.btnCancel.clicked.connect(self.close_window) # <-- call close function
        self.btnSave.clicked.connect(self.confirm_dialog) #<-- call confirm dialog when button is clicked
        
    def confirm_dialog(self): 
        p_name = (self.txtName.text()).lstrip()
        r_mobile_number =(self.txtMobile.text()).lstrip()
        
        if (p_name != "Not set"):
            self.txtName.setStyleSheet("border: none;")
            if (p_name == "" ):
                self.set_error_msg()
                
            elif (r_mobile_number == ""):
                self.txtMobile.setStyleSheet("border:1px solid red;")
                self.set_error_msg()
            else:
                nLen = len(r_mobile_number)
                f_dig = r_mobile_number[0]
                if (f_dig =="9" and r_mobile_number.isdigit()):
                    if (nLen != 10):
                        msg = QMessageBox()
                        msg.setWindowTitle("Incomplete value")
                        msg.setText("The phone number must contain 10 digits and starts with 9.")
                        msg.setIcon(QMessageBox.Warning)
                        x=msg.exec()
                    else:
                        self.txtName.setStyleSheet("border: none;")
                        self.txtMobile.setStyleSheet("border: none;")
                        msg = QMessageBox()
                        msg.setWindowTitle("Save data")
                        msg.setText("Do you want to save this to preferences")
                        msg.setIcon(QMessageBox.Question)
                        msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
                        msg.setDefaultButton(QMessageBox.Cancel)
                        msg.buttonClicked.connect(self.save_data)
                        x=msg.exec()
                        
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("Invalid Phone Number")
                    msg.setIcon(QMessageBox.Warning)
                    x=msg.exec()
        else:
            self.txtName.setStyleSheet("border:1px solid red;")
            self.set_error_msg()
    def set_error_msg(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Please fill out the missing field to proceed saving")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        x=msg.exec()
   
    def save_data(self , i): #<--- This will save the data to local temporary storage (not a database)
        self.main = MainWindow()
        val = i.text()
        if(val == "OK"):
            self.main.load_data()
            self.set_success_msg()
            p_name = (self.txtName.text()).lstrip()
            p_room_name =(self.txtRoomName.text()).lstrip()
            p_room_number =(self.txtRoomNumber.text()).lstrip()
            r_mobile_number =(self.txtMobile.text()).lstrip()
            fields = ['Patient_name','room_name','room_number','recipient_mobile']
            data = [[p_name,p_room_name,p_room_number,r_mobile_number]]
            filename = "temp_preferences.csv"
            with open(filename, 'w') as f:
                csvwriter = csv.writer(f)
                csvwriter.writerow(fields)
                csvwriter.writerows(data)
            
            self.update_mainwindow = MainWindow()
            self.update_mainwindow.btnScan.setStyleSheet("background-color: rgb(255, 102, 0); border:none; color:white; icon-size: 53px;")
            self.window_closed.emit()
            self.close_window()
            self.btnSave.setText("Update")
        #.ignore() # call the pyqt signal event
    def set_success_msg(self):
        msg = QMessageBox()
        msg.setWindowTitle("Success")
        msg.setText("Data saved successfully!")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        x=msg.exec()
    def close_window(self):
        self.close()

class Scanner(QWidget):
    def __init__(self):
        super(Scanner,self).__init__()
        loadUi("./src/uiFiles/scanner.ui", self)
        self.btnBack.clicked.connect(self.set_goback_confirmation)
        self.btnRescan.clicked.connect(self.reScan)
        self.btnSend.clicked.connect(self.validationSend)
        self.set_name()
        self.setUiDisabled()
        thread = Thread(self)
        thread.data_sensors.connect(self.update_Sensors)
        thread.start()
    
    def set_name(self):
        pref_data = "temp_preferences.csv"
        with open(pref_data, 'r') as n:
            csv_reader = csv.reader(n)
            for line_no , line in enumerate(csv_reader , 1):
                if line_no == 2:
                    name = (line[0])
                    self.lblName.setText(name)
    def validationSend(self ):
        prefix = "+63"
        pref_data = "temp_preferences.csv"
        with open(pref_data, 'r') as n:
            csv_reader = csv.reader(n)
            for line_no , line in enumerate(csv_reader , 1):
                if line_no == 2:
                    number = (line[3])
        msg = QMessageBox()
        msg.setWindowTitle("Send Data")
        msg.setText("Do you want to send data \n to {}{} phone number?.".format(prefix,number))
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Cancel)
        msg.buttonClicked.connect(self.popup_button)
        x=msg.exec()
    def reScan(self):
        self.setUiDisabled()
    
        
    def setUiDisabled(self):
        #set this button to disable when data is not yet scanned
        self.btnSend.setEnabled(False)
        self.btnRescan.setEnabled(False)
        self.btnNext_2.setEnabled(False)
        self.label_19.setEnabled(False)
        self.label_20.setEnabled(False)
        self.label_21.setEnabled(False)
        self.label_15.setEnabled(False)
        self.label_16.setEnabled(False)
        self.label_17.setEnabled(False)
        self.label_18.setEnabled(False)
        self.btnSend.setStyleSheet("background-color:gray; border:gray")
        self.lblHeartRate.setText("-")
        self.lblRoomTemp.setText("-")
        self.lblOxygenLevel.setText("-")
        self.lblBodyTemp.setText("-")
        self.btnSend.setEnabled(False)
        self.btnNext_2.setEnabled(False)
        self.label.setText("")
        self.label_7.setStyleSheet("background-color:#FFE7D7; border:1px solid #FFE7D7;")
        self.label_9.setStyleSheet("background-color:#FFE7D7; border:1px solid #FFE7D7;")
        self.label_11.setStyleSheet("background-color:#FFE7D7; border:1px solid #FFE7D7;")
        self.lblScanning.setText("Scanning..")
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
                        self.btnSend.setEnabled(True)
                        self.btnNext_2.setEnabled(True)
                        self.btnRescan.setEnabled(True)
                        self.lblScanning.setText("Done Scanning")
                        self.label_11.setStyleSheet("background-color:#FF6600; border:1px solid rgb(255,102,0);")
                        self.btnSend.setStyleSheet("background-color:#FFE2CE; border:2px solid rgb(255,102,0);")
                        self.saveTempData(data)
            else:
                self.lblNotice.setText("please put pressure on the sensor if you want to continue scanning")
                ctr = btnctr + 1
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
    def set_goback_confirmation(self):
        msg = QMessageBox()
        msg.setWindowTitle("go back")
        msg.setText("Do you want to abort the scanning? \n this will reset all the data.")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Cancel)
        msg.buttonClicked.connect(self.go_back)
        x=msg.exec()
        
    def go_back(self , i):
        val = i.text()
        if(val == "OK"):
            print("go back")
            self.back_to_main = MainWindow()
            widget.addWidget(self.back_to_main)
            widget.setCurrentIndex(widget.currentIndex()-1)
            self.reset_values()
            
    def reset_values(self):
        self.setUiDisabled()
        print("values has been reset.")
    def popup_button(self, i):
        
        val = i.text()
        Today = date.today()
        d2day = Today.strftime("%B %d, %Y")
        time = (datetime.today().strftime("%I:%M %p"))
        if(val == "OK"):
            pref_data = "temp_preferences.csv"
            user_data = "temp_user_data.csv"
            with open(pref_data, 'r') as n:
                csv_reader = csv.reader(n)
                for line_no , line in enumerate(csv_reader , 1):
                    if line_no == 2:
                        patient_name = (line[0])
                        room_name = (line[1])
                        room_number = (line[2])
                        num = (line[3])
            with open(user_data, 'r') as r:
                csv_reader = csv.reader(r)
                for line_no , line in enumerate(csv_reader , 1):
                    if line_no == 2:
                        rt = (line[0])
                        bt = (line[1])
                        sp2 = (line[2])
                        hr2 = (line[3])
            name = patient_name
            userData = ("----------------------------------\nDate: {} \nTime: {} \n----------------------------------\nName: {} \nRoom Name: {}\nRoom Number: {}\n----------------------------------\nHeart Rate: {} Bpm\nOxygen Saturation: {}% \nRoom Temp:{} C \nBody Temperature:{} C \n----------------------------------\n\n RTHM DEVICE V1.03.22 BETA"
                .format(
                    d2day,
                    time,
                    name,
                    room_name,
                    room_number,
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
class Sensor_guide(QDialog):
    def __init__(self):
        super(Sensor_guide,self).__init__()
        loadUi("./src/uiFiles/sensor_guide.ui", self)
        movie = QMovie("./src/images/gif/guide1.gif")
        self.labelGif.setMovie(movie)
        movie.start()
        print("test sensor guide")
        self.btnOk.clicked.connect(self.close_window)
        
    def close_window(self):
        self.close()

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