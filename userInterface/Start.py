
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def openInputName(self):
        self.window = QtWidgets.QMainWindow()
        
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
        self.btnStart = QtWidgets.QLabel(self.grp1)
        self.btnStart.setGeometry(QtCore.QRect(387, 440, 250, 90))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btnStart.setFont(font)
        self.btnStart.setStyleSheet("background-color: rgb(255, 102, 0);\n"
"border-radius:30px;\n"
"color: #ffffff;")
        self.btnStart.setFrameShape(QtWidgets.QFrame.Box)
        self.btnStart.setAlignment(QtCore.Qt.AlignCenter)
        self.btnStart.setObjectName("btnStart")
        self.label_2 = QtWidgets.QLabel(self.grp1)
        self.label_2.setGeometry(QtCore.QRect(212, 20, 600, 400))
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/homepage2.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(self.grp1)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.frame.setStyleSheet("background-color: #ffffff;")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.btnStart.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 26))
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
        self.btnStart.setText(_translate("MainWindow", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
