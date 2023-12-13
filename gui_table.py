from tkinter import ttk
import tkinter as tk
from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3


def view():
    conn = sqlite3.connect("testi.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Booking")
    rows = cur.fetchall()
    for row in rows:
        print(row) 
        tree.insert("", tk.END, values=row)
    conn.close()


def clear_all():
    for item in tree.get_children():
        tree.delete(item)


def exit(): 
    result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?')
    if result == 'yes':
        root.destroy()
        #exit()
    

root = tk.Tk()
root.geometry("600x400")
root.title("Reservations")

menubar = Menu()
filemenu = Menu(menubar)
filemenu.add_command(label = "Exit", command = exit)

menubar.add_cascade(label = "File", menu = filemenu)

root.config(menu = menubar)


tree= ttk.Treeview(root, column=("column1", "column2", "column3", "column4"), show='headings')
tree.column("#1", anchor="center", width=80)
tree.heading("#1", text="Event_ID")
tree.column("#2", anchor="center", width=170)
tree.heading("#2", text="Start_time")
tree.column("#3", anchor="center", width=170)
tree.heading("#3", text="End_time")
tree.column("#4", anchor="center", width=170)
tree.heading("#4", text="Username")

tree.pack()

b1 = tk.Button(root, text="View data", command=view)
b1.pack(side='left', anchor='e', expand='True', pady=10, padx=10)

b2 = tk.Button(root, text="Clear", command=clear_all)
b2.pack(side='right', anchor='w', expand='True') 


root.mainloop()

