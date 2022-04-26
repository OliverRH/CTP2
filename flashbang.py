import paho.mqtt.client as mqtt
import json


def on_message(client, userdata, msg):
	#print(f"topic = {msg.topic}, payload = {msg.payload}")
	#print(msg.payload)
	tmp = msg.payload.decode("utf-8")
	
	tmp_split = tmp.split(",")
	print(tmp_split)
	print(tmp_split[1])
	
	tmp2xsplit = tmp_split[1].split(":")
	print(tmp2xsplit)
	lux = tmp2xsplit[1]
	if int(lux) < 430: payload = {"state":"OFF"}
	elif int(lux) > 430: payload = {"state":"ON"}
	# Encode to a JSON string
	json_str = json.dumps(payload)
	print(json_str)
	client.publish("zigbee2mqtt/0x842e14fffe9e2d85/set", json_str)

    
client = mqtt.Client()

client.on_message = on_message

client.connect("192.168.0.96", 1883)

client.subscribe("zigbee2mqtt/0x00158d0005729f18")

client.loop_forever()




