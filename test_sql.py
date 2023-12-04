from datetime import datetime
import time
import random

from sql import createTable, insertData, insertUser, printTable

#Crete tables
createTable()

#Create Users for testing
users = [
    ('Litmanen', 'ertw1'),
    ('Pukki', 'erwre2'),
    ('Messi', 'werw3'),
]

user_data = random.randint(0, 3-1)
print(user_data)
userInfo = users[user_data]
print(userInfo)
insertUser(userInfo)


#user_ids = [2233, 4324, 5134, 4234, 2431]

# user_index = random.randint(0, 4-1 )
# user_id = user_ids[user_index]

#Set time for testing
now = datetime.now()
go_in = now.strftime("%d/%m/%Y %H:%M:%S")
print(go_in)

time.sleep(3)
now = datetime.now()
go_out = now.strftime("%d/%m/%Y %H:%M:%S")

go_test = now.strftime("%d/%m/%Y %H:%M:%S")
print(go_test)

parameters = (go_in, go_out)

#insert Data to table
insertData(parameters)

user_name = "MacDavid"
user_pass = "12ert"

userInfo = (user_name, user_pass)

insertUser(userInfo)

#printTable()



print("Test loppu")

