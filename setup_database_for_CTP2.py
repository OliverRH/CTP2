from setup_database import *
import sys
import time
import configparser

#Creates config.ini file that contains credentials for database login and information about the database 
#----------------------------------------------------------------
config = configparser.ConfigParser()
    
def create_config_file(ip_host, db_user, db_pass, CTP2_db_name, CTP2_db_table_name, CTP2_db_table_columns_names):

    config['mySQL_login'] = {'ip_host': ip_host,
                             'db_user': db_user,
                             'db_pass': db_pass}
    
    config['mySQL_db'] = {'CTP2_db_name': CTP2_db_name,
                          'CTP2_db_table_name': CTP2_db_table_name,
                          'CTP2_db_table_columns_names': ', '.join(CTP2_db_table_columns_names)}
    
    with open('config_db.ini', 'w+') as configfile:
        config.write(configfile)
#----------------------------------------------------------------


#Automatic creation of SQL database for CTP2 projct

print("\n----------------------------------------------------------------")
print("IP address of host:", sys.argv[1])
print("\nName of database user:", sys.argv[2])
print("\nThe password of database user:", sys.argv[3])
print("----------------------------------------------------------------\n")

ip_host = sys.argv[1]
db_user = sys.argv[2]
db_pass = sys.argv[3]

#Variables for database:
#----------------------------------------------------------------
CTP2_db_name = "test1234"
CTP2_db_table_name = "table_in_test1234"
CTP2_db_table_columns_names = ["Pi_data", "Pi_time"]
#----------------------------------------------------------------


CTP2_db_table_columns_create =   "(" + CTP2_db_table_columns_names[0] + " VARCHAR(100), " + CTP2_db_table_columns_names[1] + " DATETIME)"       
column_names = CTP2_db_table_columns_names[0] + ", " + CTP2_db_table_columns_names[1]

#create_database(ip_host, db_user, db_pass, CTP2_db_name)
#time.sleep(1)
#create_table_in_database(ip_host, db_user, db_pass, CTP2_db_name, CTP2_db_table_name, CTP2_db_table_columns_create)
#time.sleep(1)
create_config_file(ip_host, db_user, db_pass, CTP2_db_name, CTP2_db_table_name, CTP2_db_table_columns_names)
