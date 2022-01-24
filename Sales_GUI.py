from tkinter import Tk
from tkinter import *
from tkinter import messagebox
import time
from datetime import datetime

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
        len(e1) > 0,
        len(e2) > 0,
        len(e3) > 0,
        len(e4) > 0,
        len(e5) > 0,
        len(e6) > 0,
        len(e7) > 0,
        len(e8) > 0,
        len(e9) > 0,
        len(e10) > 0,
        len(e11) > 0,
        len(e12) > 0,
        len(e13) > 0,
    ]
    
    if all(rules):
        # If all entries are filled and not left empty
        receipt = messagebox.askyesno(title="Submission Successful", message="Would you like to print receipt?")
        if receipt == True:
            time.sleep(1)
            
            right_F = Frame(window, 
                            width=285, 
                            heigh=435, 
                            highlightbackground="lightgrey", 
                            highlightthickness=0.5,
                            bg="white")
            right_F.place(x=650, y= 50)

            line1 = Label(right_F, text="==================================", bg="white")
            line1.place(x=1, y=2)

            lab1 = Label(right_F, text="Auto Overdrive", bg="white")
            lab1.place(x=1, y=18)

            lab2 = Label(right_F, text="Invoive num:", bg="white")
            lab2.place(x=1, y=36)

            lab3 = Label(right_F, text="Cust name:", bg="white")
            lab3.place(x=1, y=54)
            
            lab3_get = Label(right_F, text=e6, bg="white")
            lab3_get.place(x=180, y=54)

            line2 = Label(right_F, text="==================================", bg="white")
            line2.place(x=1, y=70)
            
            lab4 = Label(right_F, text="Registration:", bg="white")
            lab4.place(x=1, y=88)
            
            lab4_get = Label(right_F, text=e1, bg="white")
            lab4_get.place(x=180, y=88)

            lab5 = Label(right_F, text="Make:", bg="white")
            lab5.place(x=1, y=106)

            lab5_get = Label(right_F, text=e3, bg="white")
            lab5_get.place(x=180, y=106)
            
            line3 = Label(right_F, text="------------------------------------------------------", bg="white")
            line3.place(x=1, y=124)
            
            ttl1 = Label(right_F, text="Vehicle Cost:", bg="white")
            ttl1.place(x=1, y=142)

            ttl1_get = Label(right_F, text=e11, bg="white")
            ttl1_get.place(x=180, y=142)
            
            ttl2 = Label(right_F, text="Warranty Cost:", bg="white")
            ttl2.place(x=1, y=160)

            ttl2_get = Label(right_F, text=e12, bg="white")
            ttl2_get.place(x=180, y=160)
            
            ttl3 = Label(right_F, text="Additional Cost:", bg="white")
            ttl3.place(x=1, y=178)

            ttl3_get = Label(right_F, text=e13, bg="white")
            ttl3_get.place(x=180, y=178)
    
            ttl4 = Label(right_F, text="Total Cost:", bg="white", font="Arial 10")
            ttl4.place(x=1, y=196)
            
            # Calculating total costs
            ttl4_get = Label(right_F, text= int(e11) + int(e12) + int(e13), bg="white")
            ttl4_get.place(x=180, y=196)
            
            line4 = Label(right_F, text="------------------------------------------------------", bg="white")
            line4.place(x=1, y=214)

            
            
            current_time = datetime.now()
            c_time = current_time.strftime("%H:%M:%S")
            c_date = current_time.strftime("%d/%m/%Y")
            
            dateL = Label(right_F, text="Date:", bg="white")
            dateL.place(x=1, y=232)
        
            date_get = Label(right_F, text=c_date, bg="white")
            date_get.place(x=180, y=232)

            
            timeL = Label(right_F, text="Time:", bg="white")
            timeL.place(x=1, y=250)
           
            time_get = Label(right_F, text=c_time, bg="white")
            time_get.place(x=180, y=250)

            
            
            
            line5 = Label(right_F, text="==================================", bg="white")
            line5.place(x=1, y=268)

            endL = Label(right_F, text=f"Thank you {e6}\nfor shopping at Auto Overdrive.", bg="white", font="Arial 12")
            endL.place(x=30, y=310)
            
            line6 = Label(right_F, text="==================================", bg="white")
            line6.place(x=1, y=372)
            
        else:
            pass   
    else:
        # If one or more entries are left empty
        messagebox.showerror(title="Missing Entries", message="Please fill in all entries")
        
        
