#!/usr/bin/python3

import threading
from gpiozero import MCP3008
import Adafruit_DHT
import os
import glob
import time

def mcp3008(values):
    '''
    channel 0,1,2 are for plants
    channel 7 is water level
    '''
    for i in range(8):
        value = MCP3008(channel=i).value
        name= 'mcp0'+str(i)
        values[name]=value
    return# 'mcp0-7',values

def DHT11(values):
    sensor = Adafruit_DHT.DHT11
    pin = 4 #GPIO_NUM
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    value = str(humidity)+'% '+str(temperature)+'°C'
    #store('airHumidityTemp',value)
    values['airTemp']=temperature
    values['humidity']= humidity
    return# 'air HumidityTemp' , [humidity,temperature]

def DS18B20(values):
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm') # these allow the prog to read sensor try without and reboot
    device_folder = glob.glob('/sys/bus/w1/devices/28*')[0]
    device_file = device_folder + '/w1_slave'
    with open(device_file, 'r') as f:
        line = f.readlines()[-1]
    t= line[line.rfind('t=')+2:-1]
    t=float(t)/1000.0
    #store('soilTemp',str(t)+'°C')
    values['soilTemp']=t
    return# 'soilTemp', [t]

def readSensors():
    sensors = [DHT11, mcp3008, DS18B20]
    #sensors = [mcp3008, DS18B20]
    threads = []
    values = {}
    start=time.time()
    for sensor in sensors:
        thread = threading.Thread(name=sensor.__name__,target=sensor,args=[values])
        thread.start()
        threads.append(thread)
        print(thread.name,'Started')

    for thread in threads:
        thread.join()
        print(thread.name,'ended:',str(time.time()-start)+'s')
        #results.append(thread.result())

    #print('read vals:',values)
    return values

if __name__ == '__main__':
    values = readSensors()
    print()
    for k,v in values.items():
       print(k,v)
