import paho.mqtt.client as mqtt

import configparser

config = configparser.ConfigParser()

config.read('config_zigbee.ini')

Pi_ip_address = config['zigbee2mqtt']['pi_ip_address']
Pi_ip_port = int(config['zigbee2mqtt']['pi_ip_port'])

client = mqtt.Client()

def on_message(client, userdata, msg):
	print(f"topic = {msg.topic}, payload = {msg.payload}")

def run_sub_events():
	client.on_message = on_message
	client.connect(Pi_ip_address, Pi_ip_port) 
	client.subscribe("zigbee2mqtt/bridge/event")
	client.loop_start()
	#client.disconnect()
	

