import sys
from PyQt5.uic import loadUi
from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget ,QLabel,QLineEdit
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
import sys

import max30102
import hrcalc
print("[INFO] MAX30102 Channel & I2C Address.")
m = max30102.MAX30102()
hr2 = 0
sp2 = 0

class Thread(QtCore.QThread):
    data_sensors = QtCore.pyqtSignal(tuple)

    def run(self):
        while True:
            red, ir = m.read_sequential()
            hr,hrb,sp,spb = hrcalc.calc_hr_and_spo2(ir, red)
            self.data_sensors.emit((hr,sp,hrb,spb))
class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("trialUi.ui", self)
         
        thread = Thread(self)
        thread.data_sensors.connect(self.update_Sensors)
        thread.start()
        
    def update_Sensors(self, data):
        hr, sp , hrb , spb = data
        hr2 = int(hr)
        sp2 = int(sp)
        if(hrb == True and spb ==True):
            if(hr != -999 and hr<105):
                self.PulseLbl.setText(str(hr2) + "Bpm")
                print("heart rate:" + str(hr2))
            if(sp != -999 and sp < 100):
                print("Oxygen Saturation :" + str(sp2))
                self.SPO2Lbl.setText(str(sp2) + "%")
        else:
            print("vitals not detected..")
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