'''
Left Frame Details -----------------------
'''

# Left Frame
leftF = Frame(window, width=620, height=350, highlightbackground="lightgrey")
leftF.place(x=15, y=50)

# Registration
regL = Label(leftF, text="Vehicle Registration:")
regL.place(x=1, y=8)

regE = Entry(leftF, width=22, bg="lightgrey")
regE.place(x=140, y=10)

# Milage
mlgL = Label(leftF, text="Vehicle Milage:")
mlgL.place(x=1, y=38)

mlgE = Entry(leftF, width=22, bg="lightgrey")
mlgE.place(x=140, y=40)

# Make
makeL = Label(leftF, text="Vehicle Make:")
makeL.place(x=1, y=68)

makeE = Entry(leftF, width=22, bg="lightgrey")
makeE.place(x=140, y=70)

# Model
modelL = Label(leftF, text="Vehicle Model:")
modelL.place(x=1, y=98)

modelE = Entry(leftF, width=22, bg="lightgrey")
modelE.place(x=140, y=100)

# Engine Number
engL = Label(leftF, text="Engine Number:")
engL.place(x=1, y=128)

engE = Entry(leftF, width=22, bg="lightgrey")
engE.place(x=140, y=130)

# Customer header
custL = Label(leftF, text="Customer Details")
custL.place(x=1, y=158)

# Fullname
nameL = Label(leftF, text="Full Name:")
nameL.place(x=1, y=188)

nameE = Entry(leftF, width=22, bg="lightgrey")
nameE.place(x=140, y=190)

# Address
addrL = Label(leftF, text="Address:")
addrL.place(x=1, y=218)

addrE = Entry(leftF, width=22, bg="lightgrey")
addrE.place(x=140, y=220)

# Postcode
postL = Label(leftF, text="Postcode:")
postL.place(x=1, y=248)

postE = Entry(leftF, width=22, bg="lightgrey")
postE.place(x=140, y=250)

# Telephone
phoneL = Label(leftF, text="Contact Details:")
phoneL.place(x=1, y=278)

phoneE = Entry(leftF, width=22, bg="lightgrey")
phoneE.place(x=140, y=280)

# Email
emailL = Label(leftF, text="Email Address:")
emailL.place(x=1, y=308)

emailE = Entry(leftF, width=22, bg="lightgrey")
emailE.place(x=140, y=310)

# Vehicle Costs
costL = Label(leftF, text="Vehicle Cost:")
costL.place(x=300, y=8)

costE = Entry(leftF, width=22, bg="lightgrey")
costE.place(x=440, y=10)

# Warranty Costs
warrL = Label(leftF, text="Warranty Cost:")
warrL.place(x=300, y=38)

warrE = Entry(leftF, width=22, bg="lightgrey")
warrE.place(x=440, y=40)

# Additional Costs
additL = Label(leftF, text="Additional Costs:")
additL.place(x=300, y=68)

additE = Entry(leftF, width=22, bg="lightgrey")
additE.place(x=440, y=70)

# Notes Label
notesL = Label(leftF, text="Add Notes")
notesL.place(x=300, y=158)

noteT = Text(leftF, height=8, width=38, bg="lightgrey")
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
               bg="white")
rightF.place(x=650, y= 50)

'''
Bottom Frame Buttons -----------------------
'''

# Bottom Frame
bottomF = Frame(window, width=620, heigh=70, highlightbackground="lightgrey", highlightthickness=0.5, bd=2)
bottomF.place(x=15, y=415)

btn1 = Button(bottomF, width=18, height=2, text="Complete Sale", bg="lightgrey", command=submit_sale)
btn1.place(x=0, y=10)

btn2 = Button(bottomF, width=18, height=2, text="Button 2", bg="lightgrey")
btn2.place(x=160, y=10)

btn3 = Button(bottomF, width=18, height=2, text="Button 3", bg="lightgrey")
btn3.place(x=320, y=10)

btn4 = Button(bottomF, width=18, height=2, text="Button 4", bg="lightgrey")
btn4.place(x=480, y=10)

'''
window configs -----------------------
'''

# window configurations
window.geometry("950x500")
window.resizable(0, 0)
window.title("Arsalon's Vehicle Management System")
window.attributes("-topmost", True)
window.mainloop()
