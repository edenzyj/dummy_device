import random 
import datetime

from sensors import sensorCO2_API
from sensors import sensorEC_API
from sensors import sensorPH_API
from sensors import sensorPS_API
from sensors import sensorUV_API
from sensors import sensorSHT31_API

ps = sensorPS_API()
ps.start()

co2 = sensorCO2_API()
co2.start()

tp_and_rh = sensorSHT31_API()
tp_and_rh.start()

ec = sensorEC_API()
ec.start()

ph = sensorPH_API()
ph.start()

uv = sensorUV_API()
uv.start()

ServerURL = 'https://class.iottalk.tw' #For example: 'https://iottalk.tw'
MQTT_broker = 'class.iottalk.tw' # MQTT Broker address, for example:  'iottalk.tw' or None = no MQTT support
MQTT_port = 5566
MQTT_encryption = True
MQTT_User = 'iottalk'
MQTT_PW = 'iottalk2023'

device_model = 'C312833017'
IDF_list = ['AtPressure', 'CO2', 'EC', 'Humidity1', 'Humidity2', 'IR', 'Luminance',
            'Moisture', 'PH', 'SoilTemp', 'Temperature1', 'Temperature2', 'UV']
ODF_list = ['Dummy_Control']
device_id = '31283301712120918' #if None, device_id = MAC address
device_name = 'eden_device'
exec_interval = 1  # IDF/ODF interval

def on_register(r):
    print('Server: {}\nDevice name: {}\nRegister successfully.'.format(r['server'], r['d_name']))

def AtPressure():
    p = ps.getData()
    if p:
        v, _, _ = p
        #print("AtPressure: {}".format(v))
        return v
    else:
        return None
    
def CO2():
    p = co2.getData()
    if p:
        #print("CO2: {}".format(p))
        return 
    else:
        return None
    
def EC():
    p = ec.getData()
    if p:
        _, _, v = p
        #print("EC: {}".format(v))
        return v
    else:
        return None

def Humidity1():
    p = ps.getData()
    if p:
        _, _, v = p
        #print("Humidity1: {}".format(v))
        return v
    else:
        return None

def Humidity2():
    p = tp_and_rh.getData()
    if p:
        _, v = p
        #print("Humidity2: {}".format(v))
        return v
    else:
        return None

def IR():
    p = uv.getData()
    if p:
        _, _, v = p
        #print("IR: {}".format(v))
        return v
    else:
        return None

def Luminance():
    p = uv.getData()
    if p:
        _, v, _ = p
        #print("Luminance: {}".format(v))
        return v
    else:
        return None

def Moisture():
    p = ec.getData()
    if p:
        v, _, _ = p
        #print("Moisture: {}".format(v))
        return v
    else:
        return None

def PH():
    p = ph.getData()
    if p:
        #print("PH: {}".format(p))
        return p
    else:
        return None

def SoilTemp():
    p = ec.getData()
    if p:
        _, v, _ = p
        #print("SoilTemp: {}".format(v))
        return v
    else:
        return None

def Temperature1():
    p = ps.getData()
    if p:
        _, v, _ = p
        #print("Temperature1: {}".format(v))
        return v
    else:
        return None

def Temperature2():
    p = tp_and_rh.getData()
    if p:
        v, _ = p
        #print("Temperature2: {}".format(v))
        return v
    else:
        return None

def UV():
    p = uv.getData()
    if p:
        v, _, _ = p
        #print("UV: {}".format(v))
        return v
    else:
        return None

def Dummy_Control(data):
    print(data[0])
