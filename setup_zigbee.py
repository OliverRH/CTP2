import configparser
import sys

#Creates config.ini file that contains credentials for database login and information about the database 
#----------------------------------------------------------------
config = configparser.ConfigParser()
    
def create_config_file(Pi_ip_address, Pi_ip_port, zigbee_subscriber_address, zigbee_publisher_address):

    config['zigbee2mqtt'] = {'Pi_ip_address': Pi_ip_address,
                             'Pi_ip_port': Pi_ip_port,
                             'zigbee_subscriber_address': zigbee_subscriber_address,
                             'zigbee_publisher_address': zigbee_publisher_address}
    
    with open('config_zigbee.ini', 'w+') as configfile:
        config.write(configfile)
#----------------------------------------------------------------

print("\n----------------------------------------------------------------")
print("IP address of the Raspberry Pi:", sys.argv[1])
print("\nName of the zigbee subscriber address:", sys.argv[2])
print("\nName of the zigbee publisher address:", sys.argv[3])
print("----------------------------------------------------------------\n")

Pi_ip_address = sys.argv[1]
Pi_ip_port = sys.argv[2]
zigbee_subscriber_address = sys.argv[3]
zigbee_publisher_address = sys.argv[4]

create_config_file(Pi_ip_address, Pi_ip_port, zigbee_subscriber_address, zigbee_publisher_address)
