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


def LoginForm():
    global LoginFrame, lb_result1
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
    password = Entry(LoginFrame, textvariable=PASSWORD)
    password.grid(row=2, column=1)

    btn_login = Button(LoginFrame, text="Login", command = login)
    btn_login.grid(row=4, columnspan=2, pady=20)

def exit():
    answer = tkMessageBox.askquestion('System', 'Are you sure you want to exit?')
    if answer == 'yes':
        root.destroy()

def login():
    database()
    cursor.execute("SELECT * FROM User where user_name = ? and user_pass = ?", (USERNAME.get(), PASSWORD.get()))
    if cursor.fetchone() is not None:
        lb_result1.config(text="You Successfully Login", fg="green")
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
