# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Scanning.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblBackground = QtWidgets.QLabel(self.centralwidget)
        self.lblBackground.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.lblBackground.setStyleSheet("background-color: #ffffff;")
        self.lblBackground.setText("")
        self.lblBackground.setScaledContents(False)
        self.lblBackground.setObjectName("lblBackground")
        self.lblTemp = QtWidgets.QLabel(self.centralwidget)
        self.lblTemp.setGeometry(QtCore.QRect(530, 100, 400, 400))
        self.lblTemp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblTemp.setText("")
        self.lblTemp.setPixmap(QtGui.QPixmap("images/TempHeart3.png"))
        self.lblTemp.setScaledContents(True)
        self.lblTemp.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTemp.setObjectName("lblTemp")
        self.btnBack = QtWidgets.QLabel(self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(-20, -11, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btnBack.setFont(font)
        self.btnBack.setStyleSheet("background-color: rgb(255, 226, 206);\n"
"border-radius:20px;")
        self.btnBack.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.btnBack.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.btnBack.setObjectName("btnBack")
        self.lblName = QtWidgets.QLabel(self.centralwidget)
        self.lblName.setGeometry(QtCore.QRect(880, 0, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lblName.setFont(font)
        self.lblName.setStyleSheet("border-radius:20px;")
        self.lblName.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblName.setAlignment(QtCore.Qt.AlignCenter)
        self.lblName.setObjectName("lblName")
        self.lblBpm = QtWidgets.QLabel(self.centralwidget)
        self.lblBpm.setGeometry(QtCore.QRect(90, 290, 400, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lblBpm.setFont(font)
        self.lblBpm.setStyleSheet("color: #594646;")
        self.lblBpm.setAlignment(QtCore.Qt.AlignCenter)
        self.lblBpm.setObjectName("lblBpm")
        self.lblSpO2 = QtWidgets.QLabel(self.centralwidget)
        self.lblSpO2.setGeometry(QtCore.QRect(90, 350, 400, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lblSpO2.setFont(font)
        self.lblSpO2.setStyleSheet("color: #594646;")
        self.lblSpO2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSpO2.setObjectName("lblSpO2")
        self.lblBtemp = QtWidgets.QLabel(self.centralwidget)
        self.lblBtemp.setGeometry(QtCore.QRect(530, 245, 400, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lblBtemp.setFont(font)
        self.lblBtemp.setStyleSheet("color: #594646;")
        self.lblBtemp.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lblBtemp.setObjectName("lblBtemp")
        self.lblRtemp = QtWidgets.QLabel(self.centralwidget)
        self.lblRtemp.setGeometry(QtCore.QRect(530, 345, 371, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lblRtemp.setFont(font)
        self.lblRtemp.setStyleSheet("color: #594646;")
        self.lblRtemp.setAlignment(QtCore.Qt.AlignCenter)
        self.lblRtemp.setObjectName("lblRtemp")
        self.lblHeart = QtWidgets.QLabel(self.centralwidget)
        self.lblHeart.setGeometry(QtCore.QRect(90, 100, 400, 400))
        self.lblHeart.setText("")
        self.lblHeart.setPixmap(QtGui.QPixmap("images/loading_heart(2).png"))
        self.lblHeart.setScaledContents(True)
        self.lblHeart.setObjectName("lblHeart")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 13, 35, 35))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/angle-left2.png"))
        self.label_2.setObjectName("label_2")
        self.lblBackground.raise_()
        self.lblHeart.raise_()
        self.lblTemp.raise_()
        self.btnBack.raise_()
        self.lblName.raise_()
        self.lblBpm.raise_()
        self.lblSpO2.raise_()
        self.lblBtemp.raise_()
        self.lblRtemp.raise_()
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
        self.btnBack.setText(_translate("MainWindow", "Back  "))
        self.lblName.setText(_translate("MainWindow", "Renj"))
        self.lblBpm.setText(_translate("MainWindow", "120 Bpm"))
        self.lblSpO2.setText(_translate("MainWindow", "98 SpO2"))
        self.lblBtemp.setText(_translate("MainWindow", "36°C"))
        self.lblRtemp.setText(_translate("MainWindow", "30°C"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())