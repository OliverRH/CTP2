import paho.mqtt.client as mqtt
import json

client = mqtt.Client()

client.connect("localhost", 1883)
#{"state":"ON"}
#{"state":"OFF"}
#{"color":{"r":88,"g":102,"b":20}} grøn
# A Python dictionary with two keys
payload = {"state":"OFF"}
# Encode to a JSON string
json_str = json.dumps(payload)
print(json_str)



client.publish("testtopic", "true")

client.disconnect()


