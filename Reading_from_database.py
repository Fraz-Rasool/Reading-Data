import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="5371240.Fr",
        database="sakila"
    )

    if conn.is_connected:
        print("Connection is connected")
        fcursor=conn.cursor()
        query="select * from actor;"
        fcursor.execute(query)
        data=fcursor.fetchall()
    else:
        print("Couldn't connect")

    for row in data:
        print(row)
except Exception as e:
    print(f"Error is {e}")
