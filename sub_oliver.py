import paho.mqtt.client as mqtt
from time import sleep

client = mqtt.Client()

def on_message(client, userdata, msg):
	print(f"topic = {msg.topic}, payload = {msg.payload}")

def run_sub():
    
	client.on_message = on_message
	
	client.connect("localhost", 1883) 
	client.subscribe("testtopic")
	client.loop_start()
	client.disconnect()

