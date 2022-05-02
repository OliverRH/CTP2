from setup_database import *
import sys

#Automatic creation of SQL database for CTP2 projct

import sys

print("\n----------------------------------------------------------------")
print("IP address of host:", sys.argv[1])
print("\nName of database user:", sys.argv[2])
print("\nThe password of database user:", sys.argv[3])
print("----------------------------------------------------------------\n")

ip_host = sys.argv[1]
db_user = sys.argv[2]
db_pass = sys.argv[3]

CTP2_db_name = "test1234"
CTP2_db_table_name = "table_in_test1234"

CTP2_db_table_columns_names = ["Pi_data", "Pi_time"]

CTP2_db_table_columns_create =   "(" + "'" + CTP2_db_table_columns_names[0] + "'" + " VARCHAR(100), " + "'" + CTP2_db_table_columns_names[1] + "'" + " DATETIME)"   
    
column_names = CTP2_db_table_columns_names[0] + ", " + CTP2_db_table_columns_names[1]
    
#create_database(ip_host, db_user, db_pass, CTP2_db_name)

#create_table_in_database(ip_host, db_user, db_pass, CTP2_db_name, CTP2_db_table_name, CTP2_db_table_columns_create)

now = datetime.now() # current date and time
date_time = now.strftime("%Y-%m-%d %H:%M:%S")    

CTP2_db_table_columns_values = ["Time"]
column_values = "'" + CTP2_db_table_columns_values[0] + "'" + ", " + "'" + date_time + "'"

insert_sql(ip_host, db_user, db_pass, CTP2_db_name, CTP2_db_table_name, column_names, column_values)