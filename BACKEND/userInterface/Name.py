

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_nameWindow(object):
    def setupUi(self, nameWindow):
        nameWindow.setObjectName("nameWindow")
        nameWindow.resize(1024, 600)
        self.centralwidget = QtWidgets.QWidget(nameWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblBackground = QtWidgets.QLabel(self.centralwidget)
        self.lblBackground.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.lblBackground.setStyleSheet("background-color: #ffffff;")
        self.lblBackground.setText("")
        self.lblBackground.setScaledContents(True)
        self.lblBackground.setObjectName("lblBackground")
        self.btnHome = QtWidgets.QLabel(self.centralwidget)
        self.btnHome.setGeometry(QtCore.QRect(-20, -11, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btnHome.setFont(font)
        self.btnHome.setStyleSheet("background-color: rgb(255, 102, 0);\n"
"background-color: rgb(255, 226, 206);\n"
"border-radius:20px;")
        self.btnHome.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.btnHome.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.btnHome.setObjectName("btnHome")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 90, 781, 331))
        self.label_3.setStyleSheet("background-color: #E5E5E5;\n"
"border-radius:30px;")
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.lblWhat = QtWidgets.QLabel(self.centralwidget)
        self.lblWhat.setGeometry(QtCore.QRect(120, 130, 781, 100))
        font = QtGui.QFont()
        font.setPointSize(38)
        font.setBold(True)
        font.setWeight(75)
        self.lblWhat.setFont(font)
        self.lblWhat.setAlignment(QtCore.Qt.AlignCenter)
        self.lblWhat.setObjectName("lblWhat")
        self.txtName = QtWidgets.QTextEdit(self.centralwidget)
        self.txtName.setGeometry(QtCore.QRect(202, 270, 621, 70))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.txtName.setFont(font)
        self.txtName.setStyleSheet("font-size: 26;")
        self.txtName.setObjectName("txtName")
        self.lblHome = QtWidgets.QLabel(self.centralwidget)
        self.lblHome.setGeometry(QtCore.QRect(10, 13, 35, 35))
        self.lblHome.setText("")
        self.lblHome.setPixmap(QtGui.QPixmap("D:\\Desktop\\CAPSTONE\\RTHM-Device\\userInterface\\designerFiles\\images/home2.png"))
        self.lblHome.setScaledContents(True)
        self.lblHome.setObjectName("lblHome")
        self.btnScan = QtWidgets.QPushButton(self.centralwidget)
        self.btnScan.setGeometry(QtCore.QRect(410, 460, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btnScan.setFont(font)
        self.btnScan.setStyleSheet("background-color: rgb(255, 102, 0);\n"
"border-radius:30px;\n"
"color: #ffffff;")
        self.btnScan.setObjectName("btnScan")
        nameWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(nameWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        nameWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(nameWindow)
        self.statusbar.setObjectName("statusbar")
        nameWindow.setStatusBar(self.statusbar)

        self.retranslateUi(nameWindow)
        QtCore.QMetaObject.connectSlotsByName(nameWindow)

    def retranslateUi(self, nameWindow):
        _translate = QtCore.QCoreApplication.translate
        nameWindow.setWindowTitle(_translate("nameWindow", "MainWindow"))
        self.btnHome.setText(_translate("nameWindow", "Home "))
        self.lblWhat.setText(_translate("nameWindow", "What is your name?"))
        self.txtName.setHtml(_translate("nameWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btnScan.setText(_translate("nameWindow", "Scan"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    nameWindow = QtWidgets.QMainWindow()
    ui = Ui_nameWindow()
    ui.setupUi(nameWindow)
    nameWindow.show()
    sys.exit(app.exec_())
