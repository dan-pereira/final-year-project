#!/usr/bin/python3

import datetime
time = datetime.datetime.now()
path='/home/pi/fyp/data/'
end='.txt'

def store(name,value):
    print(name,value)
    with open(path+name+end,'a') as file:
        timeStamp = str(time.strftime("%d-%m %H:%M:%S"))
        data = timeStamp+' '+str(value)+'\n'
        file.write(data)

from gpiozero import MCP3008
def mcp3008():
    '''
    channel 0,1,2 are for plants
    channel 7 is water level
    '''
    for i in range(8):
        value = MCP3008(channel=i).value
        name= 'mcp0'+str(i)
        store(name,str(value))
    return

import Adafruit_DHT
def DHT11():
    sensor = Adafruit_DHT.DHT11
    pin = 4 #GPIO_NUM
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    value = str(humidity)+'% '+str(temperature)+'°C'
    store('airHumidityTemp',value)

import os
import glob
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm') # these allow the prog to read sensor try without and reboot
device_folder = glob.glob('/sys/bus/w1/devices/28*')[0]
device_file = device_folder + '/w1_slave'
def DS18B20():
    with open(device_file, 'r') as f:
        line = f.readlines()[-1]
    t= line[line.rfind('t=')+2:-1]
    t=float(t)/1000.0
    store('soilTemp',str(t)+'°C')
    return

if __name__ == '__main__':
    mcp3008()
    DHT11() #takes a few seconds
    DS18B20()
