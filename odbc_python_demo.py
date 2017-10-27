'''
Created on Oct 19, 2017

@author: lauthjo
'''
'''
Created on Oct 4, 2017

@author: lauthjo
'''
import pyodbc
import argparse
import requests
import sys
import time
import oneagent_sdk
__version__ = oneagent_sdk.__version__
import bottle
from symbol import decorated


def get_stats():
    """
    Main app logic returns two stats - an ever increasing counter and a random number.
    """
    return {looper()}

def stats():
    global ui_metrics_enabled
    return get_stats()
    
class RegisterCalledAction(argparse._StoreAction):
    called = False

    def __call__(self, parser, namespace, values, option_string=None):
        self.called = True
        return super().__call__(parser, namespace, values, option_string)
    
def create_args_parser(default_auth=False, default_port=8770, default_ui=False):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--auth',
        action='store_true',
        default=default_auth,
        help='Protect stats page with HTTP basic auth'
    )
    parser.add_argument(
        '--ui',
        action='store_true',
        default=default_ui,
        help='Generate additional metrics for UI demo'
    )
    parser.add_argument(
        '-p', '--port',
        action='store',
        default=default_port,
        type=int,
        nargs='?',
        help='Port of the demo application [default %s]' % default_port
    )
    user_action = parser.add_argument(
        '--user',
        action=RegisterCalledAction,
        default='ruxit',
        type=str,
        nargs='?',
        help='Username for authentication (implies auth)'
    )
    password_action = parser.add_argument(
        '--password',
        action=RegisterCalledAction,
        default='ruxit',
        type=str,
        nargs='?',
        help='Password for authentication (implies auth)'
    )
    parser.add_argument(
        '--version',
        action="version",
        help="show program's version and exit",
        version=('{name} {version}'.format(name=__loader__.name, version=__version__))
    )
    return parser, password_action, user_action        
    
def looper():
    while(True):
        time.sleep(3) 
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

def decorate(func):
    def call(looper):
        result = func(looper())
        return result
        return call
    return decorate
        

        
#    print("id:", row.id)

#    print(counter)

#    cursor.execute("SELECT TOP 20 id FROM test order by 1 desc")

#   for row in cursor:
#        print(row.id)


def main(cmd_args, default_auth=False, default_port=8770, default_ui=False):
    parser, password_action, user_action = create_args_parser(default_auth=default_auth, default_port=default_port, default_ui=default_ui)
    args = parser.parse_args(cmd_args)
    global stats
    global ui_metrics_enabled
    ui_metrics_enabled = args.ui
    stats = bottle.route('/')(stats)
    bottle.run(host='localhost', port=args.port)
#    looper()
        
if __name__ == '__main__':
    main(sys.argv[1:])