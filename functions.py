import mysql.connector
from mysql.connector import Error
from datetime import datetime
import configparser
import time
import paho.mqtt.client as mqtt
import json

class database_functions:
    
    config = configparser.ConfigParser()

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
        mydb = database_functions.connect_to_server(ip_host, db_user, db_pass)
        mycursor = mydb.cursor()
        
        mycursor.execute("CREATE DATABASE " + new_db_name)
        print("Created database: " + new_db_name)
        mydb.close()


    def show_databases(ip_host, db_user, db_pass):
        mydb = database_functions.connect_to_server(ip_host, db_user, db_pass)
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
        mydb = database_functions.connect_to_db(ip_host, db_user, db_pass, db_name)
        mycursor = mydb.cursor()
        
        mycursor.execute("CREATE TABLE " + new_table_name + " " + table_columns_names)
        print("Created table named: " + new_table_name)
        mydb.close()
            


    def insert_sql(ip_host, db_user, db_pass, db_name, table_name, table_columns_names, table_columns_values):
        mydb = database_functions.connect_to_db(ip_host, db_user, db_pass, db_name)
        sql = "INSERT INTO " + table_name + " (" + table_columns_names + ") VALUES " + "(" + table_columns_values + ")"
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")


    def insert_timestamp(room_number):
        now = datetime.now() # current date and time
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")  
        
        column_values = "NULL, " + "'" + room_number + "'" + ", " + "'" + date_time + "'"

        config = database_functions.config

        config.read('config_db.ini')
        #print(config['mySQL_login']['db_user'])

        ip_host = config['mySQL_login']['ip_host']
        db_user = config['mySQL_login']['db_user']
        db_pass = config['mySQL_login']['db_pass']
        
        CTP2_db_name = config['mySQL_db']['ctp2_db_name']
        CTP2_db_table_room = config['mySQL_db']['ctp2_db_table_room']
        
        column_names_room = config['mySQL_db']['ctp2_db_table_room_columns_names']

        database_functions.insert_sql(ip_host, db_user, db_pass, CTP2_db_name, CTP2_db_table_room, column_names_room, column_values)

    def insert_timestamp_success_failures(room_number, success_failures):
        now = datetime.now() # current date and time
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")  
        
        column_values = "NULL, " + "'" + room_number + "'" + ", " + "'" + date_time + "'" + ", " + "'" + success_failures + "'"

        config = database_functions.config

        config.read('config_db.ini')
        #print(config['mySQL_login']['db_user'])

        ip_host = config['mySQL_login']['ip_host']
        db_user = config['mySQL_login']['db_user']
        db_pass = config['mySQL_login']['db_pass']
        
        CTP2_db_name = config['mySQL_db']['ctp2_db_name']
        CTP2_db_table_room = config['mySQL_db']['ctp2_db_table_success_failures']
        
        column_names_room = config['mySQL_db']['ctp2_db_table_success_failures_columns_names']

        database_functions.insert_sql(ip_host, db_user, db_pass, CTP2_db_name, CTP2_db_table_room, column_names_room, column_values)


    def insert_timer_db(room_number, room_timer):
        time_diff = datetime.now() - room_timer # current date and time
        diff = time_diff.total_seconds()
        diff_split = str(diff).split('.')
        print(diff_split[0])
        
        print(time_diff)
        
        column_values = "NULL, " + "'" + room_number + "'" + ", " + "'" + diff_split[0] + "'"

        config = database_functions.config

        config.read('config_db.ini')
        #print(config['mySQL_login']['db_user'])

        ip_host = config['mySQL_login']['ip_host']
        db_user = config['mySQL_login']['db_user']
        db_pass = config['mySQL_login']['db_pass']
        
        CTP2_db_name = config['mySQL_db']['ctp2_db_name']
        CTP2_db_table_room = config['mySQL_db']['ctp2_db_table_room_timer']
        
        column_names_room = config['mySQL_db']['ctp2_db_table_room_timer_columns_names']

        database_functions.insert_sql(ip_host, db_user, db_pass, CTP2_db_name, CTP2_db_table_room, column_names_room, column_values)



class zigbee2mqtt:
        
    client = mqtt.Client()

    def mqtt_subscriber(zigbbe_addr_subscriber):
        client.subscribe("zigbee2mqtt/" + zigbbe_addr_subscriber)
        print("Subscribing to: " + zigbbe_addr_subscriber)

    def mqtt_publisher(zigbbe_addr_publisher, json_str):
        client.publish("zigbee2mqtt/" + zigbbe_addr_publisher + "/set", json_str)

    def mqtt_connect(ip_addr, port):
        client.connect(ip_addr, port)
        print("Connected to: \n")
        print("Ip_address: " + ip_addr)
        print("Port: " + str(port))
        
    def turn_on_off(zigbbe_addr, bool_data):
        if bool_data == True: 
            payload = {"state":"ON"}
        elif bool_data == False:
            payload = {"state":"OFF"}
            
        json_str = json.dumps(payload)
        mqtt_publisher(zigbbe_addr, json_str)
        #client.publish("zigbee2mqtt/" + zigbbe_addr + "/set", json_str)
        
    def room_to_color_LED(zigbbe_addr, room):
        if room == 1:
            payload = {"color":{"r":255,"g":0,"b":0}}  #red
        elif room == 2:
            payload = {"color":{"r":0,"g":255,"b":0}} #green
        elif room == 3:
            payload = {"color":{"r":0,"g":0,"b":255}} #blue
        elif room == 4:
            payload = {"color":{"r":255,"g":255,"b":0}} #
        elif room == 5:
            payload = {"color":{"r":255,"g":0,"b":255}} #megenta
        else:
            print("Invalid room number: " + str(room) + ", defaults to room 1!")
            payload = {"color":{"r":255,"g":0,"b":0}}  #red
        
        json_str = json.dumps(payload)
        mqtt_publisher(zigbbe_addr, json_str)
        
    def lux_threshold_bool(lux, threshold):
        if int(lux) > threshold: 
            return True
        elif int(lux) < threshold:
            return False
        
    def get_lux_from_sensor(client, userdata, msg):
        tmp = msg.payload.decode("utf-8")
        
        tmp_split = tmp.split(",")
        print(tmp_split)
        print(tmp_split[1])
        
        tmp2xsplit = tmp_split[1].split(":")
        print(tmp2xsplit)
        lux = tmp2xsplit[1]
        if int(lux) < 430: turn_on_off("0x842e14fffe9e2d85", "OFF")
        elif int(lux) > 430: turn_on_off("0x842e14fffe9e2d85", "ON")

    def sensor_movement(client, userdata, msg): 
        tmp = msg.payload.decode("utf-8")
        
        tmp_split = tmp.split(",")
        print(tmp_split)
        print(tmp_split[1])
        
        tmp2xsplit = tmp_split[1].split(":")
        print(tmp2xsplit)
        lux = tmp2xsplit[1]
        return lux

    def run_all():
        client.connect = mqtt_connect("192.168.0.96", 1883)
        client.on_message = get_lux_from_sensor
        client.subscribe = mqtt_subscriber("0x00158d0005729f18")
