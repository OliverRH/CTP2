from ast import While
import yaml
from yaml.loader import FullLoader

with open('/opt/zigbee2mqtt/data/configuration.yaml') as f:
    data = yaml.load(f, Loader=FullLoader)
    print("TEST")
    #print(data['devices'])
    
    devices = data['devices']
    print(devices)
    #friendly_devices = devices['friendly_name']    
    #print(friendly_devices)
    
    array_devices = []
    
    print(len(devices))
    
    for device in devices:
        #print(device)
        array_devices.append(device)
    
    #print(array_devices)
    
    print(array_devices[0])
    
    """
    print('After Sorting')
    sorted_data = yaml.dump(data, sort_keys=True)
    print(sorted_data)
    """