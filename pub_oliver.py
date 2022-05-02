import paho.mqtt.client as mqtt
import configparser

config = configparser.ConfigParser()

config.read('config_zigbee.ini')

Pi_ip_address = config['zigbee2mqtt']['pi_ip_address']
Pi_ip_port = int(config['zigbee2mqtt']['pi_ip_port'])

client = mqtt.Client()
client.connect(Pi_ip_address, Pi_ip_port) 
client.publish("testtopic", "true") 
client.disconnect()


