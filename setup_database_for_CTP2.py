from setup_database import *
import sys
import time
import configparser

#Creates config.ini file that contains credentials for database login and information about the database 
#----------------------------------------------------------------
config = configparser.ConfigParser()
    
def create_config_db_file(ip_host, db_user, db_pass, CTP2_db_name, CTP2_db_table_room, CTP2_db_table_login, CTP2_db_table_room_columns_names, CTP2_db_table_login_columns_names):

    config['mySQL_login'] = {'ip_host': ip_host,
                             'db_user': db_user,
                             'db_pass': db_pass}
    
    config['mySQL_db'] = {'CTP2_db_name': CTP2_db_name,
                          'CTP2_db_table_room': CTP2_db_table_room,
                          'CTP2_db_table_login': CTP2_db_table_login,
                          'CTP2_db_table_room_columns_names': ', '.join(CTP2_db_table_room_columns_names),
                          'CTP2_db_table_login_columns_names': ', '.join(CTP2_db_table_login_columns_names)}
    
    with open('config_db.ini', 'w+') as configfile:
        config.write(configfile)
        
def create_config_zigbee_file(zigbee_subscriber_addr, zigbee_publisher_addr):
    
    config['zigbee2mqtt'] = {'pi_ip_address': "localhost",
                          'pi_ip_port': "1883",
                          'zigbee_subscriber_address': zigbee_subscriber_addr,
                          'zigbee_publisher_address': zigbee_publisher_addr }   
    
    with open('config_zigbee.ini', 'w+') as configfile:
        config.write(configfile)
#----------------------------------------------------------------


#Automatic creation of SQL database for CTP2 projct

ip_host = input("IP address of database server: ")
db_user = input("Enter the username of the database server: ")
db_pass = input("Enter the password of the database server: ")

print("\n----------------------------------------------------------------")
print("IP address of host:", ip_host)
print("\nName of database user:", db_user)
print("\nThe password of database user:", db_pass)
print("----------------------------------------------------------------\n")

#ip_host = sys.argv[1]
#db_user = sys.argv[2]
#db_pass = sys.argv[3]

#Variables for database:
#----------------------------------------------------------------
CTP2_db_name = str("HAJTEK_Smart_Home_Care") #Name of the database
CTP2_db_table_room = str("db_table_room")
CTP2_db_table_login = str("db_table_login")
CTP2_db_table_zigbee_sub = str("db_table_zigbee_sub")
CTP2_db_table_zigbee_pub = str("db_table_zigbee_pub")
CTP2_db_table_room_columns_names = ["id", "Pi_room", "Pi_time"]
CTP2_db_table_login_columns_names = ["id", "username", "user_password", "usertype"]
CTP2_db_table_zigbee_sub_columns_names = ["id", "Zigbee_name_sub", "Zigbee_addr_sub"]
CTP2_db_table_zigbee_pub_columns_names = ["id", "Zigbee_name_pub", "Zigbee_addr_pub"]

zigbee_name_sub = str("Sensor")
zigbee_addr_sub = str("0x00158d0005729f18")

zigbee_name_pub = str("LED")
zigbee_addr_pub = str("0x842e14fffe9e2d85")
#----------------------------------------------------------------




"""
userlogin = input("Please pick username for the login on HAJTEK Smart Home Care website: ")
userpass = input("Please pick password for the login on HAJTEK Smart Home Care website: ")


print("Press 1 for admin")
print("Press 2 for standard user")

usertype_input = int(input(""))

if usertype_input == 1:
    usertype = "admin"
elif usertype_input == 2:
    usertype = "user"
else:
    sys.exit("Error! Please try again")

print("\n----------------------------------------------------------------")
print("Username:", userlogin)
print("\nPassword:", userpass)
print("\nUsertype:", usertype)

print("----------------------------------------------------------------\n")
"""

CTP2_db_table_room_columns_create = "(" + CTP2_db_table_room_columns_names[0] + " int NOT NULL AUTO_INCREMENT, " + CTP2_db_table_room_columns_names[1] + " INT, " + CTP2_db_table_room_columns_names[2] + " DATETIME, PRIMARY KEY (" + CTP2_db_table_room_columns_names[0] + "))"      
#column_names_room = CTP2_db_table_room_columns_names[0] + ", " + CTP2_db_table_room_columns_names[1]

