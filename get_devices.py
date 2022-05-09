import yaml
from yaml.loader import FullLoader

with open('/opt/zigbee2mqtt/data/configuration.yaml') as f:
    data = yaml.load(f, Loader=FullLoader)
    print(data)
    print("TEST: " + data['devices'])
    
    print('After Sorting')
    sorted_data = yaml.dump(data, sort_keys=True)
    print(sorted_data)