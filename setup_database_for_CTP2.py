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
CTP2_db_table_success_failures = str("db_table_success_failures")
CTP2_db_table_login = str("db_table_login")
CTP2_db_table_zigbee = str("db_table_zigbee")
CTP2_db_table_room_columns_names = ["id", "Pi_room", "Pi_time"]
CTP2_db_table_success_failures_columns_names = ["id", "Pi_room", "Pi_time", "Status"]
CTP2_db_table_login_columns_names = ["id", "username", "user_password", "usertype"]
CTP2_db_table_zigbee_columns_names = ["id", "Zigbee_name", "Zigbee_addr"]

zigbee_name_sensor = str("Sensor")
zigbee_addr_sensor = str("Sensor")

zigbee_name_LED = str("LED")
zigbee_addr_LED = str("LED")
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

CTP2_db_table_zigbee_columns_create = "(" + CTP2_db_table_zigbee_columns_names[0] + " int NOT NULL AUTO_INCREMENT, " + CTP2_db_table_zigbee_columns_names[1] + " VARCHAR(100) NOT NULL, " + CTP2_db_table_zigbee_columns_names[2] + " VARCHAR(100) NOT NULL, PRIMARY KEY (" + CTP2_db_table_zigbee_columns_names[0] + "))"      

CTP2_db_table_success_failures_columns_create = "(" + CTP2_db_table_success_failures_columns_names[0] + " int NOT NULL AUTO_INCREMENT, " + CTP2_db_table_success_failures_columns_names[1] + " VARCHAR(100) NOT NULL, " + CTP2_db_table_success_failures_columns_names[2] + " VARCHAR(100) NOT NULL, " + CTP2_db_table_success_failures_columns_names[3] + " VARCHAR(100) NOT NULL, PRIMARY KEY (" + CTP2_db_table_success_failures_columns_names[0] + "))"      


create_database(ip_host, db_user, db_pass, CTP2_db_name)
time.sleep(1)
create_table_in_database(ip_host, db_user, db_pass, CTP2_db_name, CTP2_db_table_room, CTP2_db_table_room_columns_create)
time.sleep(1)
create_table_in_database(ip_host, db_user, db_pass, CTP2_db_name, CTP2_db_table_login, CTP2_db_table_login_columns_create)
time.sleep(1)
create_table_in_database(ip_host, db_user, db_pass, CTP2_db_name, CTP2_db_table_zigbee, CTP2_db_table_zigbee_columns_create)
time.sleep(1)
create_table_in_database(ip_host, db_user, db_pass, CTP2_db_name, CTP2_db_table_success_failures, CTP2_db_table_success_failures_columns_create)
time.sleep(1)
create_config_zigbee_file(zigbee_addr_sensor, zigbee_addr_LED)
time.sleep(1)

zigbee_columns_names = CTP2_db_table_zigbee_columns_names[0] + ", " + CTP2_db_table_zigbee_columns_names[1] + ", " + CTP2_db_table_zigbee_columns_names[2]

CTP2_db_table_zigbee_columns_values_sensor = "NULL, " + "'" + zigbee_name_sensor + "'" + ", " + "'" + zigbee_addr_sensor + "'"
CTP2_db_table_zigbee_columns_values_LED = "NULL, " + "'" + zigbee_name_LED + "'" + ", " + "'" + zigbee_addr_LED + "'" 

print("CTP2_db_table_zigbee_pub_columns_values: " + CTP2_db_table_zigbee_columns_values_sensor)
insert_sql(ip_host, db_user, db_pass, CTP2_db_name, CTP2_db_table_zigbee, zigbee_columns_names, CTP2_db_table_zigbee_columns_values_sensor)
time.sleep(1)
print("CTP2_db_table_zigbee_pub_columns_values: " + CTP2_db_table_zigbee_columns_values_LED)
insert_sql(ip_host, db_user, db_pass, CTP2_db_name, CTP2_db_table_zigbee, zigbee_columns_names, CTP2_db_table_zigbee_columns_values_LED)


#print(CTP2_db_table_login_columns_values)

#insert_sql(ip_host, db_user, db_pass, CTP2_db_name, CTP2_db_table_login, CTP2_db_table_login_columns_names, CTP2_db_table_login_columns_values)