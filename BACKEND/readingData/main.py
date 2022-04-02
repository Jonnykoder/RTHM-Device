import sys
from PyQt5.uic import loadUi
from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget ,QLabel,QLineEdit
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap


class MainWindow(QDialog):
     def __init__(self, window):
         loadUi("windowStart.ui", self)