from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tkMessageBox
import sqlite3




root = tk.Tk()
root.title("Login")
root.geometry("600x400")

global tree

def database():
    global conn, cursor 
    conn = sqlite3.connect("testi.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `User`(user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT NOT NULL, userpass TEXT NOT NULL)")


USERNAME = StringVar()
PASSWORD = StringVar()
LASTNAME = StringVar()
FIRSTNAME = StringVar()

# Login form
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


def show_table():
    global show_table
    LoginFrame.destroy()
    tableFrame = Frame(root)
    tableFrame.pack(side=TOP)
    #label = Label(tableFrame, text="table")
    #label.grid(row=1)
    tree= ttk.Treeview(tableFrame, column=("column1", "column2", "column3", "column4"), show='headings')
    tree.column("#1", anchor="center", width=80)
    tree.heading("#1", text="Event_ID")
    tree.column("#2", anchor="center", width=170)
    tree.heading("#2", text="Start_time")
    tree.column("#3", anchor="center", width=170)
    tree.heading("#3", text="End_time")
    tree.column("#4", anchor="center", width=170)
    tree.heading("#4", text="Username")

    tree.pack()

    b1 = tk.Button(tableFrame, text="View data", command=view())
    b1.pack(side='left', anchor='e', expand='True', pady=10, padx=10)

    b2 = tk.Button(tableFrame, text="Clear", command=clear_all)
    b2.pack(side='right', anchor='w', expand='True')


# Show data from Booking table
def view():
    
    conn = sqlite3.connect("testi.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Booking")
    rows = cur.fetchall()
    for row in rows:
        print(row) 
        tree.insert("", tk.END, values=row)
    conn.close()


# Clear data from the table view
def clear_all():
    for item in tree.get_children():
        tree.delete(item)


def changetoRegister(event=None):
    LoginFrame.destroy()
    #RegisterForm()


def changetoLogin(event=None):
    #RegisterFrame.destroy()
    LoginForm()


def exit():
    answer = tkMessageBox.askquestion('System', 'Are you sure you want to exit?')
    if answer == 'yes':
        root.destroy()


def login():
    database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lb_result1.config(text="Please complete the required field!", fg="orange")
    else:
        cursor.execute("SELECT * FROM User where username = ? and userpass = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            lb_result1.config(text="You Successfully Login", fg="green")
            show_table()
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
