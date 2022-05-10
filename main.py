from ast import If
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


room = "1" #Defines room number 1 as default
temp = 0 #Defines count value 
state = "inactive"
start_room_timer = 0
stop_room_timer = 0
start_room_timer =  datetime.now()

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
mqtt_connect(Pi_ip_address, Pi_ip_port) #Client IP address and port
mqtt_subscriber(Sensor_zigbee_addr)     #Subscribes to sensor
client.loop_start()                     #Starts listening
#----------------------------------------------------------------

#Function that converts string to boolean
#----------------------------------------------------------------
def str2bool(v): #Converts string to boolean
  return str(v).lower() in ("true", "1") #Returns true if string is true or 1  
#----------------------------------------------------------------

#Function that gets bool from subscriber mqtt
#----------------------------------------------------------------
movement = False                               #Definds movement boolean to false
def on_message(client, userdata, msg):
    global movement                            #Global movement variable
    global room                                #Global movement variable
    msg.payload = msg.payload.decode("utf-8")  #Converts message from MQTT publisher to utf-8 string
    tmp = msg.payload                          #Inserts the payload into a variable called "tmp"
    tmp = tmp.split(",")                       #Splits the payload into seperat elements
    occupancy_tmp = tmp[4].split(":")          #Retracts occupancy element from the sensor 
    occupancy =  occupancy_tmp[1]              #Gets the boolean value of occupancy
     
    if 7 < len(tmp):                           #The zigbee sensor payload does not contain the room number, 
        room_tmp = tmp[7].split(":")           #but when using our script that emulates a sensor, 
        room = room_tmp[1]                     #we can send the room number along, simulating a sensor in another room. 
    else:                                      #The information about the room number is a the 7th place in the array.
        room = "1"                             #Therefore if there is no 7th place in the array, it defaults to 1.
     
    print("Anyone there?: " + occupancy)       #Prints to terminal
    movement = str2bool(occupancy)             #The value from occupancy is a bool but in the format "string", this converts it to a boolean format
    turn_on_off(LED_zigbee_addr, movement)     #Function that turns on and off the LED depending on the boolean value. True = on, false = off
    #print(msg.topic + " " + str(msg.payload)) #Prints topic string and message string from MQTT publisher
#----------------------------------------------------------------

#Main forever loop
#----------------------------------------------------------------
print("System is active!")
while True: #While loops runs forever
    now = datetime.now() #Current date and time
    if 0 <= now.hour < 9 or 9 <= now.hour <= 23: #The system must be active between 22:00 and 9:00. (From 0:00 to 8:59 and 22:00 to 23:59) The system must automatically turn on/off when necessary
        state = "active"
        t_end = time.monotonic() + 1 #Gets python time and adds one second
        while time.monotonic() < t_end: #While the time is less than t_end then run
            client.on_message = on_message #Runs on_message (not function therefore no parentheses)
        print("Any movement at " + (now.strftime("%Y-%m-%d %H:%M:%S") - datetime.second(5)) + " " + str(movement)) #prints the current date and time, but commented our due to high system usage.
        temp += 1 #Count +1 every time the loop loops (every one second)
        if movement == True: #If movement is True, then insert date and time into the database.
            insert_timer_db(room, start_room_timer)
            #stop_room_timer = time.monotonic() - start_room_timer
            #movement_time = time.monotonic() #Gets python time 
            print("Insert SQL") #Placeholder for insert_sql command
            insert_timestamp(room) #Function from setup_database.py. Inserts the date and time into the database
            room_to_color_LED(LED_zigbee_addr, int(room)) #Changes the color of the LED to signal a specific room
            if room == "5": #If the person moved to room 5, then insert Success in database
                insert_timestamp_success_failures(room, "Success") 
            movement = False #Resets movement boolean to false after inserting SQL
            temp = 0 #Resest value is there is a movement
            start_room_timer = datetime.now()
        elif temp >= 30 and (1 < int(room) < 5): #If there is no movement after 30 seconds and the person is at any other room that bedroom (1) or toilet (5) then insert Failure in database
            print("Failure at: " + now.strftime("%Y-%m-%d %H:%M:%S") + " No movement for 30 seconds in room 2, 3 or 4. ")
            insert_timestamp_success_failures(room, "Failure") 
            turn_on_off(LED_zigbee_addr, False)
            room_to_color_LED(LED_zigbee_addr, 1)
            temp = 0 #Resest value is there is a movement
#----------------------------------------------------------------
