#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import json

'''
Called From crontab
Turns on water pumps
'''

path='/home/pi/src/configs/'
pins = [14,15,18]
# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)
GPIO.output(pins, GPIO.HIGH)

def water(pin,s):
    GPIO.output(pin, GPIO.LOW)  # Turn motor on
    time.sleep(s)
    GPIO.output(pin, GPIO.HIGH)  # Turn motor off
    return

def manWater(plantNo):
    val = 0.3
    pin = pins[plantNo]
    print('pump',plantNo,'run for',val,'seconds')
    water(pin,val)
    return

if __name__ == '__main__':

    #get config
    fileName = path+'q_learn_config.json'
    with open(fileName, 'r') as configFile:
        data=configFile.read()
    config=json.loads(data)

    try:
        for key,val in config["controller"].items():
            key = int(key)
            pin = pins[key]
            print('pump',key,'run for',val,'seconds')
            water(pin,val)

    except KeyboardInterrupt:
        pass

    finally:
        GPIO.cleanup()
