'''This is a Password Manager application made using Python's Tkinter and MySQL as a Database
It has three files written in Python
1) Front Page.py(This program which is the main interface)
2) NewRegistration.py(The program for registration interface)
3) ViewRegistration.py(The program interface for viewing the data)
'''

from tkinter import*
from tkinter import messagebox
from PIL import ImageTk, Image
import NewRegistration as new_r
import ViewRegistration as view_r

#Main Window
window1 = Tk()
window1.title('Welcome')
window1.geometry('850x682+0+0')
window1.config()

#Importing Images
image1 = ImageTk.PhotoImage(Image.open("background.png"))
imagenew_reg = ImageTk.PhotoImage(Image.open("new.png"))
imageview_reg = ImageTk.PhotoImage(Image.open("view.png"))
titleimage = ImageTk.PhotoImage(Image.open("heading.png"))
iconimage = ImageTk.PhotoImage(Image.open("icon.png"))
cancelimage = ImageTk.PhotoImage(Image.open("cancel.png"))

#Labels
image1_label = Label(window1, image=image1)
image1_label.place(x=0, y=0)
welcome_label = Label(window1, image=titleimage)
welcome_label.place(x=300, y=20)

#Label Frame
labelframe=LabelFrame(window1, bg='white', width=350, height=500, borderwidth=2, relief="solid")
labelframe.pack(padx=100, pady=100)

#Buttons
register = Button(labelframe, text='New Registration',bd=0,image=imagenew_reg,command=new_r.Newregist)
#command=new_r.Newregist, command=view_r.Viewregist, command=window1.destroy
register.place(x=65,y=200)
view = Button(labelframe, text='View Registration',bd=0,image=imageview_reg,command=view_r.Viewregist)
view.place(x=65, y=270)
close = Button(labelframe, image=cancelimage,bd=0,command=window1.destroy)
close.place(x=120, y=340)

window1.mainloop()
