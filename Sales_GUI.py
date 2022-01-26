from tkinter import *
from tkinter import messagebox
import time
from datetime import datetime
import random

# Tkinter GUI Window
window = Tk()
header = Label(window, text="Vehicle Sales Management System")
header.place(x=15, y=22)


def submit_sale():
    # using get() method to get values from entries in right frame
    # Vehicle entries
    e1 = (regE.get())
    e2 = (mlgE.get())
    e3 = (makeE.get())
    e4 = (modelE.get())
    e5 = (engE.get())
    
    # Customer entries
    e6 = (nameE.get())
    e7 = (addrE.get())
    e8 = (postE.get())
    e9 = (phoneE.get())
    e10 = (emailE.get())
    
    # Vehicle cost entries
    e11 = (costE.get())
    e12 = (warrE.get())
    e13 = (additE.get()) 
    
    rules = [
        # Length of all entries are > 0
        len(e1) > 0, len(e2) > 0,
        len(e3) > 0, len(e4) > 0,
        len(e5) > 0, len(e6) > 0,
        len(e7) > 0, len(e8) > 0,
        len(e9) > 0, len(e10) > 0,
        len(e11) > 0, len(e12) > 0,
        len(e13) > 0
    ]
    
    if all(rules) == True:
        # If all entries are filled and not left empty
        receipt = messagebox.askyesno(title="Submission Successful", message="Would you like to print receipt?")
        if receipt == True:
            time.sleep(1)
            
            right_F = Frame(window, 
                            width=285, 
                            heigh=435, 
                            highlightbackground="lightgrey", 
                            highlightthickness=0.5,
                            bg="grey90")
            right_F.place(x=650, y= 50)

            # Designing the receipt in right frame
            line1 = Label(right_F, text="==================================", bg="grey90")
            line1.place(x=1, y=2)

            lab1 = Label(right_F, text="Auto Overdrive", bg="grey90")
            lab1.place(x=1, y=18)
            
            lab2 = Label(right_F, text="Invoive num:", bg="grey90")
            lab2.place(x=1, y=36)
            
            # Creating transaction number with first index of entries (cust name & reg)
            num = range(1, 10)
            for x in num:
                y = (random.randint(1000000, 9000000))
            tranc = e1[0:2].upper() + e6[0].upper() + str(y)
            
            lab2_tranc = Label(right_F, text=tranc, bg="grey90")
            lab2_tranc.place(x=180, y=36)

            lab3 = Label(right_F, text="Cust name:", bg="grey90")
            lab3.place(x=1, y=54)
            
            lab3_get = Label(right_F, text=e6, bg="grey90")
            lab3_get.place(x=180, y=54)

            line2 = Label(right_F, text="==================================", bg="grey90")
            line2.place(x=1, y=70)
            
            lab4 = Label(right_F, text="Registration:", bg="grey90")
            lab4.place(x=1, y=88)
            
            lab4_get = Label(right_F, text=e1, bg="grey90")
            lab4_get.place(x=180, y=88)

            lab5 = Label(right_F, text="Make:", bg="grey90")
            lab5.place(x=1, y=106)

            lab5_get = Label(right_F, text=e3, bg="grey90")
            lab5_get.place(x=180, y=106)
            
            line3 = Label(right_F, text="------------------------------------------------------", bg="grey90")
            line3.place(x=1, y=124)
            
            ttl1 = Label(right_F, text="Vehicle Cost:", bg="grey90")
            ttl1.place(x=1, y=142)

            ttl1_get = Label(right_F, text=e11, bg="grey90")
            ttl1_get.place(x=180, y=142)
            
            ttl2 = Label(right_F, text="Warranty Cost:", bg="grey90")
            ttl2.place(x=1, y=160)

            ttl2_get = Label(right_F, text=e12, bg="grey90")
            ttl2_get.place(x=180, y=160)
            
            ttl3 = Label(right_F, text="Additional Cost:", bg="grey90")
            ttl3.place(x=1, y=178)

            ttl3_get = Label(right_F, text=e13, bg="grey90")
            ttl3_get.place(x=180, y=178)
    
            ttl4 = Label(right_F, text="Total Cost:", bg="grey90", font="Arial 10")
            ttl4.place(x=1, y=196)
            
            # Calculating total costs
            ttl4_get = Label(right_F, text= int(e11) + int(e12) + int(e13), bg="grey90")
            ttl4_get.place(x=180, y=196)
            
            line4 = Label(right_F, text="------------------------------------------------------", bg="grey90")
            line4.place(x=1, y=214)
            
            # Importing current datetime using datetime library
            current_time = datetime.now()
            c_time = current_time.strftime("%H:%M:%S")
            c_date = current_time.strftime("%d/%m/%Y")
            
            dateL = Label(right_F, text="Date:", bg="grey90")
            dateL.place(x=1, y=232)
        
            date_get = Label(right_F, text=c_date, bg="grey90")
            date_get.place(x=180, y=232)
  
            timeL = Label(right_F, text="Time:", bg="grey90")
            timeL.place(x=1, y=250)
           
            time_get = Label(right_F, text=c_time, bg="grey90")
            time_get.place(x=180, y=250)

            line5 = Label(right_F, text="==================================", bg="grey90")
            line5.place(x=1, y=268)

            endL = Label(right_F, text=f"Thank you {e6}\nfor shopping at Auto Overdrive.", bg="grey90", font="Arial 12")
            endL.place(x=30, y=310)
            
            line6 = Label(right_F, text="==================================", bg="grey90")
            line6.place(x=1, y=372)
            
        else:
            pass   
    else:
        # If one or more entries are left empty
        messagebox.showerror(title="Missing Entries", message="Please fill in all entries")
        
        
