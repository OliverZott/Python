"""
2.Example: Create Tables, alter columns

- CREATE TABLE
- DROP TABLE
- SHOW TABLES
- DESC


source: https://www.datacamp.com/community/tutorials/mysql-python

Author: Oliver Zott
Date: 31.08.2019
"""

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='python_db1'
)

cursor = mydb.cursor()

# DROP TABLE first to try around over and over again!
cursor.execute("DROP TABLE users")

# CREATE TABLE
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT(11)  NOT NULL AUTO_INCREMENT PRIMARY KEY, "
               "name VARCHAR(255), "
               "bike VARCHAR(255))"
               )

# SHOW TABLES
'''  NOT WORKING ?!?!?!
cursor.execute("DB_NAME() ")
database = cursor.fetchall()
'''
print()
print("All tables in database: ")
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()
for tabs in tables:
    print(tabs)

# 'DESC table_name' is used to get all COLUMNS information
print()
print("Columns in Table 'users': ")
cursor.execute("DESC users")
columns = cursor.fetchall()
for clms in columns:
    print(clms)
print()

# DROP Primary Key by ALTER
cursor.execute("ALTER TABLE users DROP id")
cursor.execute("DESC users")
print(cursor.fetchall())
print()

# ADD COLUMN primary key (first to make it first column!)
cursor.execute("ALTER TABLE users ADD COLUMN user_id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT FIRST")
cursor.execute("DESC users")
print(cursor.fetchall())
print()
