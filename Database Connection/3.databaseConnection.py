import mysql.connector

try:
    conn = mysql.connector.connect(
        user="root",
        host="localhost",
        password="",
        database="student"  # Replace with your actual database name
    )
    if conn.is_c.onnected():
        print(conn)
        print("Hello")
        cursor = conn.cursor()
        print("Connected to the MySQL database server")
        # cursor.execute("CREATE DATABASE  abcD;")

        # cursor.execute("CREATE TABLE dataa (ID INT PRIMARY KEY, NAME VARCHAR(255));")
        # print("Table created successfully")
        cursor.execute("USE student;")
        print("Connected to the student database")
        # cursor.execute("Insert into st (ID, NAME) values (3, 'Huxn');")
        cursor.execute("Commit;")       
        print("Data inserted successfully")
        cursor.execute("SELECT * FROM st;")
        res = cursor.fetchall()
        for i in res:
            print(i)
        
        

        # cursor.execute("INSERT INTO ST (ID, NAME) VALUES (1, 'Huxn');")
        # cursor.execute("INSERT INTO ST (ID, NAME) VALUES (2, 'Manish');")
        
     
except mysql.connector.errors.InterfaceError as e:
    print(f"{e}")


