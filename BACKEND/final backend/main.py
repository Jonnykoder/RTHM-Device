import max30102
from smbus2 import SMBus
from mlx90614 import MLX90614
import hrcalc
import time
m = max30102.MAX30102()
bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)


celcius = sensor.get_object_1();
faren = (celcius*1.8)+32
room = sensor.get_ambient()
roomTemp = round(room, 2)
bodyTemp = (round(celcius+5,2))


hr2 = 0
sp2 = 0

while True:
    red, ir = m.read_sequential()
    
    hr,hrb,sp,spb = hrcalc.calc_hr_and_spo2(ir, red)

  
    
    if(hrb == True and hr != -999):
        hr2 = int(hr)
        print("--------------------")
        print("Heart Rate : ",hr2)
        print("Body Temp  : ",bodyTemp,"\N{DEGREE SIGN}C")
    if(spb == True and sp != -999):
        sp2 = int(sp)
        print("SPO2       : ",sp2)
        print ("Room Temp  :", roomTemp,u"\N{DEGREE SIGN}C")
        print("--------------------")
    
        time.sleep(8)
        break
       
    else:
        print("No vitals detected.")
        
    
print("result : \n Heart Rate: {} \n Oxygen Level: {} \n Room Temp: {}°C \n Body Temp: {}°C"
      .format(
          hr2,
          sp2,
          roomTemp,
          bodyTemp)
      )
    
