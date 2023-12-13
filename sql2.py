import sqlite3
import time
from datetime import datetime

conn = sqlite3.connect('testi.db')

print("Database opened")

# conn.execute("""
#         DROP TABLE IF EXISTS Booking;  
#  """)

# conn.execute("""
#        DROP TABLE IF EXISTS User;  
# """)


# Create tables
def createTable():
    conn = sqlite3.connect('testi.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Booking
        (   event_id    INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
            start_time  DATETIME NOT NULL,
            end_time    DATETIME NOT NULL,
            username    TEXT     NOT NULL);
        ''')

    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS User
        (user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        username  TEXT NOT NULL,
        userpass  TEXT NOT NULL,
        lastname TEXT NOT NULL,
        firstname TEXT NOT NULL);
    ''')
   
    
    print("Tables created successfully")

    conn.commit()
    conn.close()


# conn = sqlite3.connect('test2.db')
# print("Created database successfully");

#createTable()


# Insert raservation data
def insertData(parameters):
    
    conn = sqlite3.connect('testi.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Booking (start_time, end_time, username) \
                    VALUES (?, ?, ?)", parameters);
    
    print("Record inserted successfully");     
    
    conn.commit()
    conn.close()


# Insert user data
def insertUser(parameters):
    conn = sqlite3.connect('testi.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO User (username, userpass, lastname, firstname) \
                   VALUES (?,?,?,?)", parameters);

    print("Record inserted successfully");

    conn.commit()
    conn.close()


#parameters = ("test", "test2")
#insertData(parameters)


# Print table (testing)
def printTable():

    conn = sqlite3.connect("testi.db")

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Booking")
    rows = cursor.fetchall()

    for row in rows: 
        print("ID = ", row[0])
        print("Start_time = ", row[1])
        print("End_time = ", row[2])
        print("Username = ", row[3])

    conn.commit()
    conn.close()


### Testing ###
createTable()

now = datetime.now()
start_time = now.strftime("%d/%m/%Y %H:%M:%S")
print(start_time)

time.sleep(3)
now = datetime.now()
end_time = now.strftime("%d/%m/%Y %H:%M:%S")

username = "Messi"

parameters = (start_time, end_time, username)

insertData(parameters)

printTable()


