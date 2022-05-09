import time
from time import sleep
import paho.mqtt.client as mqtt
import configparser
import sys
import json

config = configparser.ConfigParser()

config.read('config_zigbee.ini')

Pi_ip_address = config['zigbee2mqtt']['pi_ip_address']
Pi_ip_port = int(config['zigbee2mqtt']['pi_ip_port'])
LED_zigbee_addr = config['zigbee2mqtt']['zigbee_publisher_address']
Sensor_zigbee_addr = config['zigbee2mqtt']['zigbee_subscriber_address']

def publish(room_number):
    payload = '{"battery":100,"illuminance":839,"illuminance_lux":839,"linkquality":141,"occupancy":true,"temperature":25,"voltage":3025,"room":' + str(room_number) + ',"blank": black}'
    
    client = mqtt.Client()
    client.connect("192.168.87.146", Pi_ip_port) 
    client.publish("zigbee2mqtt/Sensor", payload) 
    client.disconnect()

def bedroom_to_toilet_success():
    publish(1)
    time.sleep(4)
    publish(2)
    time.sleep(4)
    publish(3)
    time.sleep(4)
    publish(4)
    time.sleep(4)
    publish(5)
    
def bedroom_to_toilet_fail():
    publish(1)
    time.sleep(4)
    publish(2)
    time.sleep(4)
    publish(3)
    

what_test = input("Press 1 for 'bedroom_to_toilet_success'\nPress 2 for 'bedroom_to_toilet_fail'")

if(what_test == "1"):
    bedroom_to_toilet_success()
elif(what_test == "2"):
    bedroom_to_toilet_fail()
