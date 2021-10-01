from tkinter import*
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector as sql

mydb=sql.connect(host="localhost", user="root", passwd="123456789", database='project')
#cur.execute("create database if not exists project")
cur=mydb.cursor()

def Newregist():
    new_r=Toplevel()
    new_r.title("Registration Page")
    new_r.geometry("850x682+0+0")
    new_r.config()
    image1=ImageTk.PhotoImage(Image.open("background.png"))
    titleimage=ImageTk.PhotoImage(Image.open("heading.png"))
    back_button=ImageTk.PhotoImage(Image.open("back.png"))
    submit_button=ImageTk.PhotoImage(Image.open("submit.png"))
    image1_label=Label(new_r, image=image1)
    #image1_label.image = image1
    image1_label.place(x=0, y=0)
    #new_label = Label(new_r, text='NEW REGISTRATION', fg='white', bg='black', bd=6, relief=RAISED, font=('ariel', 30))
    welcome_label = Label(new_r, image=titleimage)
    welcome_label.place(x=320, y=10)

    labelframe1=LabelFrame(new_r,bg='white',width=500,height=550,borderwidth=2, relief="solid")
    labelframe1.place(x=200,y=100)
    
    #Labels
    new_name = Label(labelframe1, text="First Name", bd=5, bg='white', font=('ariel', 18))
    new_name.place(x=0, y=170)

    new_last = Label(labelframe1, text="Last Name", bd=5, bg='white', font=('ariel', 18))
    new_last.place(x=0, y=220)

    new_app = Label(labelframe1, text="App Name", bd=5, bg='white', font=('ariel',18))
    new_app.place(x=0, y=270)

    new_url = Label(labelframe1, text="URL", bd=5, bg='white', font=('ariel',18))
    new_url.place(x=0, y=320)
    
    new_username = Label(labelframe1, text="Username", bd=5, bg='white', font=('ariel', 18))
    new_username.place(x=0, y=370)

    new_pass = Label(labelframe1, text="Password", bd=5, bg='white', font=('ariel', 18))
    new_pass.place(x=0, y=420)

    #Entry
    name_e = ttk.Entry(labelframe1, width=20, font=('calibre', 15, 'normal'))
    name_e.place(x=230, y=170)

    last_e = ttk.Entry(labelframe1, width=20, font=('calibre', 15, 'normal'))
    last_e.place(x=230, y=220)

    app_e = ttk.Entry(labelframe1, width=20, font=('calibre', 15, 'normal'))
    app_e.place(x=230, y=270)
    
    url_e = ttk.Entry(labelframe1, width=20, font=('calibre', 15, 'normal'))
    url_e.place(x=230, y=320)

    username_e = ttk.Entry(labelframe1, width=20, font=('calibre', 15, 'normal'))
    username_e.place(x=230, y=370)

    pass_e = ttk.Entry(labelframe1, width=20, font=('calibre', 15, 'normal'))
    pass_e.place(x=230, y=420)

    def insert():
        name = name_e.get()
        last = last_e.get()
        app = app_e.get()
        url = url_e.get()
        username = username_e.get()
        password = pass_e.get()

        mydb = sql.connect(host="localhost", user="root", passwd="123456789", database="project")
        cur = mydb.cursor()
        #cur.execute('create database if not exists project')
        cur.execute("create table if not exists passvault(name varchar(255), last varchar(255), app varchar(255), url varchar(255), username varchar(255), password varchar(255))")
        cur.execute("insert into passvault(name, last, app, url, username, password) values(%s, %s, %s, %s, %s, %s)", (name, last, app, url, username, password))
        mydb.commit()
        messagebox.showinfo(title='Registration Complete', message='Password successfully saved')
        new_r.destroy()

    #Buttons
    Button(labelframe1, bg='white', image=back_button, bd=0, command=new_r.destroy).place(x=100, y=470)
    Button(labelframe1, bg='white', image=submit_button, bd=0, command=insert).place(x=300, y=470)

    new_r.mainloop()


    
    
    
    
