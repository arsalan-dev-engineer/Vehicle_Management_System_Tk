from tkinter import Tk
from tkinter import *

# Tkinter GUI Window
window = Tk()
header = Label(window, text="Vehicle Sales Management System")
header.place(x=15, y=28)

# Left Frame
LeftF = Frame(window, width=620, height=350, highlightbackground="lightgrey", highlightthickness=0.5, bd=2)
LeftF.place(x=15, y=50)

# Right Frame
RightF = Frame(window, width=285, heigh=435, highlightbackground="lightgrey", highlightthickness=0.5, bd=2, bg="white")
RightF.place(x=650, y= 50)

# Bottom Frame
BottomF = Frame(window, width=620, heigh=70, highlightbackground="lightgrey", highlightthickness=0.5, bd=2)
BottomF.place(x=15, y=415)

# window configurations
window.geometry("950x500")
window.resizable(0, 0)
window.title("Arsalon's Vehicle Management System")
window.attributes("-topmost", True)
window.mainloop()
