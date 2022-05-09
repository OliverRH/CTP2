from ast import While
import yaml
from yaml.loader import FullLoader
from setup_database import *

column_values = "NULL, " + "'" + room_number + "'" + ", " + "'" + date_time + "'"

config.read('config_db.ini')
#print(config['mySQL_login']['db_user'])
ip_host = config['mySQL_login']['ip_host']
db_user = config['mySQL_login']['db_user']
db_pass = config['mySQL_login']['db_pass']

CTP2_db_name = config['mySQL_db']['ctp2_db_name']
CTP2_db_table_room = config['mySQL_db']['ctp2_db_table_room']

column_names_room = config['mySQL_db']['ctp2_db_table_room_columns_names']
insert_sql(ip_host, db_user, db_pass, CTP2_db_name, CTP2_db_table_room, column_names_room, column_values)


with open('/opt/zigbee2mqtt/data/configuration.yaml') as f:
    data = yaml.load(f, Loader=FullLoader)
    
    devices = data['devices']

    for device in devices:
        print(device)
    
    """
    print('After Sorting')
    sorted_data = yaml.dump(data, sort_keys=True)
    print(sorted_data)
    """