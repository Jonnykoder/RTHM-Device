#John Eric Azores

import tkinter as tk
from tkinter import *
main = Tk()


cpNum = Entry(main, width=50)
cpNum.pack()



def myClick():
  
    #targetsending
    myLabel = Label(main, text ="Message: \t" + cpNum.get())
    myLabel.pack()
        
myButton = Button(main,text="Send SMS", command=myClick)
myButton.pack()

main.mainloop()
