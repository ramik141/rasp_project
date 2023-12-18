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
    

    create_booking_table = """
    CREATE TABLE IF NOT EXISTS Booking (
        event_id    INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
        go_in       DATETIME NOT NULL,
        go_out      DATETIME NOT NULL,
        username    TEXT     NOT NULL
        );
    """
    cursor.execute(create_booking_table)
    
    
    create_user_table = """
    CREATE TABLE IF NOT EXISTS User (
        user_id     INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        username    TEXT NOT NULL,
        userpass    TEXT NOT NULL,
        lastname    TEXT NOT NULL,
        firstname   TEXT NOT NULL
        );
    """
    cursor.execute(create_user_table)


    print("Tables created successfully")

    conn.commit()
    conn.close()


# Insert reservation data
def insertData(parameters):
    
    conn = sqlite3.connect('testi.db')
    cursor = conn.cursor()
        
    insert_moving_time = """
    INSERT INTO Booking 
      (go_in, go_out, username) 
       VALUES (?, ?, ?);
    """
    cursor.execute(insert_moving_time, parameters)
    
    print("Data inserted successfully");     
    
    conn.commit()
    conn.close()


# Insert user data
def insertUser(parameters):
    conn = sqlite3.connect('testi.db')
    cursor = conn.cursor()

    insert_user = """
    INSERT INTO User
      (username, userpass, lastname, firstname) 
       VALUES (?,?,?,?);
    """
    cursor.execute(insert_user, parameters)


    print("Record inserted successfully");

    conn.commit()
    conn.close()


#parameters = ("test", "test2")
#insertData(parameters)


# Print table (testing)
def printTable():

    conn = sqlite3.connect("testi.db")
    cursor = conn.cursor()

    print_booking_table = "SELECT * FROM Booking"
    cursor.execute(print_booking_table)
    
    rows = cursor.fetchall()

    for row in rows: 
        print("ID = ", row[0])
        print("Start_time = ", row[1])
        print("End_time = ", row[2])
        print("Username = ", row[3])

    conn.commit()
    conn.close()



#======== Testing ========#
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


