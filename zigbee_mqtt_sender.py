from unittest import case
import paho.mqtt.client as mqtt
import json

client = mqtt.Client()

def mqtt_subscriber(zigbbe_addr_subscriber):
    client.subscribe("zigbee2mqtt/" + zigbbe_addr_subscriber)
    print("Subscribing to: " + zigbbe_addr_subscriber)

def mqtt_publisher(zigbbe_addr_publisher, json_str):
    client.publish("zigbee2mqtt/" + zigbbe_addr_publisher + "/set", json_str)

def mqtt_connect(ip_addr, port):
    client.connect(ip_addr, port)
    print("Connected to: \n")
    print("Ip_address: " + ip_addr)
    print("Port: " + str(port))
      
def turn_on_off(zigbbe_addr, bool_data):
    if bool_data == True: 
        payload = {"state":"ON"}
    elif bool_data == False:
        payload = {"state":"OFF"}
        
    json_str = json.dumps(payload)
    mqtt_publisher(zigbbe_addr, json_str)
    #client.publish("zigbee2mqtt/" + zigbbe_addr + "/set", json_str)
    
def room_to_color_LED(zigbbe_addr, room):
    if room == 1:
        payload = {"color":{"r":255,"g":0,"b":0}}  #red
    elif room == 2:
        payload = {"color":{"r":0,"g":255,"b":0}} #green
    elif room == 3:
        payload = {"color":{"r":0,"g":0,"b":255}} #blue
    elif room == 4:
        payload = {"color":{"r":255,"g":255,"b":0}} #
    elif room == 5:
        payload = {"color":{"r":255,"g":0,"b":255}} #megenta
    else:
        print("Invalid room number: " + str(room) + "Defaults to room 1")
        payload = {"color":{"r":255,"g":0,"b":0}}  #red
    
    json_str = json.dumps(payload)
    mqtt_publisher(zigbbe_addr, json_str)
    
def lux_threshold_bool(lux, threshold):
    if int(lux) > threshold: 
        return True
    elif int(lux) < threshold:
        return False
    
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