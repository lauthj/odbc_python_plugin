'''
Created on Oct 19, 2017

@author: lauthjo
'''
from nt import lstat
'''
Created on Oct 4, 2017

@author: lauthjo
'''
import pyodbc
import argparse
import sys
import time
import bottle
from statistics import mean

    
# Parse the command line arguments passed to the app
def create_args_parser(default_port=8770):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--port',
        action='store',
        default=default_port,
        type=int,
        nargs='?',
        help='Port of the demo application [default %s]' % default_port
    )
    return parser
    
def looper():
    while(True):
        # Print the current stats values
        print(stats()) 

        # Sleep before re-running
        time.sleep(3)
     
        
def stats():
    
    # Create the connection string
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost\DEV;DATABASE=test;UID=test;PWD=odbctest')

    cursor = conn.cursor()

    # Execute a SQL Query
    cursor.execute("SELECT TOP 20 id FROM test order by 1 desc")
   
    # Get the first row in the results
    return {"value": get_values(cursor,mean)}

# Map values for the DB cursor
def get_values(cursor,fn):
    # Create initial values
    mylist = []
    # Loop through the cursor rows
    for row in cursor:
        mylist.append(row.id)
    # Return the list
    return fn(mylist)
 
def main(cmd_args, default_port=8770):
    parser = create_args_parser(default_port=default_port)
    args = parser.parse_args(cmd_args)

    # Bottle / route
    bottle.route('/')(stats)

    # Run the bottle app
    bottle.run(host='localhost', port=args.port)

# If the file is being called directly (i.e this is the main file) run main
if __name__ == '__main__':
    main(sys.argv[1:])