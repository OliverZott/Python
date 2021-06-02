"""
1.Example: Connection

-

source: https://pynative.com/python-mysql-tutorial/
        https://www.python.org/dev/peps/pep-0249/

Author: Oliver Zott
Date: 02.09.2019
"""

import mysql.connector
from mysql.connector import Error


try:
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='python_db2'
    )

    if db.is_connected():
        db_Info = db.get_server_info()
        print("===================================================")
        print("Successfully connected to MySQL Server: ", db_Info )
        cursor = db.cursor()
        cursor.execute("SELECT DATABASE();")
        databases = cursor.fetchall()
        print("Your are connected to database: ", databases)
        print("===================================================")

    table_query = """CREATE TABLE IF NOT EXISTS SQL_lessons ( 
                             Id int(11) NOT NULL AUTO_INCREMENT,
                             Description VARCHAR(255),
                             Used_Language VARCHAR(255),
                             Time_Spend int(4),
                             Next VARCHAR(255),
                             PRIMARY KEY (Id)) """
    cursor.execute(table_query)
    print("Table successfully created!")

    # =============================================================================================
    # Add COLUMN for TIMESTAMP:
    # add_query1 = "ALTER TABLE SQL_lessons ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
    # cursor.execute(add_query1)


except Error as e:
    print("Error while connecting to MySQL: ", e)

finally:
    if db.is_connected():
        cursor.close()
        db.close()
        print("MySQL connection is closed.")


