import random 
import datetime

ServerURL = 'https://class.iottalk.tw' #For example: 'https://iottalk.tw'
MQTT_broker = 'class.iottalk.tw' # MQTT Broker address, for example:  'iottalk.tw' or None = no MQTT support
MQTT_port = 5566
MQTT_encryption = True
MQTT_User = 'iottalk'
MQTT_PW = 'iottalk2023'

device_model = 'Dummy_Device'
IDF_list = ['Dummy_Sensor']
ODF_list = ['Dummy_Control']
device_id = '31283301711221413' #if None, device_id = MAC address
device_name = 'eden_device'
exec_interval = 1  # IDF/ODF interval

def on_register(r):
    print('Server: {}\nDevice name: {}\nRegister successfully.'.format(r['server'], r['d_name']))

def Dummy_Sensor():
    return str(datetime.datetime.now())[17:]
    #return random.randint(0, 100)

delay_list = []

def Dummy_Control(data:list):
    end_time = str(datetime.datetime.now())[17:]
    time = float(end_time) - float(data[0])
    if time < 0: time = time + 60
    delay_list.append(time)
    print(time)
