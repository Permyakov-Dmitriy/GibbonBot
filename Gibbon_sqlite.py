import sqlite3
from sqlite3 import Error

from utils.sql_orm import *

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(query):
    connection = create_connection("sm_app.sqlite")
    cursor = connection.cursor()

    try:
        if isinstance(query, (Comand, Insert)):
            query = query._query

        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

    connection.close()

def execute_read_query(query):
    connection = create_connection("sm_app.sqlite")
    cursor = connection.cursor()
    result = None

    if isinstance(query, Select):
            query = query._query

    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

    connection.close()


select_timers = "SELECT * from Timer"
timers = execute_read_query(select_timers)


if __name__ == "__main__":
    print('''
    Comand:
        1. Clear table Timer
        2. Add column in Timer
        3. Delete timer for id
        4. Update data in db
    ''')

    cmd =  input('Input num cmd: ')
    
    match cmd:
        case '1':
            query = Delete().where('id > 0')

        case '2':
            column = input('Column name: ')
            type_column = input('Type [int, varchar(255), boolean, ...]: ')

            query = f'ALTER TABLE Timer ADD {column} {type_column}'

        case '3':
            id_timer = input('ID: ')

            query = Delete().where(f'id = {id_timer}')

        case '4':
            id_row = input('ID: ')
            column = input('Column: ')
            new_val = input('New value: ')

            if column in ["schedule", "name"]:
                new_val = "'" + new_val + "'"

            query = Update(f'{column} = {new_val}').where(f'id = {id_row}')


    query = execute_query(query)