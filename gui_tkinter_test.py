from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tkMessageBox
import sqlite3

# Open database
def database():
    global conn, cursor 
    conn = sqlite3.connect("testi.db")
    cursor = conn.cursor()


# Main window
class Gui_app(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.geometry("800x400")
        self.title("View data")
        self.change_frame(LoginPage)
                       

        self.menubar = Menu()
        self.filemenu = Menu(self.menubar)
        self.filemenu.add_command(label = "Exit", command = self.exit)
        self.menubar.add_cascade(label = "File", menu = self.filemenu)

        self.config(menu = self.menubar)
    
    # this function change the frame (LoginPage, RegisterPage, TablePage)
    def change_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    # for ending the program
    def exit(self): 
        result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?')
        if result == 'yes':
            app.destroy()
            #exit()

# LoginPage shows login window
class LoginPage(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.username = StringVar()
        self.password = StringVar()

        # make frame for components
        login_frame = ttk.Frame(self)
        login_frame.pack(pady=60)

        # add components to the login frame 
        self.lb_username = Label(login_frame, text="Username: ")
        self.lb_username.grid(row=0, column=0, padx=0, pady=10) 
        self.lb_password = Label(login_frame, text="Password: ")
        self.lb_password.grid(row=1, column=0, padx=0, pady=10)
        self.lb_resutl1 = Label(login_frame, text="")
        self.lb_resutl1.grid(row=6, columnspan=2)
        self.username = Entry(login_frame, bg="#F4F5FA", textvariable=self.username)
        self.username.grid(row=0, column=1, padx=10, pady=10)
        print(self.username)
        self.password = Entry(login_frame, bg="#F4F5FA", textvariable=self.password, show="*")
        self.password.grid(row=1, column=1, padx=10, pady=10)
        
        btn_login = Button(login_frame, text="Login", width=15, command= self.login)
        btn_login.grid(row=7, column=1)
        lb_register = Label(login_frame, text="Register", fg="Blue")
        lb_register.grid(row=8, column=1, pady=10)
        lb_register.bind('<Button-1>', lambda event: self.master.change_frame(RegisterPage))
     
        
    
    def login(self):
        #open database connection
        database()
        # check is some entry field empty
        if self.username.get() == "" or self.password.get() == "":
            self.lb_resutl1.config(text="Please complete the required field!", fg="orange")
        else:
            cursor.execute("SELECT * FROM User where username = ? and userpass = ?", (self.username.get(), self.password.get())) # search for login information
            if cursor.fetchone() is not None:
                self.lb_resutl1.config(text="You Successfully Login", fg="green")
                # call change_frame function from Gui_app class 
                self.master.change_frame(TablePage) 
            else:
                self.lb_resutl1.config(text="Wrong Username or password", fg="red")


class RegisterPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.username = StringVar()
        self.password = StringVar()
        self.lastname = StringVar()
        self.firstname = StringVar()

        # make frame for components
        reg_frame = ttk.Frame(self)
        reg_frame.pack(pady=60)

        # add components to Register frame
        self.lb_username = Label(reg_frame, text="Username: ")
        self.lb_username.grid(row=0, column=0, padx=0, pady=10)
        self.lb_password = Label(reg_frame, text="Password: ")
        self.lb_password.grid(row=1, column=0, padx=0, pady=10)
        self.lb_lastname = Label(reg_frame, text="Lastname: " )
        self.lb_lastname.grid(row=2, column=0, padx=0, pady=10)
        self.lb_firstname = Label(reg_frame, text="Firstname: ")
        self.lb_firstname.grid(row=3, column=0, padx=0, pady=10)
        self.lb_result2 = Label(reg_frame, text="")
        self.lb_result2.grid(row=4, columnspan=2)
        self.username = Entry(reg_frame, bg="#F4F5FA", textvariable=self.username)
        print(self.username)
        self.username.grid(row=0, column=1, padx=10, pady=10)
        self.password = Entry(reg_frame, bg="#F4F5FA", textvariable=self.password, show="*")
        self.password.grid(row=1, column=1, padx=10, pady=10)
        self.lastname = Entry(reg_frame, bg="#F4F5FA", textvariable=self.lastname)
        self.lastname.grid(row=2, column=1, padx=10, pady=10)
        self.firstname = Entry(reg_frame, bg="#F4F5FA", textvariable=self.firstname)
        self.firstname.grid(row=3, column=1, padx=10, pady=10)
        
        self.btn_register = Button(reg_frame, text="Register", command=self.register)
        self.btn_register.grid(row=5, column=1, pady=10)
        lb_login = Label(reg_frame, text="Login", fg="Blue")
        lb_login.grid(row=6, column=1)
        lb_login.bind('<Button-1>', lambda event: self.master.change_frame(LoginPage)) # calling change_frame function from Gui_app class
     


    def register(self):
        database()
        # check if some entry field is empty
        if self.username.get() == "" or self.password.get() == "" or self.lastname.get() == "" or self.firstname.get() == "":
            self.lb_result2.config(text="Please complete the required field!", fg="orange")
            #time.sleep(3)
        else: 
            cursor.execute("SELECT * FROM User WHERE `username` = ?", (self.username.get(),))
            if cursor.fetchone() is not None:
                self.lb_result2.config(text="Username is already taken", fg="red")
            else:
                # insert data to the user table
                cursor.execute("INSERT INTO User (username, userpass, lastname, firstname) VALUES(?, ?, ?, ?)", (str(self.username.get()), str(self.password.get()), str(self.lastname.get()), str(self.firstname.get())))
                conn.commit()
                self.lb_result2.config(text="Successfully Created!", fg="green")
        cursor.close()
        conn.close()



# Show 
class TablePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.showTable()
        
    #Clear data from the table view
    def clear_all(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
    

    def view(self):
        self.clear_all()
        conn = sqlite3.connect("testi.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Booking")
        rows = cur.fetchall()
        for row in rows:
            print(row) 
            self.tree.insert("", tk.END, values=row)
        conn.close()
   

    def showTable(self):
        
        #frames for layout 
        left_frame = Frame(self, width=200, height=400)
        left_frame.grid(row=0, column=0, padx=5, pady=5)

        right_frame = Frame(self, width=200, height=400)
        right_frame.grid(row=0, column=1, padx=10, pady=40)

        self.tree= ttk.Treeview(right_frame, columns=("column1", "column2", "column3", "column4"), show='headings')
        self.scrollbar = ttk.Scrollbar(right_frame, orient="vertical")
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
        self.scrollbar.pack(side="right", fill="y")
        
        self.tree.pack(side="left", fill="both", expand=True)
        
        view_btn = tk.Button(left_frame, text="View data", width=8, command= self.view)
        view_btn.grid(padx=(0, 0), pady=(20, 0))
       
        clear_btn = tk.Button(left_frame, text="Clear", command= self.clear_all)
        clear_btn.config(width=8)
        clear_btn.grid(padx=(0, 0), pady=(50, 0))
        #clear_btn.pack(side='left', anchor='50', expand='True')

        sign_out = tk.Button(left_frame, text="Sign out", fg='blue', command = lambda : self.master.change_frame(LoginPage))
        sign_out.config(width=8)
        sign_out.grid(padx=(0, 0), pady=(50, 0))
        
        #sign_out.pack(side='left', anchor='w')
        #sign_out.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)

        


if __name__ == "__main__":
    app = Gui_app()
    app.mainloop()