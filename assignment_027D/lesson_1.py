''''
****************************************************************************
*  Program  lessson_5.py                                                   *
*  Author   Jacore Baptiste                                                       *
*  Date     March 16, 2021                                                 *
*  Source   Realpython https://realpython.com/python-sql-libraries/#sqlite *
*  Description:                                                            *
*  This program is used to introduce Geniuses to using a                   *
*  database Structured Query Language (SQL).  The program                  *
*  imports the sqlite3 module which allows you to create                   *
*  and interact with an SQL Database                                       *
*                                                                          *
*  - The create_connection function is passed the                          *
*    path of the SQLite database file then it connects                     *
*    the app to an exixting SQLite3 database named hgp_pods                *
*    or if it;s not present it creates the database file                   *
*                                                                          *
*  - The execute_query function is passed the path and the                 *
*    query to implement; create_staff_member_table query and               *
*    add_staff_member query                                                *
*                                                                          *
*  - The execute_read function is passed the path and                      *
*    the display_staff_member query                                        *
****************************************************************************

'''

import sqlite3
from sqlite3 import Error

############### Function Definitions *******************
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


###################  Connect/Create to the Sqlite3 Database File *********************
connection = create_connection("hgp2")


##########################  Create staff table variable query ################
create_staff_table_query = """
CREATE TABLE IF NOT EXISTS staff (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  cell TEXT NOT NULL,
  position TEXT NOT NULL
);
"""


create_leader_table_query = """
CREATE TABLE IF NOT EXISTS leader (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  cell TEXT NOT NULL,
  staff_id INTEGER NOT NULL,
  foreign key(staff_id) references staff(id)
);
"""

create_member_table_query = """
CREATE TABLE IF NOT EXISTS member (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  cell TEXT NOT NULL,
  leader_id INTEGER NOT NULL,
  foreign key(leader_id) references leader(id)
);
"""
#################### Executive query to create staff table #################
execute_query(connection,create_staff_table_query) 
execute_query(connection,create_leader_table_query) 
execute_query(connection,create_member_table_query) 

################# Create insert query to add staff members to staff table #######



  
