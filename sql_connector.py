import mysql.connector

from datetime import datetime

def insert_sql():
    mydb = mysql.connector.connect(
    host="192.168.87.164",
    user="oliver",
    password="1234",
    database="lightguide_data"
    )
    
    now = datetime.now() # current date and time
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    print("Date and time:", date_time)	

    val = "Light turned on"
    sql = "INSERT INTO test_data (Pi_data, Pi_time) VALUES"

    print(sql + " ('" + val + "', '" + date_time + "')")
    mycursor = mydb.cursor()
    mycursor.execute(sql + " ('" + val + "', '" + date_time + "')")

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


