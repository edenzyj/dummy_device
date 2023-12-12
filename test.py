import time

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

while 1:
    p = ps.getData()
    if p: print('ps', p)

    c = co2.getData()
    if c:  print('co2', c)

    t = tp_and_rh.getData()
    if t:  print('tp_and_rh', t)

    e = ec.getData()
    if e: print('ec', e)

    p = ph.getData()
    if p: print('ph', p)

    u = uv.getData()
    if u: print('uv', u)


    time.sleep(1)
