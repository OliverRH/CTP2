import paho.mqtt.client as mqtt
import json

def mqtt_subscriber(zigbbe_addr_subscriber):
    client.subscribe("zigbee2mqtt/" + zigbbe_addr_subscriber)

def mqtt_connect(ip_addr, port):
    client.connect(ip_addr, port)
    
def turn_on_off(zigbbe_addr, json_command):
    payload = {"state":json_command}
    json_str = json.dumps(payload)
    client.publish("zigbee2mqtt/" + zigbbe_addr + "/set", json_str)

client = mqtt.Client()
client.connect = mqtt_connect("192.168.0.96", 1883)

client.on_message = turn_on_off("0x842e14fffe9e2d85", "ON")

client.subscribe = mqtt_subscriber("0x00158d0005729f18")

client.loop_forever()