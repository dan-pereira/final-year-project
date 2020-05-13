#!/usr/bin/python3
from gpiozero import MCP3008
import Adafruit_DHT
import os
import glob
import time
import sys


def mcp3008(values):
    '''
    channel 0,1,2 are for plants
    channel 7 is water level
    '''
    for i in range(8):
        value = MCP3008(channel=i).value
        name = 'mcp0' + str(i)

        if i < 7:
            value = 100 - (((value - 0.25) / (0.6)) * 100)  # moisture inverted min = 0.25 max = 0.85
        else:
            value = (((value - 0.004) / (0.135)) * 100)  # waterLevel min = 0.005 max = 0.14
        value = 0 if value < 0 else value
        value = 100 if value > 100 else value

        values[name] = value
    print('mcp,fin')
    return  # 'mcp0-7',values


def DHT11(values):
    sensor = Adafruit_DHT.DHT11
    pin = 4  # GPIO_NUM
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    value = str(humidity) + '% ' + str(temperature) + '°C'
    values['airTemp'] = temperature
    values['humidity'] = humidity
    print('DHT,fin')
    return  # 'air HumidityTemp' , [humidity,temperature]


def DS18B20(values):
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')  # these allow the prog to read sensor try without and reboot
    device_folder = glob.glob('/sys/bus/w1/devices/28*')[0]
    device_file = device_folder + '/w1_slave'
    with open(device_file, 'r') as f:
        line = f.readlines()[-1]
    t = line[line.rfind('t=') + 2:-1]
    t = float(t) / 1000.0
    values['soilTemp'] = t
    print('DS1,fin')
    return  # 'soilTemp', [t]


def readSensors():
    sensors = [DHT11, mcp3008, DS18B20]

    values = {}
    DHT11(values)
    mcp3008(values)
    DS18B20(values)
    return values


if __name__ == '__main__':
    values = readSensors()
    print()
    for k, v in values.items():
        print(k, v)
