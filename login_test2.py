from tkinter import *
import tkinter as tk
import tkinter.messagebox as tkMessageBox
import sqlite3




root = tk.Tk()
root.title("Login")
root.geometry("600x400")

def database():
    global conn, cursor 
    conn = sqlite3.connect("test2.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `User`(user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, user_name TEXT NOT NULL, user_pass TEXT NOT NULL)")


USERNAME = StringVar()
PASSWORD = StringVar()
LASTNAME = StringVar()
FIRSTNAME = StringVar()


def LoginForm():
    global LoginFrame, lb_result1
    root.title("Login")
    LoginFrame = Frame(root)
    LoginFrame.pack(side=TOP, pady=80)
    lb_username = Label(LoginFrame, text="Username: ")
    lb_username.grid(row=1)
    lb_password = Label(LoginFrame, text="Password: ")
    lb_password.grid(row=2)
    lb_result1 = Label(LoginFrame, text="")
    lb_result1.grid(row=3, columnspan=2)
    username = Entry(LoginFrame, textvariable=USERNAME)
    username.grid(row=1, column=1)
    password = Entry(LoginFrame, textvariable=PASSWORD, show="*")
    password.grid(row=2, column=1)

    #btn_login = Button(LoginFrame, text="Login", command= lambda : [login(), CalendarForm()] )
    btn_login = Button(LoginFrame, text="Login", command= login)
    btn_login.grid(row=4, columnspan=2, pady=20)
    lb_register = Label(LoginFrame, text="Register", fg="Blue")
    lb_register.grid(row=4, column=3)
    lb_register.bind('<Button-1>', changetoRegister)

def RegisterForm():
    global RegisterFrame, lb_result2
    root.title("Register")
    RegisterFrame = Frame(root)
    RegisterFrame.pack(side=TOP, pady=40)
    lb_username = Label(RegisterFrame, text="Username: ")
    lb_username.grid(row=1)
    lb_password = Label(RegisterFrame, text="Password: ")
    lb_password.grid(row=2)
    lb_lastname = Label(RegisterFrame, text="Lastname: " )
    lb_lastname.grid(row=3)
    lb_firstname = Label(RegisterFrame, text="Fisrtsname: ")
    lb_firstname.grid(row=4)
    lb_result2 = Label(RegisterFrame, text="")
    lb_result2.grid(row=5, columnspan=2)
    username = Entry(RegisterFrame, textvariable=USERNAME)
    username.grid(row=1, column=1)
    password = Entry(RegisterFrame, textvariable=PASSWORD, show="*")
    password.grid(row=2, column=1)
    lastname = Entry(RegisterFrame, textvariable=LASTNAME)
    lastname.grid(row=3, column=1)
    firstname = Entry(RegisterFrame, textvariable=FIRSTNAME)
    firstname.grid(row=4, column=1)
    btn_register = Button(RegisterFrame, text="Register", command=register)
    btn_register.grid(row=6, columnspan=2, pady=20)
    lb_login = Label(RegisterFrame, text="Login", fg="Blue")
    lb_login.grid(row=6, column=4)
    lb_login.bind('<Button-1>', changetoLogin)


def CalendarForm():
    LoginFrame.destroy()
    CalendarFrame = Frame(root)
    CalendarFrame.pack(side=TOP, pady=80)
    lb_calendar = Label(CalendarFrame, text="Calendar")
    lb_calendar.grid(row=1)

def changetoRegister(event=None):
    LoginFrame.destroy()
    RegisterForm()

def changetoLogin(event=None):
    RegisterFrame.destroy()
    LoginForm()

def exit():
    answer = tkMessageBox.askquestion('System', 'Are you sure you want to exit?')
    if answer == 'yes':
        root.destroy()

def register():
    database()
    if USERNAME.get() == "" or PASSWORD.get() == "" or LASTNAME.get() == "" or FIRSTNAME.get():
        lb_result2.config(text="Please complete the required field!", fg="orange")
    if cursor.fetchone() is not None:
            lb_result2.config(text="Username is already taken", fg="red")
    else:
        cursor.execute("INSERT INTO `user` (username, userpass, lastname, firstname) VALUES(?, ?, ?, ?)", (str(USERNAME.get()), str(PASSWORD.get()), str(LASTNAME.get()), str(FIRSTNAME.get())))
        conn.commit()
        USERNAME.set("")
        PASSWORD.set("")
        LASTNAME.set("")
        FIRSTNAME.set("")
        lb_result2.config(text="Successfully Created!", fg="black")
    cursor.close()
    conn.close()



def login():
    database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lb_result1.config(text="Please complete the required field!", fg="orange")
    else:
        cursor.execute("SELECT * FROM User where username = ? and userpass = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            lb_result1.config(text="You Successfully Login", fg="green")
            CalendarForm()
        else:
            lb_result1.config(text="Wrong Username or password", fg="red")



LoginForm()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="Exit", command=exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)





if __name__ == '__main__':
    root.mainloop()
