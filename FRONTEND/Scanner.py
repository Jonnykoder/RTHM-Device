# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Desktop\CAPSTONE\RTHM-Device\FRONTEND\Scanner.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(599, 345)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 600, 345))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color:qlineargradient(spread:pad, x1:0.005, y1:0, x2:1, y2:1, stop:0 rgba(200, 197, 191, 255), stop:1 rgba(255, 255, 255, 255))}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(510, 320, 161, 21))
        self.label.setObjectName("label")
        self.btnBack = QtWidgets.QPushButton(self.widget)
        self.btnBack.setGeometry(QtCore.QRect(-40, -20, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btnBack.setFont(font)
        self.btnBack.setStyleSheet("color: #3F3D56;\n"
"background-color: #FFE2CE;\n"
"border-radius: 20px;\n"
"border:1px solid white;\n"
"padding: 4px;\n"
"box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;")
        self.btnBack.setObjectName("btnBack")
        self.lblHeartRate = QtWidgets.QLabel(self.widget)
        self.lblHeartRate.setGeometry(QtCore.QRect(140, 140, 61, 31))
        self.lblHeartRate.setStyleSheet("color: #594646;")
        self.lblHeartRate.setObjectName("lblHeartRate")
        self.lblOxygenLevel = QtWidgets.QLabel(self.widget)
        self.lblOxygenLevel.setGeometry(QtCore.QRect(140, 210, 61, 31))
        self.lblOxygenLevel.setStyleSheet("color: #594646;")
        self.lblOxygenLevel.setObjectName("lblOxygenLevel")
        self.lblBodyTemp = QtWidgets.QLabel(self.widget)
        self.lblBodyTemp.setGeometry(QtCore.QRect(410, 130, 61, 31))
        self.lblBodyTemp.setStyleSheet("color: #594646;")
        self.lblBodyTemp.setObjectName("lblBodyTemp")
        self.lblRoomTemp = QtWidgets.QLabel(self.widget)
        self.lblRoomTemp.setGeometry(QtCore.QRect(410, 220, 61, 31))
        self.lblRoomTemp.setStyleSheet("color: #594646;")
        self.lblRoomTemp.setObjectName("lblRoomTemp")
        self.lblName = QtWidgets.QLabel(self.widget)
        self.lblName.setGeometry(QtCore.QRect(440, 10, 191, 31))
        self.lblName.setStyleSheet("color: #594646;")
        self.lblName.setObjectName("lblName")
        self.lblNamePlaceholder = QtWidgets.QLabel(self.widget)
        self.lblNamePlaceholder.setGeometry(QtCore.QRect(430, 10, 171, 31))
        self.lblNamePlaceholder.setStyleSheet("background-color:#FFB17D;")
        self.lblNamePlaceholder.setText("")
        self.lblNamePlaceholder.setObjectName("lblNamePlaceholder")
        self.lblSHeart = QtWidgets.QLabel(self.widget)
        self.lblSHeart.setGeometry(QtCore.QRect(60, 70, 210, 210))
        self.lblSHeart.setFrameShape(QtWidgets.QFrame.Box)
        self.lblSHeart.setText("")
        self.lblSHeart.setObjectName("lblSHeart")
        self.lblSTemp = QtWidgets.QLabel(self.widget)
        self.lblSTemp.setGeometry(QtCore.QRect(330, 70, 210, 210))
        self.lblSTemp.setStyleSheet("")
        self.lblSTemp.setFrameShape(QtWidgets.QFrame.Box)
        self.lblSTemp.setText("")
        self.lblSTemp.setObjectName("lblSTemp")
        self.btnNext = QtWidgets.QPushButton(self.widget)
        self.btnNext.setGeometry(QtCore.QRect(415, 290, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btnNext.setFont(font)
        self.btnNext.setStyleSheet("color: #3F3D56;\n"
"background-color: #FFE2CE;\n"
"border-radius: 20px;\n"
"border:1px solid white;\n"
"padding: 4px;\n"
"box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;")
        self.btnNext.setObjectName("btnNext")
        self.lblSTemp.raise_()
        self.lblSHeart.raise_()
        self.lblNamePlaceholder.raise_()
        self.label.raise_()
        self.btnBack.raise_()
        self.lblHeartRate.raise_()
        self.lblOxygenLevel.raise_()
        self.lblBodyTemp.raise_()
        self.lblRoomTemp.raise_()
        self.lblName.raise_()
        self.btnNext.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "RTHM-Scanner"))
        self.label.setText(_translate("Dialog", "RTHM DEVICE V1."))
        self.btnBack.setToolTip(_translate("Dialog", "<html><head/><body><p>GO BACK TO HOME</p></body></html>"))
        self.btnBack.setText(_translate("Dialog", "Back "))
        self.lblHeartRate.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Null</span></p></body></html>"))
        self.lblOxygenLevel.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Null</span></p></body></html>"))
        self.lblBodyTemp.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Null</span></p></body></html>"))
        self.lblRoomTemp.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Null</span></p></body></html>"))
        self.lblName.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Null</span></p></body></html>"))
        self.btnNext.setToolTip(_translate("Dialog", "<html><head/><body><p>NEXT SCREEN</p></body></html>"))
        self.btnNext.setText(_translate("Dialog", "    Next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())