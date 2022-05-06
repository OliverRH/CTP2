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

payload = '{"battery":100,"illuminance":839,"illuminance_lux":839,"linkquality":141,"occupancy":true,"temperature":25,"voltage":3025}'

json_str = json.loads(payload)
print(json_str)

client = mqtt.Client()
client.connect(Pi_ip_address, Pi_ip_port) 
client.publish(Sensor_zigbee_addr, str(json_str)) 
client.disconnect()


