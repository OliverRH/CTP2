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
CTP2_db_name = "HAJTEK_Smart_Home_Care"
CTP2_db_table_room = "db_table_room"
CTP2_db_table_login = "db_table_login"
CTP2_db_table_room_columns_names = ["Pi_room", "Pi_time"]
#----------------------------------------------------------------

CTP2_db_table_room_columns_create =   "(" + CTP2_db_table_room_columns_names[0] + " VARCHAR(100), " + CTP2_db_table_room_columns_names[1] + " DATETIME)"       
column_names_room = CTP2_db_table_room_columns_names[0] + ", " + CTP2_db_table_room_columns_names[1]

create_database(ip_host, db_user, db_pass, CTP2_db_name)
time.sleep(1)
create_table_in_database(ip_host, db_user, db_pass, CTP2_db_name, CTP2_db_table_room, CTP2_db_table_room_columns_create)
time.sleep(1)
create_config_file(ip_host, db_user, db_pass, CTP2_db_name, CTP2_db_table_room, CTP2_db_table_room_columns_names)


#userlogin = input("Enter your username: ")
#userpass = input("Enter your password: ")

#CTP2_db_table_login_columns_names = ["id", "username", "password", "usertype"]

#CTP2_db_table_login_columns_create =   "(" + CTP2_db_table_login_columns_names[0] + " VARCHAR(100), " + CTP2_db_table_room_columns_names[1] + " VARCHAR(100))"       
#column_names_login = CTP2_db_table_login_columns_names[0] + ", " + CTP2_db_table_login_columns_names[1]




#create_table_in_database(ip_host, db_user, db_pass, CTP2_db_name, CTP2_db_table_login, CTP2_db_table_login_columns_create)
#time.sleep(1)
#create_config_file(ip_host, db_user, db_pass, CTP2_db_name, CTP2_db_table_login, CTP2_db_table_login_columns_names)

