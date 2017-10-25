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
import sys
import time
import oneagent_sdk
__version__ = oneagent_sdk.__version__

def looper():
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost\DEV;DATABASE=test;UID=test;PWD=odbctest')

    cursor = conn.cursor()

     # Execute a SQL Query
    cursor.execute("SELECT TOP 20 id FROM test order by 1 desc")

    # Get the first row in the results
    #row = cursor.fetchone()
    print(get_values(cursor))    


        
def get_values(cursor):
#    global counter
    mylist = [1] *20
    counter = 0
    
    for row in cursor:
        #counter = 0
        val =row.id
        #mylist = [1] *20
        mylist[counter] = val
        counter += 1
    return mylist    
        

        
#    print("id:", row.id)

#    print(counter)

#    cursor.execute("SELECT TOP 20 id FROM test order by 1 desc")

#   for row in cursor:
#        print(row.id)

def main(cmd_args, default_auth=False, default_ui=False):
    while(True):
        looper()
        time.sleep(3)
        
if __name__ == '__main__':
    main(sys.argv[1:])        