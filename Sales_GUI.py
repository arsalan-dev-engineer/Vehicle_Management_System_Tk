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
