from cProfile import run
from pydoc import cli
from traceback import print_tb
from sql_connector import *
from zigbee_mqtt_sender import *
from datetime import datetime
from setup_database import *
import time
import paho.mqtt.client as mqtt
import configparser
import sys


room = "1"

#Read from config_zigbee.ini file
#----------------------------------------------------------------
config = configparser.ConfigParser()
config.read('config_zigbee.ini')
Pi_ip_address = config['zigbee2mqtt']['pi_ip_address']
Pi_ip_port = int(config['zigbee2mqtt']['pi_ip_port'])
LED_zigbee_addr = config['zigbee2mqtt']['zigbee_publisher_address']
Sensor_zigbee_addr = config['zigbee2mqtt']['zigbee_subscriber_address']
#----------------------------------------------------------------

#Connect to mqtt
#----------------------------------------------------------------
mqtt_connect(Pi_ip_address, Pi_ip_port)#Client IP address and port
mqtt_subscriber(Sensor_zigbee_addr) 
#client.subscribe("testtopic") #Publisher name topic
client.loop_start() #Starts listening
#----------------------------------------------------------------

#Function that converts string to boolean
#----------------------------------------------------------------
def str2bool(v): #Converts string to boolean
  return str(v).lower() in ("true", "1") #Returns true if string is true or 1  
#----------------------------------------------------------------

#Function that gets bool from subscriber mqtt
#----------------------------------------------------------------
movement = False #Definds movement boolean to false
def on_message(client, userdata, msg):
    global movement #Global movement variable
    msg.payload = msg.payload.decode("utf-8") #Converts message from MQTT publisher to utf-8 string
    tmp = msg.payload
    #room = tmp
    #print(room)
    tmp = tmp.split(",")
    print(tmp)
    tmp = tmp[4].split(":")
    occupancy = tmp[1]
    print("Anyone there?: " + occupancy)
    #movement = lux_threshold_bool(lux, 430)
    movement = str2bool(occupancy)
    turn_on_off(LED_zigbee_addr, movement)    
    #movement = str2bool(msg.payload) #Converts payload string from MQTT publisher to movement boolean
    #print(msg.topic + " " + str(msg.payload)) #Prints topic string and message string from MQTT publisher

#----------------------------------------------------------------

#Main forever loop
#----------------------------------------------------------------
while True: #While loops runs forever
    now = datetime.now() #Current date and time
    if 0 <= now.hour < 9 or 9 <= now.hour <= 23: #The system must be active between 22:00 and 9:00. (From 0:00 to 8:59 and 22:00 to 23:59) The system must automatically turn on/off when necessary
        t_end = time.monotonic() + 1 #Gets python time and adds one second
        while time.monotonic() < t_end: #While the time is less than t_end then run
            client.on_message = on_message #Runs on_message (not function therefore no parentheses)
        print("Any movement at " + now.strftime("%Y-%m-%d %H:%M:%S") + " " + str(movement)) #prints the current date and time, but commented our due to high system usage.
        if movement == True: #If movement is True, then insert date and time into the database.
            print("Insert SQL") #Placeholder for insert_sql command
            insert_timestamp(room)
            room_to_color_LED(LED_zigbee_addr, int(room))
            #insert_sql() #Function from sql_connector.py. Inserts the date and time into the database and prints the date and time
            movement = False #Resets movement boolean to false after inserting SQL
#----------------------------------------------------------------
