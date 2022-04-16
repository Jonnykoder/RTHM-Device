from json import load
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

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("./src/uiFilesV2/mainWindow.ui", self)
        self.btnPreferences.clicked.connect(self.view_preferences)   #set method to the button preferences
        self.btnScan.clicked.connect(self.goto_scanner)
        
        self.load_data()
    def goto_scanner(self):
        
        print("scanner enabled")
        self.scanner = Scanner()
        widget.addWidget(self.scanner)
        #self.set_notice_msg()  <---reserved
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.view_guide()
        
    def view_preferences(self):
        self.preferences = Preferences()
        self.preferences.window_closed.connect(self.load_data)
        self.preferences.show()
        
    def view_guide(self):
        self.show_guide = Sensor_guide()
        self.show_guide.show()
    """
    def set_notice_msg (self):   <---reserved
        msg = QMessageBox()
        msg.setWindowTitle("Notice")
        msg.setText("Please put your finger on the scanner.")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        x=msg.exec()
    """
    def load_data(self):
        filename = ".temp_preferences.csv"
        try:
            with open(filename, 'r') as r:
                csv_reader = csv.reader(r)
                for line_no , line in enumerate(csv_reader , 1):
                    if line_no == 3:
                        #print(line[0])
                        self.name = (line[0])
                        self.recipient =(line[3])
                        if (self.name != "" and self.recipient !=""):
                            print("================================\n|\tData loaded.... \t|\n================================")
                            self.btnScan.setEnabled(True)
                            self.btnScan.setStyleSheet("background-color: rgb(255, 102, 0); border:none; color:white; icon-size: 53px;")
                            self.pref = Preferences()
                            self.pref.btnSave.setText("Update")
                        else:
                            print("================================\n|\tData Missing.... \t|\n================================")
                            self.btnScan.setEnabled(False)
                            self.btnScan.setStyleSheet("background-color: #FF954F; border:none; icon-size: 53px;")
        except IOError: 
            print("========================================\n| Data not found, button is disabled....|\n========================================")   
        if not filename:
            raise ValueError('No data available')
        return filename
class Preferences(QDialog):
    window_closed = pyqtSignal()
    def __init__(self):
        super(Preferences,self).__init__()
        loadUi("./src/uiFilesV2/preferences.ui", self)  # <--import preferences ui file
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
        val = i.text()
        if(val == "OK"):
            self.set_success_msg()
            p_name = (self.txtName.text()).lstrip()
            p_room_name =(self.txtRoomName.text()).lstrip()
            p_room_number =(self.txtRoomNumber.text()).lstrip()
            r_mobile_number =(self.txtMobile.text()).lstrip()
            fields = ['Patient_name','room_name','room_number','recipient_mobile']
            data = [[p_name,p_room_name,p_room_number,r_mobile_number]]
            filename = ".temp_preferences.csv"
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
    window_open = pyqtSignal()
    def __init__(self):
        super(Scanner,self).__init__()
        loadUi("./src/uiFilesV2/scanner.ui", self)
        self.btnBack.clicked.connect(self.set_goback_confirmation)
        self.window_open.emit()
        self.load_data()
        
    def load_data(self):
        
        filename = ".temp_preferences.csv"
        try:
            with open(filename, 'r') as r:
                csv_reader = csv.reader(r)
                for line_no , line in enumerate(csv_reader , 1):
                    if line_no == 3:
                      
                        self.name = (line[0])
                        self.room_name = (line[1])
                        self.room_no = (line[2])
                        self.recipient = (line[3])
                        if (self.name != ""):
                            print("Data loaded on scanner")
                            self.lblName.setText(self.name)
        except IOError: 
            print("========================================\n| Data not found, button is disabled....|\n========================================")   
        if not filename:
            raise ValueError('No data available')
        return filename
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
            print("values has been reset.")
            
class Sensor_guide(QDialog):
    def __init__(self):
        super(Sensor_guide,self).__init__()
        loadUi("./src/uiFilesV2/sensor_guide.ui", self)
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