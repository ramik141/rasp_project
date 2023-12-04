import sqlite3
from tkinter import ttk
from tkinter import *

from datetime import datetime
from time import time

conn = sqlite3.connect('test2.db')
cursor = conn.cursor()

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

        # button = ttk.Button(master= self.master, width=7, text="Reload", command=Gui.clear_entry())
        # button.grid(row = 11, column = 0)
    
    # def clear_entry(e):
        
    #     e.delete(0, "end")


    def fetchData(self,window):
        
        moving_data = cursor.execute("""SELECT * from Stime""")
        #moving_data.clear()
        lb = Label(window, width=8,text='ID',borderwidth=0,relief='ridge', anchor='center')
        lb.grid(row=0, column=0, pady=(10,0))
        lb = Label(window, width=20,text='Go_in',borderwidth=0,relief='ridge', anchor='center')
        lb.grid(row=0, column=1, pady=(10,0))
        lb = Label(window, width=20,text='Go_out',borderwidth=0,relief='ridge', anchor='center')
        lb.grid(row=0, column=2, pady=(10,0))
        lb = Label(window, width=8,text='User_id',borderwidth=0,relief='ridge', anchor='center')
        lb.grid(row=0, column=3, pady=(10,0))

        i = 1
        j = 1

        #colums widths, first and last are smaller
        col_widths = [8] + [20] + [20] + [8]

        for row in moving_data:
            for j in range(len(row)):
                e = Entry(window, width=col_widths[j], fg='blue', justify=CENTER)
                e.grid(row=i, column=j)
                e.insert(END, row[j])

            i = i +1
            
        now = datetime.now()
        fetch_time = now.strftime("%d/%m/%Y %H:%M:%S")
        text_label = ttk.Label(master=self.master, text="Fetch time")
        time_label = ttk.Label(master=self.master, text=fetch_time)
        
        text_label.grid(row=10, column=0, pady=(5,5))
        time_label.grid(row=10, column=1, pady=(5,5))

        # button = ttk.Button(master= self.master, width=7, text="Reload", command=Gui.clear_entry(e))
        # button.grid(row = 11, column = 0)

                

# Main
if __name__ == '__main__':
    
    window = Tk()
    app = Gui(window)
    window.mainloop()