def clear_sale():
    # This function will clear all entries
    regE.delete(0, "end")
    mlgE.delete(0, "end")
    makeE.delete(0, "end")
    modelE.delete(0, "end")
    engE.delete(0, "end")
    nameE.delete(0, "end")
    addrE.delete(0, "end")
    postE.delete(0, "end")
    phoneE.delete(0, "end")
    emailE.delete(0, "end")
    costE.delete(0, "end")
    warrE.delete(0, "end")
    additE.delete(0, "end")
    
    
'''
Left Frame Details -----------------------
'''

# Left Frame
leftF = Frame(window, width=620, height=350, highlightbackground="lightgrey")
leftF.place(x=15, y=50)

# Registration
regL = Label(leftF, text="Vehicle Registration:")
regL.place(x=1, y=8)

regE = Entry(leftF, width=22, bg="grey100")
regE.place(x=140, y=10)

# Milage
mlgL = Label(leftF, text="Vehicle Milage:")
mlgL.place(x=1, y=38)

mlgE = Entry(leftF, width=22, bg="grey100")
mlgE.place(x=140, y=40)

# Make
makeL = Label(leftF, text="Vehicle Make:")
makeL.place(x=1, y=68)

makeE = Entry(leftF, width=22, bg="grey100")
makeE.place(x=140, y=70)

# Model
modelL = Label(leftF, text="Vehicle Model:")
modelL.place(x=1, y=98)

modelE = Entry(leftF, width=22, bg="grey100")
modelE.place(x=140, y=100)

# Engine Number
engL = Label(leftF, text="Engine Number:")
engL.place(x=1, y=128)

engE = Entry(leftF, width=22, bg="grey100")
engE.place(x=140, y=130)

# Customer header
custL = Label(leftF, text="Customer Details")
custL.place(x=1, y=158)

# Fullname
nameL = Label(leftF, text="Full Name:")
nameL.place(x=1, y=188)

nameE = Entry(leftF, width=22, bg="grey100")
nameE.place(x=140, y=190)

# Address
addrL = Label(leftF, text="Address:")
addrL.place(x=1, y=218)

addrE = Entry(leftF, width=22, bg="grey100")
addrE.place(x=140, y=220)

# Postcode
postL = Label(leftF, text="Postcode:")
postL.place(x=1, y=248)

postE = Entry(leftF, width=22, bg="grey100")
postE.place(x=140, y=250)

# Telephone
phoneL = Label(leftF, text="Contact Details:")
phoneL.place(x=1, y=278)

phoneE = Entry(leftF, width=22, bg="grey100")
phoneE.place(x=140, y=280)

# Email
emailL = Label(leftF, text="Email Address:")
emailL.place(x=1, y=308)

emailE = Entry(leftF, width=22, bg="grey100")
emailE.place(x=140, y=310)

# Vehicle Costs
costL = Label(leftF, text="Vehicle Cost:")
costL.place(x=300, y=8)

costE = Entry(leftF, width=22, bg="grey100")
costE.place(x=440, y=10)

# Warranty Costs
warrL = Label(leftF, text="Warranty Cost:")
warrL.place(x=300, y=38)

warrE = Entry(leftF, width=22, bg="grey100")
warrE.place(x=440, y=40)

# Additional Costs
additL = Label(leftF, text="Additional Costs:")
additL.place(x=300, y=68)

additE = Entry(leftF, width=22, bg="grey100")
additE.place(x=440, y=70)

# Notes Label
notesL = Label(leftF, text="Add Notes (Optional Field)")
notesL.place(x=300, y=158)

noteT = Text(leftF, height=8, width=38, bg="grey100")
noteT.place(x=300, y=190)

'''
Right Frame Receipt -----------------------
'''

# Right Frame
rightF = Frame(window, 
               width=285, 
               heigh=435, 
               highlightbackground="lightgrey", 
               highlightthickness=0.5,
               bg="grey90")
rightF.place(x=650, y= 50)

'''
Bottom Frame Buttons -----------------------
'''

# Bottom Frame
bottomF = Frame(window, width=620, heigh=70, highlightthickness=0.5, bd=2)
bottomF.place(x=15, y=415)

btn1 = Button(bottomF, width=18, height=2, text="Submit Sale", bg="grey90", command=submit_sale)
btn1.place(x=0, y=10)

btn2 = Button(bottomF, width=18, height=2, text="Clear Sale", bg="grey90", command=clear_sale)
btn2.place(x=160, y=10)

'''
btn3 = Button(bottomF, width=18, height=2, text="", bg="grey90")
btn3.place(x=320, y=10)

btn4 = Button(bottomF, width=18, height=2, text="", bg="grey90")
btn4.place(x=480, y=10)

'''

'''
window configs -----------------------
'''

# window configurations
window.geometry("950x500")
window.resizable(0, 0)
window.title("Arsalon's Vehicle Management System")
window.attributes("-topmost", True)
window.mainloop()
