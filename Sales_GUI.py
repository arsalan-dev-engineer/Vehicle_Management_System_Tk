from tkinter import Tk
from tkinter import *
from tkinter import messagebox

# Tkinter GUI Window
window = Tk()
header = Label(window, text="Vehicle Sales Management System")
header.place(x=15, y=22)

'''
Left Frame Details -----------------------
'''

# Left Frame
leftF = Frame(window, width=620, height=350, highlightbackground="lightgrey", highlightthickness=0.5)
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
RightF = Frame(window, width=285, heigh=435, highlightbackground="lightgrey", highlightthickness=0.5)
RightF.place(x=650, y= 50)

'''
Bottom Frame Buttons -----------------------
'''

# Bottom Frame
BottomF = Frame(window, width=620, heigh=70, highlightbackground="lightgrey", highlightthickness=0.5, bd=2)
BottomF.place(x=15, y=415)

btn1 = Button(BottomF, width=18, height=2, text="Button 1", bg="lightgrey")
btn1.place(x=0, y=10)

btn2 = Button(BottomF, width=18, height=2, text="Button 2", bg="lightgrey")
btn2.place(x=160, y=10)

btn3 = Button(BottomF, width=18, height=2, text="Button 3", bg="lightgrey")
btn3.place(x=320, y=10)

btn4 = Button(BottomF, width=18, height=2, text="Button 4", bg="lightgrey")
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
