from datetime import datetime
import time
import random

from sql import createTable, insertData, insertUser, printTable

#Crete tables
createTable()

#Create Users for testing
users = [
    ('admin', 'ad123', 'Admin', 'Admin'),
    ('test', 'test123', 'Testi', 'Testi')
    ]

user_index = random.randint(0, 1)
print(user_index)
userData = users[user_index]
print(userData)

#Insert user to database table User
insertUser(userData)


#user_ids = [2233, 4324, 5134, 4234, 2431]

# user_index = random.randint(0, 4-1 )
# user_id = user_ids[user_index]

#Set time for testing
now = datetime.now()
start_time = now.strftime("%d/%m/%Y %H:%M:%S")
print(start_time)

time.sleep(3)
now = datetime.now()
end_time = now.strftime("%d/%m/%Y %H:%M:%S")

go_test = now.strftime("%d/%m/%Y %H:%M:%S")
print(go_test)

username = "Messi"

parameters = (start_time, end_time, username)

#insert data to table
insertData(parameters)

# user_name = "MacDavid"
# user_pass = "12ert"

# userInfo = (user_name, user_pass)

#insertUser(userInfo)

#printTable()