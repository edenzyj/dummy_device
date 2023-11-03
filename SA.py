import random 
from datetime import datetime as dt
import DAN

ServerURL = 'https://class.iottalk.tw' #For example: 'https://iottalk.tw'
MQTT_broker = None # MQTT Broker address, for example:  'iottalk.tw' or None = no MQTT support
MQTT_port = 5566
MQTT_encryption = True
MQTT_User = 'iottalk'
MQTT_PW = 'iottalk2023'

device_model = '312833017'
IDF_list = ['I312833017']
ODF_list = ['O312833017']
device_id = '11011434' #if None, device_id = MAC address
device_name = 'eden_class'
exec_interval = 1  # IDF/ODF interval

def on_register(r):
    print('Server: {}\nDevice name: {}\nRegister successfully.'.format(r['server'], r['d_name']))

def I312833017():
    time_string = DAN.get_alias('I312833017')[0]
    time_list = time_string.split('-')
    begin = time_list[0]
    end = time_list[1]
    now = (str)(dt.now().time())
    if now > begin and now < end:
        return 1
    return 0
    #return random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100) 

def O312833017(data:list):
    print(data[0])
