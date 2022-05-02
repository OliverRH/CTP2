import mysql.connector
from mysql.connector import Error
from datetime import datetime

#Functions for connection and setting up SQL database, tables and more

def connect_to_server(ip_host, db_user, db_pass):
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host = ip_host,
                                       user = db_user,
                                       password = db_pass)
        if conn.is_connected():
            print('Connected to MySQL database server')
            return conn

    except Error as e:
        print(e)

def connect_to_db(ip_host, db_user, db_pass, db_name):
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host = ip_host,
                                       user = db_user,
                                       password = db_pass,
                                       database = db_name)
        if conn.is_connected():
            print('Connected to MySQL database named: ' + db_name)
            return conn

    except Error as e:
        print(e)


def create_database(ip_host, db_user, db_pass, new_db_name):
    mydb = connect_to_server(ip_host, db_user, db_pass)
    mycursor = mydb.cursor()
    
    mycursor.execute("CREATE DATABASE " + new_db_name)
    print("Created database: " + new_db_name)
    mydb.close()


def show_databases(ip_host, db_user, db_pass):
    mydb = connect_to_server(ip_host, db_user, db_pass)
    mycursor = mydb.cursor()
    
    mycursor.execute("SHOW DATABASES")
    databases = mycursor.fetchall()
    print("\nCurrent databases: ")
    for database in databases:
        print(database)
    #databases = [ i[0] for i in databases ]
    #print(databases)
    mydb.close()
    
    
def create_table_in_database(ip_host, db_user, db_pass, db_name, new_table_name, table_columns_names):
    mydb = connect_to_db(ip_host, db_user, db_pass, db_name)
    mycursor = mydb.cursor()
    
    mycursor.execute("CREATE TABLE " + new_table_name + " " + table_columns_names)
    print("Created table named: " + new_table_name)
    mydb.close()
        


def insert_sql(ip_host, db_user, db_pass, db_name, table_name, table_columns_names, table_columns_values):
    mydb = connect_to_db(ip_host, db_user, db_pass, db_name)
    sql = "INSERT INTO " + table_name + " (" + table_columns_names + ") VALUES " + "(" + table_columns_values + ")"
    print(sql)
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")



    
