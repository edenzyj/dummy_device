import random 
import datetime

ServerURL = 'https://class.iottalk.tw' #For example: 'https://iottalk.tw'
MQTT_broker = None # MQTT Broker address, for example:  'iottalk.tw' or None = no MQTT support
MQTT_port = 5566
MQTT_encryption = True
MQTT_User = 'iottalk'
MQTT_PW = 'iottalk2023'

device_model = 'Dummy_Device'
IDF_list = ['Dummy_Sensor']
ODF_list = ['Dummy_Control']
device_id = '31283301711220137' #if None, device_id = MAC address
device_name = 'eden_device'
exec_interval = 1  # IDF/ODF interval

def on_register(r):
    print('Server: {}\nDevice name: {}\nRegister successfully.'.format(r['server'], r['d_name']))

def I312833017():
    return str(datetime.datetime.now())
    #return random.randint(0, 100)

def O312833017(data:list):
    end_time = str(datetime.datetime.now())
    time = int(end_time) - int(data[0])
    print(time)
