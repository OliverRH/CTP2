import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost", 1883) 
client.publish("testtopic", "true") 
client.disconnect()


