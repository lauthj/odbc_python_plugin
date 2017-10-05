'''
Created on Oct 4, 2017

@author: lauthjo
'''
import pyodbc
import requests

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost\DEV;DATABASE=test;UID=test;PWD=odbctest')

cursor = conn.cursor()

# Execute a SQL Query
cursor.execute("SELECT TOP 10 id FROM test")

# Get the first row in the results
row = cursor.fetchone()

print("id:", row.id)


