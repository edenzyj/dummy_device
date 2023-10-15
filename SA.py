import random 
import datetime

ServerURL = 'https://3.iottalk.tw' #For example: 'https://iottalk.tw'
MQTT_broker = '3.iottalk.tw' # MQTT Broker address, for example:  'iottalk.tw' or None = no MQTT support
MQTT_port = 5566
MQTT_encryption = True
MQTT_User = 'iottalk'
MQTT_PW = 'iottalk2023'

device_model = '312833017_new'
IDF_list = ['I312833017']
ODF_list = ['O312833017']
device_id = '31283301710151649' #if None, device_id = MAC address
device_name = 'eden_device'
exec_interval = 1  # IDF/ODF interval

def on_register(r):
    print('Server: {}\nDevice name: {}\nRegister successfully.'.format(r['server'], r['d_name']))

def I312833017():
    return '312833017' + str(datetime.datetime.now())
    #return random.randint(0, 100)

def O312833017(data:list):
    print(data[0])
