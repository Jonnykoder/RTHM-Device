import tkinter
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.IN)
import max30102
import hrcalc


from smbus2 import SMBus
from mlx90614 import MLX90614
bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)


print("[INFO] MAX30102 Channel & I2C Address.")
m = max30102.MAX30102()
hr2 = 0
sp2 = 0


class App:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

       
        #Label for heart rate
        self.PulseLbl = tkinter.Label(window, text="[Heart Pulse Rate    : ]",font=("Arial", 20), fg = "red",relief="ridge",borderwidth = 2)
        self.PulseLbl.pack(anchor=tkinter.CENTER, expand=True)
        
        #Label for blood Oxygen 
        self.SPO2Lbl = tkinter.Label(window, text="[Oxygen Saturation   : ]",font=("Arial", 20), fg ="blue",relief="ridge",borderwidth = 2)
        self.SPO2Lbl.pack(anchor=tkinter.CENTER, expand=True)
        
         #Label for Ambient Temperature
        self.AmbientTemp = tkinter.Label(window, text="[Ambient Temperature   : ]",font=("Arial", 20), fg ="blue",relief="ridge",borderwidth = 2)
        self.AmbientTemp.pack(anchor=tkinter.CENTER, expand=True)
        
        
         #Label for Target Temp
        self.BodyTemp = tkinter.Label(window, text="[Body Temperature   : ]",font=("Arial", 20), fg ="blue",relief="ridge",borderwidth = 2)
        self.BodyTemp.pack(anchor=tkinter.CENTER, expand=True)
        
       
        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 1
        self.update()

        self.window.mainloop()

 
    def update(self):
        if(GPIO.input(18)==0):
            celcius = sensor.get_object_1();
            faren = (celcius) +4
            ambient = sensor.get_ambient()
            
            
            red, ir = m.read_sequential()
            hr,hrb,sp,spb = hrcalc.calc_hr_and_spo2(ir, red)
            if(hrb == True and hr != -999 and hr < 105):
                hr2 = int(hr)
                #print("Heart Rate : ",hr2)
                self.PulseLbl['text'] = "[Heart Pulse Rate    : "+str(hr2)+"bpm]"
                
                self.BodyTemp['text'] = "[Body Temperature    : "+str(round(faren, 2))+"°C]"
                self.AmbientTemp['text'] = "[Ambient Temperature    : "+str(round(ambient, 2))+"°C]"
                
            if(spb == True and sp != -999 and sp < 100):
                sp2 = int(sp)
                #print("SPO2       : ",sp2)
                self.SPO2Lbl['text'] = "[Oxygen Saturation   : "+str(sp2)+"%]"
               
            else:
                self.PulseLbl['text'] = "[Heart Pulse Rate    : [No Value]"
                self.SPO2Lbl['text'] = " [Oxygen Saturation   : [No Value]"
                self.AmbientTemp['text'] = "[Ambient Temperature    : [No Value]"
                self.BodyTemp['text'] = " [Body Temperature   : [No Value]"
                
        self.window.after(self.delay, self.update)


# Create a window and pass it to the Application object
root = tkinter.Tk()
root.geometry("+{}+{}".format(250, 50))
App(root, "PULSE OXIMETER | BODY TEMPERATURE V1")
