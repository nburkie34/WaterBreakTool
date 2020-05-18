import Tkinter
from Tkinter import *
import tkMessageBox
from PIL import ImageTk, Image
import math

win = Tkinter.Tk()
win.title("Water Main Break Tool")
win.geometry("300x300")

def hole():
    win3 = Tkinter.Toplevel()
    win3.title('Hole in Pipe Leak Calculator')
    win3.geometry("550x220")

    def calc():
        dia = float(e1.get())
        press = float(e3.get())
        time = float(e4.get())
        gpm = (dia/2)/12*(dia/2)/12*3.1416*math.sqrt(press*2.309*64.4)*0.7*7.48*60
        gpm2 = round(gpm*100)/100
        total = time*gpm2*60
        tkMessageBox.showinfo("Results", ("GPM Flow lost from leak: " + str(gpm2) + "\n Total Water Lost (Gallons): " + str(total)))

    path = "hole.jpg"
    img = ImageTk.PhotoImage(Image.open(path))
    L1 = Label(win3, anchor = W, text='Input Hole Diameter (Inches)').grid(row=0)
    L3 = Label(win3, anchor = W, text='Input Pipe Pressure (PSI)').grid(row=1)
    L4 = Label(win3, anchor = W, text='Input Leak Time (Hours)').grid(row=2)
    L5 = Label(master = win3, anchor = W, image=img)
    L5.image = img
    L5.grid(row=5)
    e1 = Entry(win3) 
    e3 = Entry(win3) 
    e4 = Entry(win3)
    e1.grid(row=0, column=1) 
    e3.grid(row=1, column=1) 
    e4.grid(row=2, column=1)

    B = Button(win3, text='Calculate', command = calc).grid(row=5, column=1)
    win3.mainloop()
    
def circ():
    win1 = Tkinter.Toplevel()
    win1.title('Circular Break Leak Calculator')
    win1.geometry("650x300")

    def calc():
        dia = float(e1.get())
        wid = float(e2.get())
        press = float(e3.get())
        time = float(e4.get())
        gpm = (dia/12)*(wid/12)*3.1416*math.sqrt(press*2.309*64.4)*0.7*7.48*60
        gpm2 = round(gpm*100)/100
        total = time*gpm2*60
        tkMessageBox.showinfo("Results", ("GPM Flow lost from leak: " + str(gpm2) + "\n Total Water Lost (Gallons): " + str(total)))

    path = "circ.jpg"
    img = ImageTk.PhotoImage(Image.open(path))
    L1 = Label(win1, text='Input Pipe Diameter (Inches)').grid(row=0)
    L2 = Label(win1, text='Input Break Width (Inches)').grid(row=1)
    L3 = Label(win1, text='Input Pipe Pressure (PSI)').grid(row=2)
    L4 = Label(win1, text='Input Leak Time (Hours)').grid(row=3)
    L5 = Label(master = win1, anchor = W, image=img)
    L5.image = img
    L5.grid(row=5)
    e1 = Entry(win1) 
    e2 = Entry(win1)
    e3 = Entry(win1) 
    e4 = Entry(win1)
    e1.grid(row=0, column=1) 
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1) 
    e4.grid(row=3, column=1)

    B = Button(win1, text='Calculate', command = calc).grid(row=5, column=1)

    win1.mainloop()

def rect():
    win2 = Tkinter.Toplevel()
    win2.title('Rectangular Break Leak Calculator')
    win2.geometry("520x200")

    def calc():
        len = float(e1.get())
        wid = float(e2.get())
        press = float(e3.get())
        time = float(e4.get())
        gpm = (len/12)*(wid/12)*math.sqrt(press*2.309*64.2)*0.7*7.48*60
        gpm2 = round(gpm*100)/100
        total = time*gpm2*60
        tkMessageBox.showinfo("Results", ("GPM Flow lost from leak: " + str(gpm2) + "\n Total Water Lost (Gallons): " + str(total)))

    path = "rect.jpg"
    img = ImageTk.PhotoImage(Image.open(path))
    L1 = Label(win2, text='Input Break Length (Inches)').grid(row=0)
    L2 = Label(win2, text='Input Break Width (Inches)').grid(row=1)
    L3 = Label(win2, text='Input Pipe Pressure (PSI)').grid(row=2)
    L4 = Label(win2, text='Input Leak Time (Hours)').grid(row=3)
    L5 = Label(master = win2, anchor = W, image=img)
    L5.image = img
    L5.grid(row=5)
    e1 = Entry(win2) 
    e2 = Entry(win2)
    e3 = Entry(win2) 
    e4 = Entry(win2)
    e1.grid(row=0, column=1) 
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1) 
    e4.grid(row=3, column=1)

    B = Button(win2, text='Calculate', command = calc).grid(row=5, column=1)

    win2.mainloop()
def ope():
    if Lb.curselection() == (0,):
        circ()
    if Lb.curselection() == (1,):
        hole()
    if Lb.curselection() == (2,):
        rect()
    print Lb.curselection()
L1 = Label(win, text="Select a Type of Break")        
Lb = Listbox(win)
Lb.insert(0, "Circular Break")
Lb.insert(1, "Hole in Pipe")
Lb.insert(2, "Rectangular Break")




btn = Button(win, text = "Open", command = ope)
L1.pack()
Lb.pack()
btn.pack()
win.mainloop()
