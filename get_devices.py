import yaml
from yaml.loader import FullLoader

with open('/opt/zigbee2mqtt/data/configuration.yaml') as f:
    data = yaml.load(f, Loader=FullLoader)
    print("TEST")
    #print(data['devices'])
    
    devices = data['devices']
    friendly_devices = devices['friendly_name']
    
    for device in friendly_devices:
        print(device)
    
    
    """
    print('After Sorting')
    sorted_data = yaml.dump(data, sort_keys=True)
    print(sorted_data)
    """