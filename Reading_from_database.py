import mysql.connector

host=input("Enter the host: ")
user=input("Enter the username:")
password=input("Enter the password:")
database=input("Enter the name of the databse:")

try:
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
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