from sim800l import SIM800L
sim800l=SIM800L('/dev/serial0')
name="John"

hr = str(92)
sp02 = str(120)
roomTemp = str(35.2)
bodyTemp = str(34.2)
deg = "C"
userData = ("Name: {} \nHeart Rate: {} Bpm\nOxygen Saturation: {}% \nRoom Temp:{} C \nBody Temperature:{} C"
            .format(
                name,
                hr,
                sp02,
                roomTemp,
                bodyTemp)
            )
print(userData )
sms=("test again")
num = '9155006780' #this will be from the user input
pref = '63'
cp = pref+num
print(cp)
#sim800l.send_sms(dest.no,sms)
sim800l.send_sms(cp,userData)