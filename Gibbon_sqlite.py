import sqlite3
from sqlite3 import Error

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
    for time in timers:
        print(time)