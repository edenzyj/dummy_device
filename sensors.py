import re, time, json, threading, requests, traceback
from datetime import datetime
import paho.mqtt.client as mqtt

MQTT_broker = 'sdwan.iottalk.tw' 
MQTT_port = 6688 
MQTT_User = 'iottalk'
MQTT_PW = 'iottalk2023'
MQTT_encryption = False

def on_connect(client, userdata, flags, rc):
    if not rc:
        print('MQTT broker: {}'.format(MQTT_broker))
        topic_list=[('141901000002//AtPressure',0), ('141901000002//Humidity1',0), ('141901000002//Temperature1',0), ('141901000002//CO2',0), ('141901000002//Humidity2',0), ('141901000002//Temperature2',0), ('141901000002//UV1',0), ('141901000002//Luminance',0), ('141901000002//Infrared',0), ('141901000002//Moisture1',0), ('141901000002//SoilEC-I',0), ('141901000002//SoilTemp-I',0), ('141901000002//PH1',0), ('141901000002//WindSpeed',0), ('141901000002//WindDir',0), ('141901000002//RainMeter',0)]
        r = client.subscribe(topic_list)
        if r[0]: print('Failed to subscribe topics. Error code:{}'.format(r))
    else: print('Connect to MQTT borker failed. Error code:{}'.format(rc))
        
def on_disconnect(client, userdata,  rc):
    print('MQTT Disconnected. Re-connect...')
    client.reconnect()

sensors={}
def on_message(client, userdata, msg):
    global sensors
    samples = json.loads(msg.payload)
    DF_name = msg.topic.split('//')[1]
    DF_data = samples['samples'][0][1][0]
    sensors[DF_name] = DF_data
    #print('{}: {}\n{}'.format(DF_name, DF_data, sensors))
    

def MQTT_config(client):
    client.username_pw_set(MQTT_User, MQTT_PW)
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    if MQTT_encryption: client.tls_set()
    client.connect(MQTT_broker, MQTT_port, keepalive=60)

mqttc = mqtt.Client()
MQTT_config(mqttc)
mqttc.loop_start()


class sensorCO2_API:
    def __init__(self):
        pass

    state = 'SUSPEND'
    def start(self):
        self.state = 'RESUME'

    def getData(self):
        if self.state == 'RESUME': return sensors.get('CO2')
        else: return None

class sensorPH_API:
    def __init__(self):
        pass

    state = 'SUSPEND'
    def start(self):
        self.state = 'RESUME'

    def getData(self):
        if self.state == 'RESUME': return sensors.get('PH1')
        else: return None

class sensorPS_API:
    def __init__(self):
        pass

    state = 'SUSPEND'
    def start(self):
        self.state = 'RESUME'

    def getData(self):
        if self.state == 'RESUME':
            A = sensors.get('AtPressure')
            B = sensors.get('Temperature1')
            C = sensors.get('Humidity1')
            if None in [A, B, C]: return None
            return A, B, C
        else: return None

class sensorEC_API:
    def __init__(self):
        pass

    state = 'SUSPEND'
    def start(self):
        self.state = 'RESUME'

    def getData(self):
        if self.state == 'RESUME':
            A = sensors.get('Moisture1')
            B = sensors.get('SoilTemp-I')
            C =  sensors.get('SoilEC-I')
            if None in [A, B, C]: return None
            return A, B, C
        else: return None

class sensorSHT31_API:
    def __init__(self):
        pass

    state = 'SUSPEND'
    def start(self):
        self.state = 'RESUME'

    def getData(self):
        if self.state == 'RESUME':
            A = sensors.get('Temperature2')
            B = sensors.get('Humidity2')
            if None in [A, B]: return None
            return A, B
        else: return None

class sensorUV_API:
    def __init__(self):
        pass

    state = 'SUSPEND'
    def start(self):
        self.state = 'RESUME'

    def getData(self):
        if self.state == 'RESUME':
            A = sensors.get('UV1')
            B = sensors.get('Luminance')
            C =  sensors.get('Infrared')
            if None in [A, B, C]: return None
            return A, B, C
        else: return None


if __name__ == '__main__':
    pass
