from PyQt5.QtWidgets import QDesktopWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from Name import Ui_nameWindow

class Ui_MainWindow(object):
    def openInputName(self):
        self.window = QtWidgets.QMainWindow()
        self.itself = QtWidgets.QMainWindow() #for this window 
        self.ui = Ui_nameWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.grp1 = QtWidgets.QGroupBox(self.centralwidget)
        self.grp1.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.grp1.setFont(font)
        self.grp1.setTitle("")
        self.grp1.setFlat(False)
        self.grp1.setObjectName("grp1")
        self.label_2 = QtWidgets.QLabel(self.grp1)
        self.label_2.setGeometry(QtCore.QRect(212, 20, 600, 400))
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("/home/pi/Desktop/sensorRead/userInterface/images/homepage2.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(self.grp1)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.frame.setStyleSheet("background-color: #ffffff;")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.btnStart_2 = QtWidgets.QPushButton(self.frame , clicked = lambda: self.openInputName() )
        self.btnStart_2.clicked.connect(MainWindow.close)
        self.btnStart_2.setGeometry(QtCore.QRect(420, 460, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btnStart_2.setFont(font)
        self.btnStart_2.setStyleSheet("background-color: rgb(255, 102, 0);\n"
"border-radius:30px;\n"
"color: #ffffff;")
        self.btnStart_2.setObjectName("btnStart_2")
        self.frame.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnStart_2.setText(_translate("MainWindow", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
