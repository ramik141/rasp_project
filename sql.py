import sqlite3
import time

conn = sqlite3.connect('test2.db')

print("Database opened")

# conn.execute("""
#       DROP TABLE IF EXISTS Stime;  
# """)

# Create tables
def createTable():
    conn = sqlite3.connect('test2.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Stime
        (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        go_in  DATETIME NOT NULL,
        go_out DATETIME NOT NULL);
    ''')

    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS User
        (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        user_name  TEXT NOT NULL,
        user_pass  NOT NULL);
    ''')
   
    
    print("Tables created successfully")

    conn.commit()
    conn.close()


# conn = sqlite3.connect('test2.db')
# print("Created database successfully");

#createTable()


# Insert movement data
def insertData(parameters):
    
    conn = sqlite3.connect('test2.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Stime (go_in, go_out) \
                    VALUES (?, ?)", parameters);
    
    print("Record inserted successfully");     
    
    conn.commit()
    conn.close()

# Insert user data
def insertUser(parameters):
    conn = sqlite3.connect('test2.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO User (user_name, user_pass) \
                   VALUES (?,?)", parameters);

    print("Record inserted successfully");

    conn.commit()
    conn.close()


#parameters = ("test", "test2")
#insertData(parameters)

# Print tabel (testing)
def printTable():

    conn = sqlite3.connect("test2.db")

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Stime")
    rows = cursor.fetchall()

    for row in rows: 
        print("ID = ", row[0])
        print("GO_IN = ", row[1])
        print("GO_OUT = ", row[2])
        print("USER_ID = ", row[3])

    conn.commit()
    conn.close()

