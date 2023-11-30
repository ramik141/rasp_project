import sqlite3
from tkinter import ttk
conn = sqlite3.connect('test2.db')

import datetime
from time import time

import tkinter as tk
from tkinter import *

class Gui:
    def __init__(self, master):
        self.master = master
        #super().__init__()

        master.title("Movement tracker")
        master.geometry("600x250")

        self.menubar = Menu(window)

        self.filemenu = Menu(self.menubar)
        self.filemenu.add_command(label = "Exit", command = lambda : master.destroy())

        self.menubar.add_cascade(label = "File", menu = self.filemenu)

        master.config(menu = self.menubar)

        

        Gui.fetchData(self,window)

        button = ttk.Button(master= self.master, text="Reload", command= Gui.fetchData(self, window))
        button.grid(row = 11, column = 0)


    def fetchData(self,window):
        moving_data = ""
        moving_data = conn.execute("""SELECT * from Stime""")
        print("test")
        i = 0

        #colums widths, first is smaller
        col_widths = [8] + [25] + [25] + [8]

        for test in moving_data:
            for j in range(len(test)):
                e = Entry(window, width=col_widths[j], fg='blue')
                e.grid(row=i, column=j)
                e.insert(END, test[j])

            i = i +1
    
        
        
        fetch_time = datetime.datetime.now()
        print (fetch_time)
        text_label = ttk.Label(master=self.master, text="Fetch time:")
        time_label = ttk.Label(master=self.master, text=fetch_time)
        

        text_label.grid(row = 10, column = 0)
        time_label.grid(row = 10, column = 1)
        




if __name__ == '__main__':
    
    window = Tk()
    app = Gui(window)
    window.mainloop()