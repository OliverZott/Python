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
        print("Successfully connected to MySQL Server: ", db_Info)
        cursor = db.cursor()
        cursor.execute("SELECT DATABASE();")
        databases = cursor.fetchall()
        print("Your are connected to database: ", databases)
        print("===================================================")

    insert_query = """INSERT INTO sql_lessons (Description, Used_Language, Time_Spend, Next) VALUES (%s, %s, %s, %s)"""

    # Read from input

    val1 = input("Description of lesson: ")
    val2 = input("Used Language (Python, Java, PHP,...): ")
    val3 = input("Time spend for lesson [hours]: ")
    val4 = input("What to do next: ")
    values = (val1, val2, val3, val4)

    result = cursor.execute(insert_query, values)
    db.commit()
    print("Record insert successful")


except Error as e:
    print("Some error occurred: ", e)
