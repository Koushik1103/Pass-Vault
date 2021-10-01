from tkinter import*
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk
import mysql.connector as sql
mydb = sql.connect(host='localhost', user='root', passwd='123456789', database='project')
cur = mydb.cursor()

def Viewregist():
    view_r = Toplevel()
    view_r.title('Registration Page')
    view_r.geometry('850x682+0+0')
    image1 = ImageTk.PhotoImage(Image.open("background.png"))
    image1_label = Label(view_r, image=image1)
    image1_label.place(x=0, y=0)

    #Label Frame
    labelframe=LabelFrame(view_r,bg='white',width=500,height=550,borderwidth=2, relief="solid")
    labelframe.place(x=200,y=100)

    #images
    titleimage = ImageTk.PhotoImage(Image.open("heading.png"))
    back_button = ImageTk.PhotoImage(Image.open("back.png"))
    submit_button=ImageTk.PhotoImage(Image.open("submit.png"))
    welcome_label = Label(view_r, image=titleimage)
    welcome_label.place(x=320, y=10)

    #Labels
    new_name = Label(labelframe, text="First Name", bd=5, bg="white", font=("ariel",18))
    new_name.place(x=0, y=170)

    new_last = Label(labelframe, text="Last Name", bd=5, bg="white", font=("ariel",18))
    new_last.place(x=0, y=220)

    new_app = Label(labelframe, text="App Name", bd=5, bg="white", font=("ariel",18))
    new_app.place(x=0, y=270)
    
    #Entry
    name_e = ttk.Entry(labelframe, width=20, font=('calibre', 15, 'normal'))
    name_e.place(x=230, y=170)

    last_e = ttk.Entry(labelframe, width=20, font=('calibre', 15, 'normal'))
    last_e.place(x=230, y=220)

    app_e = ttk.Entry(labelframe, width=20, font=('calibre', 15, 'normal'))
    app_e.place(x=230, y=270)
    
    def submit():
        view = Toplevel()
        view.title('Registration Page')
        view.geometry('850x682+0+0')
        view.config(bg='sky blue')
        image1 = ImageTk.PhotoImage(Image.open("background.png"))
        image1_label = Label(view,image=image1)     
        image1_label.place(x=0, y=0)

        #Image Label
        labelframe=LabelFrame(view,bg='white',width=500,height=550,borderwidth=2, relief="solid")
        labelframe.place(x=270,y=100)

        #Images
        titleimage = ImageTk.PhotoImage(Image.open("heading.png"))
        back_button=ImageTk.PhotoImage(Image.open("back.png"))
        welcome_label = Label(view, image=titleimage)
        welcome_label.place(x=320, y=10)

        #Labels
        new_name = Label(labelframe, text="First Name", bd=2, bg='white', font=('ariel', 18))
        new_name.place(x=0, y=170)

        new_last = Label(labelframe, text="Last Name", bd=2, bg='white', font=('ariel', 18))
        new_last.place(x=0, y=220)

        new_app = Label(labelframe, text="App Name", bd=2, bg='white', font=('ariel',18))
        new_app.place(x=0, y=270)

        new_url = Label(labelframe, text="URL", bd=2, bg='white', font=('ariel',18))
        new_url.place(x=0, y=320)
    
        new_username = Label(labelframe, text="Username", bd=2, bg='white', font=('ariel', 18))
        new_username.place(x=0, y=370)

        new_pass = Label(labelframe, text="Password", bd=2, bg='white', font=('ariel', 18))
        new_pass.place(x=0, y=420)

        iname = name_e.get()
        ilast = last_e.get()
        iapp = app_e.get()
        
        mydb = sql.connect(host="localhost", user="root", passwd="123456789", database='project')
        cur = mydb.cursor()

        #cur.execute('create database if not exists project')
        #cur.execute('create table if not exists passvault(name varchar(250), last varchar(250), app varchar(250), url varchar(250), username varchar(250), password varchar(250)')

        cur.execute("select name from passvault where name=%s and last=%s and app=%s", (iname, ilast, iapp))
        dname = cur.fetchone()

        cur.execute("select last from project.passvault where name=%s and last=%s and app=%s", (iname, ilast, iapp))
        dlast = cur.fetchone()

        cur.execute("select app from project.passvault where name=%s and last=%s and app=%s", (iname, ilast, iapp))
        dapp = cur.fetchone()

        cur.execute("select url from project.passvault where name=%s and last=%s and app=%s", (iname, ilast, iapp))
        durl = cur.fetchone()

        cur.execute("select username from project.passvault where name=%s and last=%s and app=%s", (iname, ilast, iapp))
        dusername = cur.fetchone()

        cur.execute("select password from project.passvault where name=%s and last=%s and app=%s", (iname, ilast, iapp))
        dpassword = cur.fetchone()

        #Labels
        name = Label(labelframe, text=dname, bd=5, bg='white', font=('ariel', 15))
        name.place(x=230, y=170)

        last = Label(labelframe, text=dlast, bd=5, bg='white', font=('ariel', 15))
        last.place(x=230, y=220)

        app = Label(labelframe, text=dapp, bd=5, bg='white', font=('ariel', 15))
        app.place(x=230, y=270)

        url = Label(labelframe, text=durl, bd=5, bg='white', font=('ariel', 15))
        url.place(x=230, y=320)

        username = Label(labelframe, text=dusername, bd=5, bg='white', font=('ariel', 15))
        username.place(x=230, y=370)

        password = Label(labelframe, text=dpassword, bd=5, bg='white', font=('ariel', 15))
        password.place(x=230, y=430)

        Button(labelframe, image=back_button, bd=0, bg='white', command=view_r.destroy).place(x=100, y=470)
        view.mainloop()

    #Buttons
    Button(labelframe, bg='white', image=back_button,bd=0, command=view_r.destroy).place(x=100, y=470)
    Button(labelframe, bg='white', image=submit_button,bd=0,command=submit).place(x=300, y=470)
    view_r.mainloop()
