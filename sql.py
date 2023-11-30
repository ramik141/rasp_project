import sqlite3
import time

conn = sqlite3.connect('test2.db')

print("Database opened")


# conn.execute("""
#     DROP TABLE IF EXISTS Stime;  
#  """)

def createTable():
    conn = sqlite3.connect('test2.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Stime
        (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        go_in  TEXT NOT NULL,
        go_out TEXT NOT NULL,
        user_id INTEGER NOT NULL);
    ''')

    print("Table created successfully")

    conn.commit()
    conn.close()


conn = sqlite3.connect('test2.db')
print("Opened database successfully");


createTable()

def insertData(parameters):
    
    conn = sqlite3.connect('test2.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Stime (go_in, go_out, user_id) VALUES (?, ?, ?)", parameters);

    print ("Records created successfully");     
    
    conn.commit()
    conn.close()

#parameters = ("test", "test2")
#insertData(parameters)

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

"""
i = 1
while i <= 5:
    
    conn.execute("INSERT INTO Stime (go_in, go_out) \
          VALUES (datetime('now'), datetime('now'))");
    i += 1
    time.sleep(1)

conn.commit()
print ("Records created successfully");

conn.close()
"""
"""
conn = sqlite3.connect("test2.db")
print("Read all records")

cursor = conn.cursor()
cursor.execute("SELECT * FROM Stime")
rows = cursor.fetchall()

print("Company contents")
for row in rows:
    print("ID = ", row[0])
    print("GO_IN = ", row[1])
    print("GO_OUT = ", row[2])
    


conn.close()
"""
