import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
	print(f"topic = {msg.topic}, payload = {msg.payload}")

client = mqtt.Client()

client.on_message = on_message

client.connect("localhost", 1883)

client.subscribe("testtopic")

client.loop_forever()
