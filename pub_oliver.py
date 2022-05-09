import paho.mqtt.client as mqtt
import configparser
import sys
import json

room = sys.argv[1]

config = configparser.ConfigParser()

config.read('config_zigbee.ini')

Pi_ip_address = config['zigbee2mqtt']['pi_ip_address']
Pi_ip_port = int(config['zigbee2mqtt']['pi_ip_port'])
LED_zigbee_addr = config['zigbee2mqtt']['zigbee_publisher_address']
Sensor_zigbee_addr = config['zigbee2mqtt']['zigbee_subscriber_address']

payload = '{"battery":100,"illuminance":839,"illuminance_lux":839,"linkquality":141,"occupancy":true,"temperature":25,"voltage":3025,"room":' + room + ',"blank": black}'

json_str = json.dumps(payload)
print(json_str)

client = mqtt.Client()
client.connect("192.168.87.146", Pi_ip_port) 
client.publish("zigbee2mqtt/LED", payload) 
client.disconnect()


