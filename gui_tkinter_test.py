from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tkMessageBox
import sqlite3


def database():
    global conn, cursor 
    conn = sqlite3.connect("testi.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `User`(user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT NOT NULL, userpass TEXT NOT NULL)")


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.geometry("700x450")
        self.title("View data")
        self.change_frame(LoginPage)
                        

        self.menubar = Menu()
        self.filemenu = Menu(self.menubar)
        self.filemenu.add_command(label = "Exit", command = self.exit)

        self.menubar.add_cascade(label = "File", menu = self.filemenu)

        self.config(menu = self.menubar)
    

    def change_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def exit(self): 
        result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?')
        if result == 'yes':
            app.destroy()
            #exit()


class LoginPage(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.username = StringVar()
        self.password = StringVar()
        #self.lastname = StringVar()
        #elf.firstname = StringVar()

        self.lb_username = Label(self, text="Username: ")
        self.lb_username.grid(row=4, pady=40)
        self.lb_password = Label(self, text="Password: ")
        self.lb_password.grid(row=5)
        self.lb_result1 = Label(self, text="")
        self.lb_result1.grid(row=6, columnspan=2)
        self.username = Entry(self, textvariable=self.username)
        self.username.grid(row=4, column=1)
        self.password = Entry(self, textvariable=self.password, show="*")
        self.password.grid(row=5, column=1)

        btn_login = Button(self, text="Login", command= self.login)
        btn_login.grid(row=7, columnspan=2, pady=20)
        

    def login(self):
        database()
        if self.username.get() == "" or self.password.get() == "":
            self.lb_result1.config(text="Please complete the required field!", fg="orange")
        else:
            cursor.execute("SELECT * FROM User where username = ? and userpass = ?", (self.username.get(), self.password.get()))
            if cursor.fetchone() is not None:
                self.lb_result1.config(text="You Successfully Login", fg="green")
                #command= lambda : master.change_frame(TablePage)
                app.change_frame(TablePage)
            else:
                self.lb_result1.config(text="Wrong Username or password", fg="red")


class TablePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.showTable()

        
    #Clear data from the table view
    def clear_all(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
    
    def view(self):
        #self.clear_all()
        conn = sqlite3.connect("testi.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Booking")
        rows = cur.fetchall()
        for row in rows:
            print(row) 
            self.tree.insert("", tk.END, values=row)
        conn.close()
   

    def showTable(self):
        #self.title("View data")
        # tree_frame = Frame(self)
        # tree_frame.pack(pady=20)

        # tree_scroll = Scrollbar(tree_frame)
        # tree_scroll.pack(side="right", fill="y")


        #self.tree= ttk.Treeview(self, columns=("column1", "column2", "column3", "column4"), show='headings', yscroll=tree_scroll.set)
        self.tree= ttk.Treeview(self, columns=("column1", "column2", "column3", "column4"), show='headings')
        self.scrollbar = ttk.Scrollbar(self, orient="vertical")
        self.tree.column("#1", anchor="center", width=80)
        self.tree.heading("#1", text="Event ID")
        self.tree.column("#2", anchor="center", width=170)
        self.tree.heading("#2", text="Start time")
        self.tree.column("#3", anchor="center", width=170)
        self.tree.heading("#3", text="End time")
        self.tree.column("#4", anchor="center", width=170)
        self.tree.heading("#4", text="Username")
        self.tree.configure(yscroll=self.scrollbar.set, selectmode="browse")
        self.scrollbar.config(command=self.tree.yview)
        self.scrollbar.pack(side="right")
        
        self.tree.pack(side=TOP, pady=20)
        
        view_btn = tk.Button(self, text="View data", command= self.view)
        view_btn.pack(side='left', anchor='e', expand='True', padx=10)
        print("test")

        clear_btn = tk.Button(self, text="Clear", command= self.clear_all)
        clear_btn.pack(side='left', anchor='w', expand='True')

        sign_out = tk.Button(self, text="Sign out", fg='blue', command = lambda : app.change_frame(LoginPage))
        sign_out.pack(side='left', anchor='w')
        #sign_out.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)

        


if __name__ == "__main__":
    app = App()
    app.mainloop()