from tkinter import ttk
import tkinter as tk
from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        root = tk.Tk()
        self.geometry("600x400")
        self.title("Reservations")
        style = ttk.Style()
        style.theme_use('classic')

        self.menubar = Menu()
        self.filemenu = Menu(self.menubar)
        self.filemenu.add_command(label = "Exit", command = lambda : exit())

        self.menubar.add_cascade(label = "File", menu = self.filemenu)

        self.config(menu = self.menubar)

        self.show_table()

    def view(self):
        conn = sqlite3.connect("testi.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Booking")
        rows = cur.fetchall()
        for row in rows:
            print(row) 
            self.tree.insert("", tk.END, values=row)
        conn.close()


    def clear_all(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def show_table(self):
        #tableFrame = Frame(root)
        #tableFrame.pack(side=TOP)

        self.tree= ttk.Treeview(self, column=("column1", "column2", "column3", "column4"), show='headings')
        self.tree.column("#1", anchor="center", width=80)
        self.tree.heading("#1", text="Event ID")
        self.tree.column("#2", anchor="center", width=170)
        self.tree.heading("#2", text="Start time")
        self.tree.column("#3", anchor="center", width=170)
        self.tree.heading("#3", text="End time")
        self.tree.column("#4", anchor="center", width=170)
        self.tree.heading("#4", text="Username")

        self.tree.pack(side=TOP, pady=20)

        b1 = tk.Button(self, text="View data", command=self.view)
        b1.pack(side='left', anchor='e', expand='True', pady=10, padx=10)

        b2 = tk.Button(self, text="Clear", command=self.clear_all)
        b2.pack(side='right', anchor='w', expand='True')


        def exit(): 
            result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?')
            if result == 'yes':
                self.destroy()
                #exit()
    

# root = tk.Tk()
# root.geometry("600x400")
# root.title("Reservations")

# menubar = Menu()
# filemenu = Menu(menubar)
# filemenu.add_command(label = "Exit", command = exit)

# menubar.add_cascade(label = "File", menu = filemenu)

#root.config(menu = menubar)


# tree= ttk.Treeview(root, column=("column1", "column2", "column3", "column4"), show='headings')
# tree.column("#1", anchor="center", width=80)
# tree.heading("#1", text="Event ID")
# tree.column("#2", anchor="center", width=170)
# tree.heading("#2", text="Start time")
# tree.column("#3", anchor="center", width=170)
# tree.heading("#3", text="End time")
# tree.column("#4", anchor="center", width=170)
# tree.heading("#4", text="Username")

# tree.pack(side=TOP, pady=20)

# b1 = tk.Button(root, text="View data", command=view)
# b1.pack(side='left', anchor='e', expand='True', pady=10, padx=10)

# b2 = tk.Button(root, text="Clear", command=clear_all)
# b2.pack(side='right', anchor='w', expand='True') 

if __name__ == "__main__":
    app = App()
    app.mainloop()

