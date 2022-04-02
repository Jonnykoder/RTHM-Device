#python sms sending
#John Eric Azores
import serial
import RPi.GPIO as GPIO      
import os, time

#Init serial port
ser = serial.Serial()
GPIO.setmode(GPIO.BOARD)    
 
# Enable Serial Communication via serial0
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)
 
# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key
 
port.write('AT'+'\r\n')
rcv = port.read(10)
time.sleep(1)
 
port.write('ATE0'+'\r\n')      # Disable the Echo
rcv = port.read(10)
print (rcv)
time.sleep(1)
 
port.write('AT+CMGF=1'+'\r\n')  # Select Message format as Text mode 
rcv = port.read(10)
time.sleep(1)

 
# Set number
port.write('AT+CMGS="+639155006780"'+'\r\n')
rcv = port.read(10)
time.sleep(1)
 
port.write('Hello User'+'\r\n')  # Message <----
rcv = port.read(10)
 
port.write("\x1A") # Enable to send SMS

for i in range(10):
    rcv = port.read(10)
    print (rcv)