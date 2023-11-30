import datetime
from time import time

from sql import createTable, insertData, printTable


createTable()

go_in = datetime.datetime.now()
print(go_in)
go_out = datetime.datetime.now()
user_id = 2233

parameters = (go_in, go_out, user_id)

insertData(parameters)

printTable()



print("Testi loppu")


