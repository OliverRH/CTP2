import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
	print(f"topic = {msg.topic}, payload = {msg.payload}")

client = mqtt.Client()

client.on_message = on_message

client.connect("192.168.0.96", 1883)

client.subscribe("zigbee2mqtt/0x00158d0005729f18")

client.loop_forever()