CTP2_db_table_login_columns_create = "(" + CTP2_db_table_login_columns_names[0] + " int NOT NULL AUTO_INCREMENT, " + CTP2_db_table_login_columns_names[1] + " VARCHAR(100) NOT NULL, " + CTP2_db_table_login_columns_names[2] + " VARCHAR(100) NOT NULL, " + CTP2_db_table_login_columns_names[3] + " VARCHAR(20) NOT NULL, PRIMARY KEY (" + CTP2_db_table_login_columns_names[0] + "))"      
#column_names_login = CTP2_db_table_login_columns_names[0] + ", " + CTP2_db_table_login_columns_names[1]

CTP2_db_table_zigbee_sub_columns_create = "(" + CTP2_db_table_zigbee_sub_columns_names[0] + " int NOT NULL AUTO_INCREMENT, " + CTP2_db_table_zigbee_sub_columns_names[1] + " VARCHAR(100) NOT NULL, " + CTP2_db_table_zigbee_sub_columns_names[2] + " VARCHAR(100) NOT NULL, PRIMARY KEY (" + CTP2_db_table_zigbee_sub_columns_names[0] + "))"      
CTP2_db_table_zigbee_pub_columns_create = "(" + CTP2_db_table_zigbee_pub_columns_names[0] + " int NOT NULL AUTO_INCREMENT, " + CTP2_db_table_zigbee_pub_columns_names[1] + " VARCHAR(100) NOT NULL, " + CTP2_db_table_zigbee_pub_columns_names[2] + " VARCHAR(100) NOT NULL, PRIMARY KEY (" + CTP2_db_table_zigbee_pub_columns_names[0] + "))"      
  

create_database(ip_host, db_user, db_pass, CTP2_db_name)
time.sleep(1)
create_table_in_database(ip_host, db_user, db_pass, CTP2_db_name, CTP2_db_table_room, CTP2_db_table_room_columns_create)
time.sleep(1)
create_table_in_database(ip_host, db_user, db_pass, CTP2_db_name, CTP2_db_table_login, CTP2_db_table_login_columns_create)
time.sleep(1)
create_table_in_database(ip_host, db_user, db_pass, CTP2_db_name, CTP2_db_table_zigbee_sub, CTP2_db_table_zigbee_sub_columns_create)
time.sleep(1)
create_table_in_database(ip_host, db_user, db_pass, CTP2_db_name, CTP2_db_table_zigbee_pub, CTP2_db_table_zigbee_pub_columns_create)
time.sleep(1)
create_config_zigbee_file(zigbee_addr_sub, zigbee_addr_pub)
time.sleep(1)

zigbee_sub_columns_names = CTP2_db_table_zigbee_sub_columns_names[0] + ", " + CTP2_db_table_zigbee_sub_columns_names[1] + ", " + CTP2_db_table_zigbee_sub_columns_names[2]
zigbee_pub_columns_names = CTP2_db_table_zigbee_pub_columns_names[0] + ", " + CTP2_db_table_zigbee_pub_columns_names[1] + ", " + CTP2_db_table_zigbee_pub_columns_names[2]

CTP2_db_table_zigbee_sub_columns_values = "NULL, " + "'" + zigbee_name_sub + "'" + ", " + "'" + zigbee_addr_sub + "'" 
CTP2_db_table_zigbee_pub_columns_values = "NULL, " + "'" + zigbee_name_pub + "'" + ", " + "'" + zigbee_addr_pub + "'"
print("CTP2_db_table_zigbee_pub_columns_values: " + CTP2_db_table_zigbee_pub_columns_values)

insert_sql(ip_host, db_user, db_pass, CTP2_db_name, CTP2_db_table_zigbee_sub, zigbee_sub_columns_names, CTP2_db_table_zigbee_sub_columns_values)
insert_sql(ip_host, db_user, db_pass, CTP2_db_name, CTP2_db_table_zigbee_pub, zigbee_pub_columns_names, CTP2_db_table_zigbee_pub_columns_values)


#print(CTP2_db_table_login_columns_values)

#insert_sql(ip_host, db_user, db_pass, CTP2_db_name, CTP2_db_table_login, CTP2_db_table_login_columns_names, CTP2_db_table_login_columns_values)