"""
1.Example: Connect / Check

 - Connect
 - Check Databases

 - if import not working: --> File->Settings->Project Interpreter
 - first connect wamp server

sources: https://www.datacamp.com/community/tutorials/mysql-python

Author: Oliver Zott
Date: 31.08.2019
"""

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
)


''' Test if Database exists '''
print(mydb)


''' Create table in db '''
# creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
cursor = mydb.cursor()

# 'execute()' method is used to compile a 'SQL' statement
cursor.execute("CREATE DATABASE IF NOT EXISTS python_db1")


''' check Databases '''
cursor.execute("SHOW DATABASES")

# 'fetchall()' method fetches all the rows from the last executed statement
databases = cursor.fetchall()
print()
print(databases)
for dbs in databases:
    print(dbs)

print()
cursor.execute("SHOW DATABASES")
for x in cursor:
    print(x)
