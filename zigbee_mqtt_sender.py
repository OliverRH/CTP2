import paho.mqtt.client as mqtt
import json

client = mqtt.Client()

def mqtt_subscriber(zigbbe_addr_subscriber):
    client.subscribe("zigbee2mqtt/" + zigbbe_addr_subscriber)

def mqtt_connect(ip_addr, port):
    client.connect(ip_addr, port)
      
def turn_on_off(zigbbe_addr, json_command):
    payload = {"state":json_command}
    json_str = json.dumps(payload)
    client.publish("zigbee2mqtt/" + zigbbe_addr + "/set", json_str)
    
def get_lux_from_sensor(client, userdata, msg):
	tmp = msg.payload.decode("utf-8")
	
	tmp_split = tmp.split(",")
	print(tmp_split)
	print(tmp_split[1])
	
	tmp2xsplit = tmp_split[1].split(":")
	print(tmp2xsplit)
	lux = tmp2xsplit[1]
	if int(lux) < 430: turn_on_off("0x842e14fffe9e2d85", "OFF")
	elif int(lux) > 430: turn_on_off("0x842e14fffe9e2d85", "ON")

def sensor_movement(client, userdata, msg): 
	tmp = msg.payload.decode("utf-8")
	
	tmp_split = tmp.split(",")
	print(tmp_split)
	print(tmp_split[1])
	
	tmp2xsplit = tmp_split[1].split(":")
	print(tmp2xsplit)
	lux = tmp2xsplit[1]
	return lux

def run_all():
    client.connect = mqtt_connect("192.168.0.96", 1883)
    client.on_message = get_lux_from_sensor
    client.subscribe = mqtt_subscriber("0x00158d0005729f18")