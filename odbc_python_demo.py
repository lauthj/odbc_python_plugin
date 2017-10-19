'''
Created on Oct 19, 2017

@author: lauthjo
'''
'''
Created on Oct 4, 2017

@author: lauthjo
'''
import pyodbc
import requests

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost\DEV;DATABASE=test;UID=test;PWD=odbctest')

cursor = conn.cursor()

# Execute a SQL Query
cursor.execute("SELECT TOP 20 id FROM test order by 1 desc")

# Get the first row in the results
row = cursor.fetchone()
    
def get_values():
    global counter
    mylist = [1] *20
    counter = 0
    
    for row in cursor:
        #counter = 0
        val =row.id
        #mylist = [1] *20
        mylist[counter] = val
        counter += 1
    return mylist
        
print(get_values()) 
        
print("id:", row.id)

print(counter)

cursor.execute("SELECT TOP 20 id FROM test order by 1 desc")

for row in cursor:
    print(row.id)