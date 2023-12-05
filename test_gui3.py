from tkinter import ttk
import tkinter as tk
from tkinter import *
import sqlite3

def View():
    conn = sqlite3.connect("test2.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Stime")
    rows = cur.fetchall()
    for row in rows:
        print(row) 
        tree.insert("", tk.END, values=row)
    conn.close()

def clear_all():
    for item in tree.get_children():
        tree.delete(item)
    

root = tk.Tk()
root.geometry("600x400")

menubar = Menu()
filemenu = Menu(menubar)
filemenu.add_command(label = "Exit", command = root.quit)

menubar.add_cascade(label = "File", menu = filemenu)

root.config(menu = menubar)


tree= ttk.Treeview(root, column=("column1", "column2", "column3"), show='headings')
tree.column("#1", anchor="center", width=80)
tree.heading("#1", text="ID")
tree.column("#2", anchor="center", width=170)
tree.heading("#2", text="go_in")
tree.column("#3", anchor="center", width=170)
tree.heading("#3", text="go_out")
tree.pack()

b2 = tk.Button(text="View data", command=View)
b2.pack()

ttk.Button(root, text="Clear", command=clear_all).pack(pady=10) 

root.mainloop()