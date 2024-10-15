import mysql.connector

host=input("Enter the host: ")
user=input("Enter the username:")
password=input("Enter the password:")
database=input("Enter the name of the databse:")

try:
    if not host or not user or not password or not database:
        print("Error! Missing some details")
        exit()
    else:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    if conn.is_connected:
        print("Connection is connected")
        fcursor=conn.cursor()
        fcursor.execute("SELECT DATABASE();")
        name=fcursor.fetchall()
        print(name)
        table=input("Enter the table name form which you need data: ")
        if not table:
            print("Table doesn't exists in database!")
            exit()
        query="select* from "+table
        fcursor.execute(query)
        data=fcursor.fetchall()
    else:
        print("Couldn't connect")
    for row in data:
        print(row)
except Exception as e:
    print(f"Error is {e}")