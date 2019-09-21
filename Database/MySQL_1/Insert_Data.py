"""
3.Example: Insert Data

- DELETE
- INSERT INTO / executemany
- SELECT
- WHERE
- ORDER BY
- UPDATE


TODO:   - INSERT if not exist
        - delete all data
        - restart primary_key (id)
            https://stackoverflow.com/questions/740358/reorder-reset-auto-increment-primary-key
        - exercise: add column "Bike-Model" "Bike-Brand" and update data

source: https://www.datacamp.com/community/tutorials/mysql-python

Author: Oliver Zott
Date: 01.09.2019
"""

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='python_db1'
)

cursor = mydb.cursor()

cursor.execute("SHOW TABLES")
print(cursor.fetchall())
cursor.execute("DESC users")
print(cursor.fetchall())


# ----------------------------------------------------------------------
# DELETE:
# delete all existing first:
query = "DELETE FROM users"
# query = "DELETE FROM users WHERE name = 'Olli'"
cursor.execute(query)
mydb.commit()


# ----------------------------------------------------------------------
# INSERT:
# defining the query (%s not the same as python-string formatting!)
query = "INSERT IGNORE INTO users (name, bike) VALUES (%s, %s)"
values = [
    ("Lena", "Trance"),
    ("Olli", "StumpJumper"),
    ("Hautschi", "Capra"),
    ("Pipo", "Spectral"),
    ("Dave", "301")
    ]

# if more then one insert --> executemany!
cursor.executemany(query, values)

mydb.commit()

print()
print(cursor.rowcount, "record inserted")


# ----------------------------------------------------------------------
# SELECT:
# defining the query
query = "SELECT * FROM users"

# get ALL records from table
cursor.execute(query)
records = cursor.fetchall()
for data in records:
    print(data)

# get specific COLUMN
query = "SELECT name FROM users"
cursor.execute(query)
username = cursor.fetchall()
print()
for user in username:
    print(user)


# ----------------------------------------------------------------------
# WHERE:
query = "SELECT * FROM users WHERE name = 'Lena'"
cursor.execute(query)
records = cursor.fetchall()
print()
for recs in records:
    print(recs)


# ----------------------------------------------------------------------
# ODER BY: (DESC for descending order)
query = "SELECT * FROM users ORDER BY name DESC"
cursor.execute(query)
order = cursor.fetchall()
print()
for ord in order:
    print(ord)


# ----------------------------------------------------------------------
# UPDATE:
query = "UPDATE users SET name = 'Christoph' WHERE name = 'Hautschi'"
cursor.execute(query)
mydb.commit()

# checking change:
query = "SELECT * FROM users"
cursor.execute(query)
data = cursor.fetchall()
print()
print("Updated 'Hautisch' to 'Christoph': ")
for dat in data:
    print(dat)

print()
print("DESC users: ")
print(cursor.execute("DESC users"))
